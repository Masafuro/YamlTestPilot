from ruamel.yaml import YAML
import importlib.util
import os
import time
from hashlib import sha256
from collections import OrderedDict
from datetime import datetime

yaml = YAML()
yaml.default_flow_style = False
yaml.allow_unicode = True

from InquirerPy import inquirer

def select_python_file(root_path):
    """
    指定されたルートパス内の .py ファイルをリストし、CLI で選択させる関数。
    選択されたファイルのファイルパスとファイル名を返す。
    
    Args:
        root_path (str): ルートパス

    Returns:
        tuple: 選択されたファイルのファイルパスとファイル名
    """
    # ルートパス内の .py ファイルをリストアップ
    py_files = [f for f in os.listdir(root_path) if f.endswith('.py')]
    
    if not py_files:
        print("指定されたディレクトリに .py ファイルが見つかりません。")
        return None, None

    # CLIでファイルを選択
    selected_file = inquirer.select(
        message="テスト対象の Python ファイルを選択してください:",
        choices=py_files,
    ).execute()

    # 選択されたファイルのフルパスとファイル名を返す
    full_path = os.path.join(root_path, selected_file)
    return full_path, selected_file

def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = yaml.load(file)
    
    # expected_outputがエラー型を表す辞書の場合、Pythonのエラー型に変換
    for function in data["functions"]:
        for test_case in function["test_cases"]:
            expected_output = test_case.get("expected_output")
            if isinstance(expected_output, dict) and "error" in expected_output:
                # 辞書形式のまま保存し、Pythonエラー型にも変換
                test_case["original_expected_output"] = expected_output
                error_type_name = expected_output["error"]
                test_case["expected_output"] = globals().get(error_type_name, Exception)
            else:
                # 通常の出力の場合、そのまま保存
                test_case["original_expected_output"] = expected_output
    
    return data

def import_function(module_path, function_name):
    spec = importlib.util.spec_from_file_location("module.name", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)

def calculate_sha256(file_path):
    """指定されたファイルのSHA-256ハッシュを計算する"""
    hash_sha256 = sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def run_tests(test_file_path, program_path, result_file_path):
    # テスト開始時間
    start_time = datetime.now()
    
    # テストケースを読み込む
    test_data = load_yaml(test_file_path)
    
    # テスト対象ファイルのSHA-256ハッシュを計算
    file_hash = calculate_sha256(program_path)

    # 結果を保存するための構造
    results = {"meta": OrderedDict(), "functions": []}

    # テスト項目の数と成功数をカウント
    total_tests = 0
    successful_tests = 0

    # 各関数に対してテストを実行
    for function_data in test_data["functions"]:
        function_name = function_data["function_name"]
        description = function_data["description"]
        function_results = {
            "function_name": function_name,
            "description": description,
            "results": []
        }

        # 関数をインポート
        function = import_function(program_path, function_name)

        # 各テストケースを実行
        for case in function_data["test_cases"]:
            total_tests += 1
            case_start_time = time.time()
            inputs = case["inputs"]
            expected_output = case["expected_output"]
            original_expected_output = case["original_expected_output"]
            description = case["description"]

            try:
                # 関数を実行して出力を取得
                actual_output = function(*inputs)
                
                # 出力のチェック：エラーを期待している場合はFailとする
                if isinstance(expected_output, type) and issubclass(expected_output, Exception):
                    status = "Fail"  # エラーが発生しないときは失敗
                else:
                    status = "Success" if actual_output == expected_output else "Fail"

            except Exception as e:
                actual_output = f"{type(e).__name__}: {str(e)}"
                
                # 発生したエラーの型が期待通りであればSuccess、それ以外はFail
                if isinstance(expected_output, type) and isinstance(e, expected_output):
                    status = "Success"
                else:
                    status = "Fail"

            # 成功した場合にカウント
            if status == "Success":
                successful_tests += 1

            case_end_time = time.time()
            execution_time_ms = (case_end_time - case_start_time) * 1000

            # テストケース結果を記録（順序を指定）
            function_results["results"].append(OrderedDict([
                ("description", description),
                ("inputs", inputs),
                ("expected_output", original_expected_output),  # expected_outputを先に
                ("actual_output", actual_output),               # actual_outputを次に
                ("status", status),
                ("execution_time_ms", execution_time_ms)
            ]))

        results["functions"].append(function_results)

    # テスト終了時間
    end_time = datetime.now()
    total_time = (end_time - start_time).total_seconds()

    # metaフィールドを設定
    results["meta"] = OrderedDict([
        ("target_file_path", program_path),
        ("file_hash", file_hash),
        ("start_time", start_time.isoformat()),
        ("end_time", end_time.isoformat()),
        ("total_duration_seconds", total_time),
        ("total_tests", total_tests),
        ("successful_tests", successful_tests)
    ])

    # 結果をYAML形式で保存
    with open(result_file_path, "w", encoding="utf-8") as result_file:
        yaml.dump(results, result_file)
    print(f"Results saved to {result_file_path}")

if __name__ == "__main__":
    # パスの設定
    program_root = "./"

    # ルートパスを指定
    root_path = program_root  # ここにルートパスを指定

    # Pythonファイルを選択
    file_path, file_name = select_python_file(root_path)
    
    if file_path and file_name:
        print(f"選択されたファイル: {file_name}")
        print(f"ファイルパス: {file_path}")
    else:
        print("ファイルの選択がキャンセルされました。")
    
    yaml_extension = ".yaml"
    base = os.path.splitext(file_name)[0]  # ファイル名から拡張子を除去
    yaml_file_name = base + yaml_extension

    test_file = os.path.join(program_root, f"test_cases/{yaml_file_name}")
    program_file = os.path.join(program_root, file_name)
    result_file = os.path.join(program_root, f"results/r_{yaml_file_name}")
    
    # テストを実行
    run_tests(test_file, program_file, result_file)
