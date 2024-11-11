from ruamel.yaml import YAML
from datetime import datetime

def update_last_run(file_path, last_run_value):
    """
    YAMLファイル内のmetaセクションのlast_runに指定した値を記入します。

    Parameters:
    - file_path (str): YAMLファイルのパス
    - last_run_value (str): 記入したい日付と時刻の文字列（例："2023-11-10 12:34:56"）
    """
    
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(sequence=4, offset=2)

    # YAMLファイルを読み込み
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    # metaセクションのlast_runに値を更新
    if 'meta' in data:
        data['meta']['last_run'] = last_run_value

    # 更新された内容をファイルに書き戻し
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file)

def main():
    # ファイルパスと現在時刻の設定（例として現在時刻を設定）
    file_path = 'sample.yaml'  # ファイルパスを指定
    last_run_value = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 現在の日時を取得

    # 関数を実行してYAMLを更新
    update_last_run(file_path, last_run_value)

# main関数の実行
if __name__ == "__main__":
    main()
