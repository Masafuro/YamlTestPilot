import yaml

def extract_path_and_file(yaml_file_path):
    """
    指定されたYAMLファイルからroot_pathとfile_nameを抽出し、返します。
    
    Args:
        yaml_file_path (str): YAMLファイルのパス
    
    Returns:
        tuple: (root_path, file_name) の形式で返す
    """
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    # settingsからroot_pathとfile_nameを抽出
    root_path = data.get('settings', {}).get('root_path')
    file_name = data.get('settings', {}).get('file_name')
    
    return root_path, file_name

# main関数での実行
if __name__ == "__main__":
    yaml_file_path = 'sample.yaml'  # ユーザーから提供されたYAMLファイルのパス
    root_path, file_name = extract_path_and_file(yaml_file_path)
    print(root_path)
    print(file_name)
