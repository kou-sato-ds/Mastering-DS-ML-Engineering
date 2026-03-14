import numpy as np
import pandas as pd

def handle_outliers(data, strategy='clip'):
    """
    1.5xIQRルールに基づき外れ値を処理する関数
    
    Args:
        data (np.array): 処理対象の数値データ
        strategy (str): 'remove' (削除), 'clip' (境界値で埋める)
        
    Returns:
        tuple: (処理済みデータ, (下限境界, 上限境界))
    """
    # 四分位数とIQRの算出
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    
    # 境界線の定義
    lower_bridge = q1 - 1.5 * iqr
    upper_bridge = q3 + 1.5 * iqr
    
    if strategy == 'remove':
        # 範囲内のデータのみを抽出して削除
        cleaned_data = data[(data >= lower_bridge) & (data <= upper_bridge)]
    elif strategy == 'clip':
        # 範囲外を上限・下限値に丸める（実務で多用される「クリッピング」）
        cleaned_data = np.clip(data, lower_bridge, upper_bridge)
    else:
        raise ValueError("strategy must be 'remove' or 'clip'")
    
    return cleaned_data, (lower_bridge, upper_bridge)

# --- テスト実行（実務を想定した検証） ---
if __name__ == "__main__":
    np.random.seed(42)
    # 平均50, 標準偏差10のデータを100個生成し、意図的に外れ値を2つ追加
    base_data = np.random.normal(50, 10, 100)
    test_data = np.append(base_data, [100, -10])

    # 関数を呼び出して処理
    strategy = 'clip'
    cleaned, (lb, ub) = handle_outliers(test_data, strategy=strategy)

    # 結果の可視化とレポート
    print(f"--- 13日目：データクレンジング完了報告 ---")
    print(f"採用戦略: {strategy}")
    print(f"計算境界: 下限 {lb:.2f} / 上限 {ub:.2f}")
    print(f"最大値の推移: {test_data.max()} -> {cleaned.max():.2f}")
    print(f"最小値の推移: {test_data.min()} -> {cleaned.min():.2f}")