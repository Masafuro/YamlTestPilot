from ruamel.yaml import YAML

def update_yaml_test_result(file_path, function_name, summary_name, test_case_name, 
                            status=None, actual_return=None, execution_time_ms=None):
    """
    YAMLファイル内の特定のテストケースの__result__を更新します。

    Parameters:
    - file_path (str): YAMLファイルのパス
    - function_name (str): 対象の関数名
    - summary_name (str): 対象のサマリ名
    - test_case_name (str): 更新するテストケースの名前
    - status (str, optional): 更新するステータス
    - actual_return (any, optional): 期待される戻り値
    - execution_time_ms (int, optional): 実行時間（ミリ秒単位）
    """
    
    yaml = YAML()
    yaml.preserve_quotes = True  # 引用符を保持
    yaml.indent(sequence=4, offset=2)  # インデントを設定

    # YAMLファイルを読み込み
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    # 該当するfunction_name, summary_name, test_case_nameを探して更新
    for test_case in data['test_cases']:
        if test_case.get('function_name') == function_name:
            for summary in test_case.get('summary', []):
                if summary.get('summary_name') == summary_name:
                    for case in summary.get('cases', []):
                        if case.get('case_name') == test_case_name:
                            # __result__に値を更新
                            if case.get('__result__'):
                                result = case['__result__'][0]
                                if status is not None:
                                    result['status'] = status
                                if actual_return is not None:
                                    result['actual_return'] = actual_return
                                if execution_time_ms is not None:
                                    result['execution_time_ms'] = execution_time_ms
                            break

    # 更新された内容を同じファイルに書き込み
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file)

def main():
    # 引数に応じて設定（例として指定）
    file_path = 'sample.yaml'  # ファイルパスを指定
    function_name = "add"
    summary_name = "Basic Additions"
    test_case_name = "Addition with Zero"
    
    # 更新したい項目
    status = "success5"
    actual_return = 10
    execution_time_ms = 2000
    
    # 関数を実行してYAMLを更新
    update_yaml_test_result(file_path, function_name, summary_name, test_case_name, 
                            status=status, actual_return=actual_return, execution_time_ms=execution_time_ms)

# main関数の実行
if __name__ == "__main__":
    main()
