import yaml

# YAMLを辞書として読み込み
with open('example.yaml', 'r') as file:
    data = yaml.safe_load(file)

# 特定の箇所の値を変更
data['settings']['services'][0]['key'] = 'hello masafuro yaml'

# YAMLファイルとして再度保存
with open('example.yaml', 'w') as file:
    yaml.safe_dump(data, file)
