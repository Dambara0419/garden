import numpy as np
import matplotlib.pyplot as plt


def simulate_learning(alpha, rewards, initial_value=0.0):
    """Simulate V_{t+1} = V_t + alpha(r_t - V_t)."""
    values = [initial_value]

    for reward in rewards:
        current_value = values[-1]
        next_value = current_value + alpha * (reward - current_value)
        values.append(next_value)

    return np.array(values)


def main():
    alpha = 0.2
    steps = 60
    reward_prob = 0.8
    rng = np.random.default_rng(0)

    # r_t is Bernoulli: it becomes 1 with probability p, otherwise 0.
    rewards = rng.binomial(n=1, p=reward_prob, size=steps)

    values = simulate_learning(alpha=alpha, rewards=rewards, initial_value=0.0)
    time = np.arange(steps)

    plt.figure(figsize=(10, 5))
    plt.plot(time, rewards, label="reward $r_t$", linestyle="--", color="tab:orange")
    plt.axhline(reward_prob, label="probability $p$", linewidth=2, color="tab:green")
    plt.plot(time, values[:-1], label="estimate $V_t$", linewidth=2, color="tab:blue")
    plt.scatter(time, values[1:], s=18, color="tab:blue", alpha=0.7)

    plt.title(r"Learning Process: $V_{t+1} = V_t + \alpha(r_t - V_t)$")
    plt.xlabel("time step t")
    plt.ylabel("value")
    plt.ylim(-0.05, 1.05)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
