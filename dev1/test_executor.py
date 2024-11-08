import yaml
import yaml_parser
import test_code_generator
import tempfile
import subprocess
import os
import re

def execute_tests_and_collect_results(yaml_data):
    """
    YAMLデータから生成されたテストコードを一時ファイルに保存し、
    pytestを使って実行し、その結果を標準出力から解析して取得する。
    """
    # テストコードを生成
    generated_code = test_code_generator.generate_test_code(yaml_data)

    # 一時ファイルにテストコードを書き込む
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
        temp_file_path = temp_file.name
        temp_file.write(generated_code.encode())  # バイナリモードで書き込む

    # pytestで一時ファイルのテストを実行し、結果を取得
    result_data = {}
    try:
        result = subprocess.run(["pytest", temp_file_path, "--tb=short", "--disable-warnings"], capture_output=True, text=True)
        print("Test Output:\n", result.stdout)
        print("Test Errors:\n", result.stderr)
        
        # pytestの標準出力を解析して結果を抽出
        for line in result.stdout.splitlines():
            match = re.search(r'(\w+): (test_\w+): (\w+)', line)
            if match:
                result_key = match.group(2)  # テスト関数名
                status = match.group(3)  # 成功または失敗のステータス
                result_data[result_key] = {
                    "outcome": status,
                    "execution_time_ms": None,  # 実行時間は取得できないためNoneを設定
                    "actual_return": None  # 戻り値は標準出力から取得できないためNoneを設定
                }

    finally:
        # 一時ファイルの削除
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

    return result_data

def update_yaml_with_results(yaml_data, result_data):
    """
    テスト結果を元のYAMLデータに格納し、__result__フィールドを更新する。
    """
    # 各テスト結果をyaml_data内の該当するテストケースに反映
    for test_case in yaml_data.get("test_cases", []):
        function_name = test_case.get("function_name")
        
        for summary in test_case.get("summary", []):
            for case in summary.get("cases", []):
                # caseの名前と一致するテスト結果を探す
                case_name = case.get("name")
                result_key = f"test_{function_name}_{case_name.replace(' ', '_')}"
                
                # result_dataから結果を取得して反映
                result_info = result_data.get(result_key, {})
                if result_info:
                    case["__result__"]["status"] = result_info.get("outcome")
                    case["__result__"]["actual_return"] = result_info.get("actual_return")
                    case["__result__"]["execution_time_ms"] = result_info.get("execution_time_ms")
                    
    # デバッグ用の確認出力
    print("Updated YAML Data with Results:")
    print(yaml.dump(yaml_data))

def save_yaml(yaml_data, file_path):
    """
    更新されたYAMLデータを指定されたパスに保存する。
    """
    with open(file_path, "w") as file:
        yaml.dump(yaml_data, file, default_flow_style=False)
    print(f"YAML data saved to {file_path}")

def main():
    # YAMLファイルからデータを読み込む
    file_path = "sample.yaml"
    yaml_data = yaml_parser.parse_yaml(file_path)
    
    # テストを実行し、結果を収集
    result_data = execute_tests_and_collect_results(yaml_data)
    
    # YAMLデータにテスト結果を格納
    update_yaml_with_results(yaml_data, result_data)
    
    # YAMLデータをファイルに保存
    save_yaml(yaml_data, file_path)

if __name__ == "__main__":
    main()
