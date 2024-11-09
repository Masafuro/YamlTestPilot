import yaml_parser
import test_code_generator
import test_executor
from ruamel.yaml import YAML
import tempfile
import subprocess
import os
import re

def update_yaml_with_results(yaml_data, test_output):
    """
    pytestの出力結果を解析し、YAMLデータ内の各テストケースに結果を格納する。
    """
    # 正規表現を使ってpytestの出力から結果を抽出
    result_pattern = re.compile(r'(\w+)\s+::\s+(test_\w+)\s+\[\d+%\]')
    passed_cases = []
    failed_cases = []

    # pytest出力を解析して結果を取得
    for line in test_output.splitlines():
        match = result_pattern.search(line)
        if match:
            status, test_name = match.groups()
            if status == "PASSED":
                passed_cases.append(test_name)
            elif status == "FAILED":
                failed_cases.append(test_name)

    # YAMLデータ内の各テストケースを更新
    for test_case in yaml_data['test_cases']:
        for summary in test_case['summary']:
            for case in summary['cases']:
                test_function_name = f"test_{test_case['function_name']}_{case['name'].replace(' ', '_')}"
                
                # テストケースの結果を更新
                if test_function_name in passed_cases:
                    case['__result__']['status'] = "passed"
                elif test_function_name in failed_cases:
                    case['__result__']['status'] = "failed"
                else:
                    case['__result__']['status'] = "not_executed"

    return yaml_data

def save_updated_yaml(yaml_data, file_path):
    """
    更新されたYAMLデータを元のファイルに保存する。
    """
    yaml = YAML()
    yaml.preserve_quotes = True
    with open(file_path, 'w') as file:
        yaml.dump(yaml_data, file)

def main():
    # YAMLファイルのパス
    file_path = "sample.yaml"
    
    # YAMLファイルを読み込み
    yaml_data = yaml_parser.parse_yaml(file_path)
    
    # テストを実行し、結果を取得
    test_output = test_executor.execute_generated_tests(yaml_data)
    
    # テスト結果でYAMLデータを更新
    updated_yaml_data = update_yaml_with_results(yaml_data, test_output)
    
    # 更新されたYAMLデータを保存
    save_updated_yaml(updated_yaml_data, file_path)
    print(f"Updated YAML data saved to {file_path}")

if __name__ == "__main__":
    main()
