import yaml

def update_yaml_with_name(file_path, target_name, field_path, new_value):
    """
    YAMLファイル内の指定された名前の要素のフィールドを更新する関数

    Args:
      file_path (str): YAMLファイルのパス
      target_name (str): 更新する要素のnameキーの値
      field_path (list): 更新するフィールドのパス (例: ['b', 'c'])
      new_value: 新しい値
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if not isinstance(data, list):
            raise ValueError("YAML data must be a list of dictionaries.")

        # nameで要素を検索
        target_dict = None
        for item in data:
            if item.get('name') == target_name:
                target_dict = item
                break

        if target_dict is None:
            raise ValueError(f"No element found with name: {target_name}")

        # field_pathに基づいてネストされた辞書にアクセス
        current_dict = target_dict
        for key in field_path[:-1]:
            current_dict = current_dict.get(key)
            if current_dict is None:
                raise ValueError(f"Invalid field path: {field_path}")

        # 値を更新
        current_dict[field_path[-1]] = new_value

        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, indent=2, allow_unicode=True)

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_path = 'sample.yaml'
    target_name = 'test1'
    field_path = ['b', 'c']
    new_value = 'updated_value'

    update_yaml_with_name(file_path, target_name, field_path, new_value)
    print(f"Updated '{field_path}' in '{file_path}' for '{target_name}' to '{new_value}'")