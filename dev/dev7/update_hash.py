import hashlib
from ruamel.yaml import YAML
import os

def extract_function_code(py_code, function_name):
    """
    指定された関数名のコードをインデントに基づいて抽出します。

    Parameters:
    - py_code (str): Pythonコード全体のテキスト
    - function_name (str): 抽出したい関数の名前

    Returns:
    - str: 関数コードの文字列
    """
    lines = py_code.splitlines()
    func_code_lines = []
    in_function = False
    base_indent = None

    for line in lines:
        # 関数の先頭を探す
        if line.strip().startswith(f"def {function_name}(") and not in_function:
            in_function = True
            base_indent = len(line) - len(line.lstrip())
            func_code_lines.append(line)
            continue

        # 関数内にいる場合、適切なインデントの範囲内でコードを追加
        if in_function:
            current_indent = len(line) - len(line.lstrip())

            # 空行や関数内部の行を追加
            if line.strip() == "" or current_indent > base_indent:
                func_code_lines.append(line)
            else:
                # インデントが基準に戻った場合、関数の終わりとみなす
                break

    return "\n".join(func_code_lines)

def update_function_hash(yaml_file_path):
    """
    YAMLファイルのtest_casesに記載されている関数のコードを読み取り、
    SHA-256のハッシュを計算し、__function_hash__に書き込みます。

    Parameters:
    - yaml_file_path (str): YAMLファイルのパス
    """
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(sequence=4, offset=2)

    # YAMLファイルを読み込み
    with open(yaml_file_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    # settingsのroot_pathとfile_nameを取得
    root_path = data['settings']['root_path']
    file_name = data['settings']['file_name']
    target_file_path = os.path.join(root_path, file_name)

    # 指定された.pyファイルを読み込み
    with open(target_file_path, 'r', encoding='utf-8') as py_file:
        py_code = py_file.read()

    # test_cases内の各関数について、function_nameからコードを取得してハッシュを生成
    for test_case in data['test_cases']:
        function_name = test_case.get('function_name')

        # 関数コードを抽出
        function_code = extract_function_code(py_code, function_name)
        if not function_code:
            print(f"Error: {function_name}関数が{file_name}内に見つかりません")
            continue

        # 関数コードのハッシュを計算
        function_hash = hashlib.sha256(function_code.encode('utf-8')).hexdigest()
        
        # ハッシュをYAMLファイルに書き込む
        test_case['__function_hash__'] = function_hash

    # 更新されたYAMLデータを書き戻し
    with open(yaml_file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file)

def main():
    yaml_file_path = 'sample.yaml'  # 読み込むYAMLファイルパス
    update_function_hash(yaml_file_path)

# main関数の実行
if __name__ == "__main__":
    main()
