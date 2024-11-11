def test_error_handling(expected_error_type, func, *args):
    """
    指定した関数funcを実行し、expected_error_typeが発生するか確認するテスト関数
    """
    try:
        result = func(*args)
        # エラーが発生しない場合は失敗
        print(f"Test Fail: Expected {expected_error_type.__name__}, but no error occurred. Result = {result}")
    except Exception as e:
        # 期待されるエラー型と一致するか確認
        if isinstance(e, expected_error_type):
            print(f"Test Success: Caught expected error of type {expected_error_type.__name__}. Error message: {e}")
        else:
            print(f"Test Fail: Expected {expected_error_type.__name__}, but caught {type(e).__name__}. Error message: {e}")

# 例としてTypeErrorを発生させる関数
def cause_type_error():
    return "string" + 10  # TypeErrorを発生させる

# テスト実行
test_error_handling(TypeError, cause_type_error)
