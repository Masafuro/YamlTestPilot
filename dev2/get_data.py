def get_status(data, function_name, case_name):
    """
    data内で指定したfunction_nameとcase_nameに対応する
    __result__内のstatusにアクセスする関数

    Parameters:
    - data (list): YAMLファイルを読み込んだデータ
    - function_name (str): 対象の関数名
    - case_name (str): 対象のテストケース名

    Returns:
    - statusの値
    """
    # test_casesリストを順に探索
    for function in data['test_cases']:
        # 指定したfunction_nameと一致するものを検索
        if function.get('function_name') == function_name:
            # casesリストを順に探索
            for case in function.get('cases', []):
                # 指定したcase_nameと一致するものを検索
                if case.get('case_name') == case_name:
                    # __result__内のstatusを返す
                    return case['__result'].get('status')
    return None  # 見つからなかった場合

# 使用例
# 例としてYAMLデータがdataに読み込まれていると仮定します
status = get_status(data, "add", "Addition with Positive Integers")
print("Status:", status)
