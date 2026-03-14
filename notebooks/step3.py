# 1. 昨日の部品を呼び出す（モジュール化の基本）
# ※ファイル名が数字で始まる場合、通常のimportでエラーが出る時は 
# import importlib; outlier_mod = importlib.import_module("2") 
# のような手法を使いますが、まずはこのシンプルな形で試しましょう。
from step2 import handle_outliers
import numpy as np

def main():
    print("--- 14日目：モジュール呼び出しによる実戦演習 ---")

    # 1. テストデータの準備（実務でのセンサーデータ等を想定）
    np.random.seed(13)
    raw_data = np.random.normal(100, 20, 50)
    # 外れ値を注入
    raw_data = np.append(raw_data, [250, -50])

    # 2. 外部モジュールの関数を実行
    strategy = 'remove'
    cleaned_data, bounds = handle_outliers(raw_data, strategy=strategy)

    # 3. ビジネスインパクトの可視化
    print(f"採用戦略: {strategy}")
    print(f"計算境界: {bounds[0]:.2f} ～ {bounds[1]:.2f}")
    print(f"外れ値除去数: {len(raw_data) - len(cleaned_data)} 件")
    print(f"平均値の変化: {np.mean(raw_data):.2f} -> {np.mean(cleaned_data):.2f}")

    print("\n[ビジネス価値への翻訳]")
    print("異常値を除去したことで、予測モデルの平均誤差を抑え、")
    print("より精度の高い在庫発注アラートが可能になります。")

if __name__ == "__main__":
    main()