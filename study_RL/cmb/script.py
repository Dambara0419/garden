import matplotlib.pyplot as plt

def simulate_rescorla_wagner(trials, alpha, reward, initial_v=0.0):
    """
    Rescorla-Wagnerモデルの学習過程をシミュレーションする関数
    """
    v = initial_v
    v_history = [v]

    for _ in range(trials):
        # 1. 予測誤差の計算 (実際の報酬 - 現在の予測)
        prediction_error = reward - v
        
        # 2. 価値の更新 (現在の予測 + 学習率 * 予測誤差)
        v = v + alpha * prediction_error
        
        v_history.append(v)

    return v_history

# --- パラメータの設定 ---
trials_per_phase = 20  # 各フェーズの試行回数
learning_rate = 0.3    # 学習率 (α)

# --- フェーズ1: 獲得 (Acquisition) ---
# 報酬が与えられる状態 (R=10)
reward_acquisition = 10.0
v_acquisition = simulate_rescorla_wagner(
    trials=trials_per_phase, 
    alpha=learning_rate, 
    reward=reward_acquisition, 
    initial_v=0.0
)

# --- フェーズ2: 消去 (Extinction) ---
# 報酬が与えられなくなる状態 (R=0)
reward_extinction = 0.0
# 獲得フェーズの最終的な価値を初期値として引き継ぐ
v_extinction = simulate_rescorla_wagner(
    trials=trials_per_phase, 
    alpha=learning_rate, 
    reward=reward_extinction, 
    initial_v=v_acquisition[-1]
)

# --- グラフの描画 ---
plt.figure(figsize=(10, 5))

# 獲得フェーズのプロット
plt.plot(range(trials_per_phase + 1), v_acquisition, 
         label='Acquisition (Reward=10)', marker='o', color='blue')

# 消去フェーズのプロット (X軸をずらして連続させる)
extinction_x = range(trials_per_phase, trials_per_phase * 2 + 1)
plt.plot(extinction_x, v_extinction, 
         label='Extinction (Reward=0)', marker='x', color='red')

plt.title('Rescorla-Wagner Model Learning Process')
plt.xlabel('Trials')
plt.ylabel('Predicted Value (V)')
plt.axhline(y=10, color='gray', linestyle='--', alpha=0.5) # 最大予測値のライン
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.5)  # 最小予測値のライン
plt.legend()
plt.grid(True)
plt.show()