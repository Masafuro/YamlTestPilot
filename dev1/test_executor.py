import yaml_parser
import test_code_generator
import tempfile
import subprocess
import os

def execute_generated_tests(yaml_data):
    """
    YAMLデータから生成されたテストコードを一時ファイルに保存し、
    pytestを使って実行し、その結果を返す。
    """
    # テストコードを生成
    generated_code = test_code_generator.generate_test_code(yaml_data)

    # 一時ファイルにテストコードを書き込む
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
        temp_file_path = temp_file.name
        temp_file.write(generated_code.encode())  # バイナリモードで書き込む

    # pytestで一時ファイルのテストを実行
    try:
        result = subprocess.run(["pytest", temp_file_path], capture_output=True, text=True)
        return result.stdout  # 実行結果を返す
    finally:
        # 一時ファイルの削除
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

def main():
    # YAMLファイルからデータを読み込む
    file_path = "sample.yaml"
    yaml_data = yaml_parser.parse_yaml(file_path)
    
    # テストを実行
    test_output = execute_generated_tests(yaml_data)
    print("Test Output:\n", test_output)

if __name__ == "__main__":
    main()
