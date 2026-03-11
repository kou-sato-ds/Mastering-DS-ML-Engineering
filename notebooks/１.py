import numpy as np
import matplotlib.pyplot as plt

# 乱数シードを固定（再現性の確保）
np.random.seed(42)

# 1. データの生成
data = np.random.normal(50, 10, 1000)

# 2. 統計量の算出
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

# 3. 外れ値の境界線を計算 (1.5倍IQRルール)
lower_bridge = q1 - 1.5 * iqr
upper_bridge = q3 + 1.5 * iqr

# 4. 外れ値を特定
outliers = data[(data < lower_bridge) | (data > upper_bridge)]

# --- 統計レポートの出力 ---
print(f"--- 12日目：統計要約レポート ---")
print(f"平均値: {np.mean(data):.2f} / 中央値: {np.median(data):.2f}")
print(f"第1四分位数 (Q1): {q1:.2f} / 第3四分位数 (Q3): {q3:.2f}")
print(f"四分位範囲 (IQR): {iqr:.2f}")
print(f"下限境界線: {lower_bridge:.2f} / 上限境界線: {upper_bridge:.2f}")
print(f"検知された外れ値の数: {len(outliers)}")

# 5. 可視化（ヒストグラムと箱ひげ図を並べて表示）
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# ヒストグラム
ax1.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax1.axvline(np.mean(data), color='red', linestyle='dashed', label='Mean')
ax1.set_title('Data Distribution')
ax1.legend()

# 箱ひげ図（境界線を赤線で表示）
ax2.boxplot(data, vert=False, patch_artist=True)
ax2.axvline(lower_bridge, color='red', linestyle='--', label='Lower Bound')
ax2.axvline(upper_bridge, color='red', linestyle='--', label='Upper Bound')
ax2.set_title('Outlier Detection (1.5xIQR Rule)')
ax2.legend()

plt.tight_layout()
plt.show()