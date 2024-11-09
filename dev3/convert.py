import yaml
import csv

def yaml_to_csv(yaml_file, csv_file):
    # YAMLファイルを読み込み
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # CSVファイルに書き込み
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # CSVのヘッダー行を定義
        header = [
            'function_name',
            'description',
            'case_name',
            'arguments',
            'expected_return',
            'exception',
            'status',
            'actual_return',
            'execution_time_ms'
        ]
        writer.writerow(header)
        
        # YAMLデータをフラットにして各行をCSVに書き込み
        for function in data.get('test_cases', []):
            function_name = function.get('function_name')
            description = function.get('description')
            for case in function.get('cases', []):
                # 各テストケースの情報を取得
                case_name = case.get('case_name')
                arguments = case.get('arguments')
                expected_return = case.get('expected_return')
                exception = case.get('exception')
                # __result__内の各項目を取得
                result = case.get('__result__', {})
                status = result.get('status')
                actual_return = result.get('actual_return')
                execution_time_ms = result.get('execution_time_ms')
                
                # CSV行に書き込むデータを準備
                row = [
                    function_name,
                    description,
                    case_name,
                    arguments,
                    expected_return,
                    exception,
                    status,
                    actual_return,
                    execution_time_ms
                ]
                writer.writerow(row)

# 使用例
yaml_file = 'sample.yaml'
csv_file = 'sample.csv'
yaml_to_csv(yaml_file, csv_file)
print(f"YAML data has been converted to {csv_file}")
