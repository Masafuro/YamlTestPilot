from ruamel.yaml import YAML

def reload_yaml(input_file, output_file):
    yaml = YAML()  # ruamel.yamlのインスタンスを作成
    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.load(f)  # sample.yamlを読み込む

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)  # 読み込んだデータをそのまま別名で保存

# ファイル名を指定して実行
input_file = 'sample.yaml'
output_file = 'sample_reload.yaml'
reload_yaml(input_file, output_file)
