import statistics

def calculate_stats_with_table():
    print("好きな数字をスペース区切りで入力してください。")
    print("（例: 10 20 5 30 15）")
    
    user_input = input("数字を入力 > ")
    
    try:
        # 入力された文字をスペースで分割し、数値のリストに変換
        numbers = [float(x) for x in user_input.split()]
        
        if not numbers:
            print("数字が入力されませんでした。")
            return
            
        # 平均値と中央値を計算
        mean_value = statistics.mean(numbers)
        median_value = statistics.median(numbers)
        count = len(numbers)
        
        # 綺麗に表示するために数値を文字列に変換（平均値は小数第2位までに丸める例）
        count_str = f"{count}個"
        mean_str = f"{mean_value:.2f}"
        median_str = f"{median_value}"
        
        # 表形式で出力
        print("\n【 計算結果 】")
        print("入力されたデータ:", numbers)
        print("+" + "-"*14 + "+" + "-"*14 + "+")
        print("| 項目           | 値             |")
        print("+" + "-"*14 + "+" + "-"*14 + "+")
        # 左揃え（<）を使って縦の線を合わせる
        print(f"| データの個数   | {count_str:<12} |")
        print(f"| 平均値         | {mean_str:<12} |")
        print(f"| 中央値         | {median_str:<12} |")
        print("+" + "-"*14 + "+" + "-"*14 + "+")
        
    except ValueError:
        print("【エラー】数字以外の文字が含まれているか、形式が間違っています。")

if __name__ == "__main__":
    calculate_stats_with_table()
