# YamlTestPilot
YamlTestPilot - A YAML-based tool that lets developers define, run, and track Python function tests, eliminating repetitive scripting and streamlining workflows.
The template YAML file for YamlTestPilot is available [here](https://github.com/Masafuro/YamlTestPilot/blob/main/template.yaml).

- YamlTestPilotは、YAMLのテキストファイルにテスト情報を記述することで、Python 関数のテストを定義、実行、追跡できるようにする一連のスクリプトセットです。
- このYAMLファイルはテンプレートをChatGPT等のLLMに読み込ませることによる、AIによるテスト作成を想定しています。
- YamlTestPilot のテンプレート YAML ファイルは[こちら](https://github.com/Masafuro/YamlTestPilot/blob/main/template.yaml)からご利用いただけます。

## 特徴
1. pythonの関数の入出力テストを所定の.yamlファイルの記述を元に実行できる。
2. この.yamlファイルはchatGPTなどのLLMによって記述されることを想定している。
3. 実行と共に結果は、resultsフォルダに格納される。

### 実行に必要なもの
1. 所定のフォルダ構造
2. test_cases内に.pyファイルと同名の.yamlファイル（テスト項目を記述したもの）
3. test_runner.py

## フォルダ構造ルール：directory rules
<pre>
.
└── project_root/
    └── program_files/
        ├── test_runner.py
        ├── example1.py
        ├── test_cases/
        │   └── example1.yaml
        └── results/
            └── r_example1.yaml
</pre>
## 使用方法 (Usage)

1. テスト対象の Python ファイル `{program_name}.py` を作成し、`program_files(任意)` フォルダに保存します。
2. テスト仕様を検討し、`{program_name}.yaml` という名前で `test_cases(固定)` フォルダにテストケースを記述した YAML ファイルを作成します。
3. `test_runner.py` を実行し、1, 2 で作成したファイルに基づいてテストを実行します。
4. テスト結果は `results(固定)` フォルダに `r_{program_name}.yaml` という名前で保存され、実行結果とテスト全体のメタ情報を含みます。

### 実行例

以下のコマンドで `test_runner.py` を実行し、テストを開始します。
正しいフォルダ構造になっていれば、.pyファイルが選択できます。エンターキーで選択して実行してください。

```bash
python test_runner.py

テスト対象の Python ファイルを選択してください: 
❯ example1.py
  test_runner.py
