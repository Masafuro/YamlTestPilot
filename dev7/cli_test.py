from InquirerPy import inquirer
import os

# .pyファイルがあるディレクトリのパスを指定
directory = "./"

# ディレクトリ内のファイルを取得し、.pyファイルのみリスト化
py_files = [f for f in os.listdir(directory) if f.endswith('.py')]

# ファイルリストが空でないか確認
if not py_files:
    print("No Python files found in the specified directory.")
else:
    # ファイルリストからユーザーに選択してもらう
    selected_file = inquirer.select(
        message="Select the Python file to test:",
        choices=py_files,
        default=None
    ).execute()

    # 選択されたファイル名を表示（ここで任意の処理を開始）
    print(f"You selected: {selected_file}")
    # ここに選択されたファイルに対する処理（例：テストの実行など）を記述
