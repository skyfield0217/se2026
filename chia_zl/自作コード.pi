import statistics

def calculate_stats():
    print("好きな数字をスペース区切りで入力してください。")
    print("（例: 10 20 5 30 15）")
    
    user_input = input("数字を入力 > ")
    
    try:
        # 入力された文字をスペースで分割し、数値（小数）のリストに変換する
        numbers = [float(x) for x in user_input.split()]
        
        # リストが空の場合は終了
        if not numbers:
            print("数字が入力されませんでした。")
            return
            
        # 平均値と中央値を計算
        mean_value = statistics.mean(numbers)
        median_value = statistics.median(numbers)
        
        # 結果を表示
        print("\n=== 計算結果 ===")
        print(f"入力されたデータ: {numbers}")
        print(f"データの個数: {len(numbers)}個")
        print(f"平均値: {mean_value}")
        print(f"中央値: {median_value}")
        print("================")
        
    except ValueError:
        print("【エラー】数字以外の文字が含まれているか、形式が間違っています。")

if __name__ == "__main__":
    calculate_stats()
