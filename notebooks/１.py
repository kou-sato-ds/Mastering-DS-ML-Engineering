import numpy as np
import matplotlib.pyplot as plt

# 乱数シードを固定（再現性の確保：実務の鉄則）
np.random.seed(42)

# 1. データの生成
mean_val = 50
std_val = 10
data = np.random.normal(mean_val, std_val, 1000)

# 2. 可視化の強化
plt.figure(figsize=(10, 6)) # グラフサイズを指定
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# 平均値（赤）と中央値（緑）をラインで表示
plt.axvline(np.mean(data), color='red', linestyle='dashed', linewidth=2, label=f'Mean: {np.mean(data):.2f}')
plt.axvline(np.median(data), color='green', linestyle='dotted', linewidth=2, label=f'Median: {np.median(data):.2f}')

plt.title('Data Distribution & Central Tendency', fontsize=14)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', alpha=0.3) # グリッド線を追加して見やすく
plt.show()

# 3. 統計量の出力
print(f"平均値 (Mean): {np.mean(data):.2f}")
print(f"中央値 (Median): {np.median(data):.2f}")
print(f"標準偏差 (Std Dev): {np.std(data):.2f}")