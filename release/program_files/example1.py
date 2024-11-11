# example1.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    # 動作確認用の引数を変数として宣言
    x1, y1 = 4, -100 # add 関数用のテスト引数

    ans = add(x1,y1)
    print(f"add{x1},{y1}>>>{ans}")
    ans = subtract(x1,y1)
    print(f"sub{x1},{y1}>>>{ans}")

if __name__ == "__main__":
    main()
