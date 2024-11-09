from ruamel.yaml import YAML

def update_status_in_yaml(input_file, output_file, target_name, new_status):
    yaml = YAML()
    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.load(f)  # YAMLデータを読み込む

    # 対象の要素を検索し、statusを更新
    updated = False  # 更新できたかの確認用フラグ
    for test_case in data.get('test_cases', []):
        for summary in test_case.get('summary', []):
            for case in summary.get('cases', []):
                if case.get('name') == target_name:
                    # __result__ 以下の status に新しい値を書き込む
                    if '__result__' in case:
                        case['__result__']['status'] = new_status
                        updated = True
                    else:
                        case['__result__'] = {'status': new_status}
                        updated = True
                    print(f"Updated status for case: {case.get('name')}")

    if not updated:
        print("Target name not found or status not updated.")

    # 更新されたデータを別名で保存
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)

# 使用例
input_file = 'sample.yaml'
output_file = 'sample_reload.yaml'
target_name = "Addition with Positive Integers"
new_status = "input_from_test"
update_status_in_yaml(input_file, output_file, target_name, new_status)
print(f"Status updated for {target_name} and saved to {output_file}.")
