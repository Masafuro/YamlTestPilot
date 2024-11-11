from pydantic import BaseModel, Field
from typing import List, Optional
import yaml

from pydantic import BaseModel, Field
from typing import List, Optional

# 各テストの結果情報
class TestResult(BaseModel):
    status: Optional[str] = None
    actual_return: Optional[int] = None
    execution_time_ms: Optional[int] = None

# 各テストケースのデータ
class TestData(BaseModel):
    arguments: List[int]
    expected_return: int
    exception: Optional[str] = None

# 個々のテストケース
class TestCase(BaseModel):
    case_name: str
    test_data: List[TestData]
    result: List[TestResult]  # <-- `result`に変更しました

# テストケースのグループ
class Summary(BaseModel):
    summary_name: str
    description: str
    names: List[str]
    cases: List[TestCase]

# 個々の関数ごとのテスト
class TestCaseEntry(BaseModel):
    function_name: str
    function_description: str
    function_hash: Optional[str] = None
    summary: List[Summary]

# メタ情報と設定情報
class MetaInfo(BaseModel):
    name: str
    description: str
    created_by: str
    last_run: Optional[str] = None

class Settings(BaseModel):
    root_path: str
    module_file: str
    retries: int
    timeout: int

# 全体のデータモデル
class RootModel(BaseModel):
    meta: MetaInfo
    settings: Settings
    test_cases: List[TestCaseEntry]



if __name__ == "__main__":
# YAMLデータの読み込みとモデル化

    with open('sample2.yaml', 'r') as file:
        yaml_data = yaml.safe_load(file)

    root_model = RootModel(**yaml_data)

    # resultフィールドにアクセス
    result = root_model.test_cases[0].summary[0].cases[0].result[0]
    print(result.status)         # None（未実行）
    print(result.actual_return)   # None（未実行）

