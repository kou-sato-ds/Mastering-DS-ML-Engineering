import numpy as np
from scipy import stats

# 1. データの準備
data = np.array([102, 98, 105, 95, 110, 100, 97, 103, 101, 99])

def calculate_confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data) # ← mena から修正
    sem = stats.sem(data)
    
    # t分布を用いた信頼区間の算出
    interval = stats.t.interval(confidence, n-1, loc=mean, scale=sem)
    
    return mean, interval

mean, (lower, upper) = calculate_confidence_interval(data)

print(f"標本平均: {mean:.2f}")
print(f"95%信頼区間: {lower:.2f} 〜 {upper:.2f}")