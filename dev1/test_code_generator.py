import yaml_parser

def generate_test_code(yaml_data):
    """
    YAMLデータからテストコードを生成し、文字列として返す関数。
    """
    test_code_lines = []  # テストコードの行を格納するリスト

    # settingsセクションからroot_pathとmodule_fileを取得
    root_path = yaml_data.get("settings", {}).get("root_path")
    module_file = yaml_data.get("settings", {}).get("module_file")
    
    # root_pathをsys.pathに追加するコード行を生成
    if root_path:
        test_code_lines.append("import sys")
        test_code_lines.append(f"sys.path.append('{root_path}')")
    
    # module_fileからインポート文を生成
    if module_file:
        module_name = module_file.replace(".py", "")  # 拡張子を除去してモジュール名に変換
        test_code_lines.append(f"from {module_name} import *")  # 全ての関数をインポート

    # test_casesセクションを読み込み、各テストケースを処理
    for test_case in yaml_data.get("test_cases", []):
        function_name = test_case.get("function_name")
        function_description = test_case.get("function_description")
        
        # 各summary内のケースごとにテストコードを生成
        for summary in test_case.get("summary", []):
            for case in summary.get("cases", []):
                case_name = case.get("name")
                arguments = case.get("arguments", [])
                expected_return = case.get("expected_return")
                exception = case.get("exception")
                
                # テスト関数の名前を作成
                test_function_name = f"test_{function_name}_{case_name.replace(' ', '_')}"
                
                # テストコードのコメントとして、ケースの説明を追加
                test_code_lines.append(f"# {case_name}: {function_description}")
                
                # テストコードの本体を作成
                if exception and exception != "None":
                    # 例外を期待する場合のテストコード
                    test_code_lines.append(f"def {test_function_name}():")
                    test_code_lines.append(f"    try:")
                    test_code_lines.append(f"        {function_name}({', '.join(map(str, arguments))})")
                    test_code_lines.append(f"        assert False, 'Expected exception {exception} was not raised'")
                    test_code_lines.append(f"    except {exception}:")
                    test_code_lines.append(f"        pass  # Expected exception raised")
                else:
                    # 正常な戻り値を期待する場合のテストコード
                    test_code_lines.append(f"def {test_function_name}():")
                    test_code_lines.append(f"    result = {function_name}({', '.join(map(str, arguments))})")
                    test_code_lines.append(f"    assert result == {expected_return}, f'Expected {expected_return} but got {{result}}'")
                
                # 空行を追加して見やすく
                test_code_lines.append("")
    
    # 生成されたテストコードを1つの文字列に結合して返す
    return "\n".join(test_code_lines)

def main():
    # sample.yamlを読み込む
    file_path = "sample.yaml"
    yaml_data = yaml_parser.parse_yaml(file_path)
    
    # YAMLデータからテストコードを生成
    generated_code = generate_test_code(yaml_data)
    
    # 結果を表示（またはログに記録することも可能）
    print("Generated Test Code:")
    print(generated_code)

if __name__ == "__main__":
    main()
