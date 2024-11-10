def add(a, b):
    """
    Adds two numbers and returns the sum.
    
    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.
    
    Returns:
    - int or float: The sum of a and b.
    """
    return a + b

# 使用例
if __name__ == "__main__":
    # テストデータを使用した実行例
    print("Addition with Positive Integers:", add(2, 3))  # 期待される出力: 5
    print("Addition with Negative Integers:", add(-2, -3))  # 期待される出力: -5
    print("Addition with Zero:", add(0, 5))  # 期待される出力: 5
