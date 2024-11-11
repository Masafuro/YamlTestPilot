import os
from InquirerPy import inquirer

def select_python_file(root_path):
    """
    指定されたルートパス内の .py ファイルをリストし、CLI で選択させる関数。
    選択されたファイルのファイルパスとファイル名を返す。
    
    Args:
        root_path (str): ルートパス

    Returns:
        tuple: 選択されたファイルのファイルパスとファイル名
    """
    # ルートパス内の .py ファイルをリストアップ
    py_files = [f for f in os.listdir(root_path) if f.endswith('.py')]
    
    if not py_files:
        print("指定されたディレクトリに .py ファイルが見つかりません。")
        return None, None

    # CLIでファイルを選択
    selected_file = inquirer.select(
        message="テスト対象の Python ファイルを選択してください:",
        choices=py_files,
    ).execute()

    # 選択されたファイルのフルパスとファイル名を返す
    full_path = os.path.join(root_path, selected_file)
    return full_path, selected_file

def main():
    # ルートパスを指定
    root_path = "../"  # ここにルートパスを指定

    # Pythonファイルを選択
    file_path, file_name = select_python_file(root_path)
    
    if file_path and file_name:
        print(f"選択されたファイル: {file_name}")
        print(f"ファイルパス: {file_path}")
    else:
        print("ファイルの選択がキャンセルされました。")

if __name__ == "__main__":
    main()
