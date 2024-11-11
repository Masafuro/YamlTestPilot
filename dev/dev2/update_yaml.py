import re

def update_yaml_value_regex(file_path, key_path, new_value):
    """
    正規表現を使用してYAMLファイルの特定のキーの値を直接更新します。

    Parameters:
    file_path (str): YAMLファイルのパス
    key_path (str): 更新したい項目の場所（スラッシュ区切り）
    new_value: 更新する新しい値
    """
    # 新しい値が文字列でない場合、YAML表記の形式に変換
    if isinstance(new_value, str):
        value_str = f'"{new_value}"'  # 文字列の場合、ダブルクォートで囲む
    else:
        value_str = str(new_value)    # 数値やNoneはそのまま

    # key_pathをスラッシュで分割して、正規表現パターンを作成
    pattern_path = key_path.replace('/', r'[ \t]*:[ \t]*\n[ \t]*')  # パスのフォーマット調整
    pattern = rf"({pattern_path}[ \t]*:[ \t]*)[^#\n]*"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 正規表現で該当の項目を置換
    new_content = re.sub(pattern, rf"\1{value_str}", content, flags=re.MULTILINE)

    # ファイルに書き込み
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

# 例: 特定のYAMLファイルの指定項目を変更する
file_path = "sample.yaml"
key_path = "test_cases/0/summary/0/cases/0/__result__/status"
new_value = "passed"

update_yaml_value_regex(file_path, key_path, new_value)
print(f"{key_path} has been updated to {new_value} in {file_path}")
