import yaml
import os

def parse_yaml(file_path):
    """
    指定されたYAMLファイルを読み込み、データを辞書形式で返す関数。
    """
    # ファイルが存在するか確認
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    # YAMLファイルを読み込む
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error reading YAML file: {e}")
    
    return data

def main():
    # sample.yamlを指定してparse_yaml関数を実行
    file_path = 'sample.yaml'
    parsed_data = parse_yaml(file_path)
    
    # 結果を表示
    print("Parsed YAML Data:")
    print(parsed_data)

if __name__ == "__main__":
    main()
