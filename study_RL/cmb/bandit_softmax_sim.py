import numpy as np
import matplotlib.pyplot as plt


def softmax_probabilities(q_values, beta):
    scaled = beta * np.asarray(q_values, dtype=float)
    shifted = scaled - np.max(scaled)
    exp_values = np.exp(shifted)
    return exp_values / np.sum(exp_values)


def replay_bandit(alpha, beta, rewards, actions):
    q_values = np.zeros(2, dtype=float)
    q_history = [q_values.copy()]
    prob_history = []

    for action, reward in zip(actions, rewards):
        action_probs = softmax_probabilities(q_values, beta=beta)
        prob_history.append(action_probs)
        q_values[action] = q_values[action] + alpha * (reward - q_values[action])
        q_history.append(q_values.copy())

    return np.array(q_history), np.array(prob_history)


def simulate_bandit(trials, alpha, beta, reward_probs, seed=0):
    rng = np.random.default_rng(seed)
    action_names = ["A", "B"]
    q_values = np.zeros(2, dtype=float)

    q_history = [q_values.copy()]
    prob_history = []
    action_history = []
    reward_history = []

    for _ in range(trials):
        action_probs = softmax_probabilities(q_values, beta=beta)
        action = rng.choice(len(action_names), p=action_probs)
        reward = rng.binomial(n=1, p=reward_probs[action])

        q_values[action] = q_values[action] + alpha * (reward - q_values[action])

        prob_history.append(action_probs)
        action_history.append(action)
        reward_history.append(reward)
        q_history.append(q_values.copy())

    return {
        "action_names": action_names,
        "q_history": np.array(q_history),
        "prob_history": np.array(prob_history),
        "action_history": np.array(action_history),
        "reward_history": np.array(reward_history),
    }


def negative_log_likelihood(alpha, beta, rewards, actions):
    _, prob_history = replay_bandit(alpha=alpha, beta=beta, rewards=rewards, actions=actions)
    chosen_probs = prob_history[np.arange(len(actions)), actions]
    chosen_probs = np.clip(chosen_probs, 1e-12, 1.0)
    return -np.sum(np.log(chosen_probs))


def fit_parameters_mle(rewards, actions):
    alpha_grid = np.linspace(0.05, 0.95, 91)
    beta_grid = np.linspace(0.1, 6.0, 119)

    best_alpha = alpha_grid[0]
    best_beta = beta_grid[0]
    best_nll = np.inf

    for alpha in alpha_grid:
        for beta in beta_grid:
            nll = negative_log_likelihood(alpha=alpha, beta=beta, rewards=rewards, actions=actions)
            if nll < best_nll:
                best_nll = nll
                best_alpha = alpha
                best_beta = beta

    return best_alpha, best_beta, best_nll


def main():
    trials = 100
    alpha = 0.3
    beta = 2.0
    reward_probs = np.array([0.7, 0.3], dtype=float)

    result = simulate_bandit(
        trials=trials,
        alpha=alpha,
        beta=beta,
        reward_probs=reward_probs,
        seed=0,
    )

    time = np.arange(1, trials + 1)
    q_history = result["q_history"]
    prob_history = result["prob_history"]
    action_history = result["action_history"]
    reward_history = result["reward_history"]
    est_alpha, est_beta, _ = fit_parameters_mle(rewards=reward_history, actions=action_history)
    est_q_history, est_prob_history = replay_bandit(
        alpha=est_alpha,
        beta=est_beta,
        rewards=reward_history,
        actions=action_history,
    )

    fig, axes = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

    axes[0].plot(time, q_history[:-1, 0], label=r"$Q_t(A)$ true", linewidth=2)
    axes[0].plot(time, q_history[:-1, 1], label=r"$Q_t(B)$ true", linewidth=2)
    axes[0].plot(time, est_q_history[:-1, 0], "--", label=r"$Q_t(A)$ MLE", linewidth=2)
    axes[0].plot(time, est_q_history[:-1, 1], "--", label=r"$Q_t(B)$ MLE", linewidth=2)
    axes[0].axhline(reward_probs[0], color="tab:blue", linestyle="--", alpha=0.5)
    axes[0].axhline(reward_probs[1], color="tab:orange", linestyle="--", alpha=0.5)
    axes[0].set_ylabel("Q value")
    axes[0].set_title(
        rf"Softmax Bandit Learning "
        rf"(true: $\alpha={alpha}, \beta={beta}$; "
        rf"MLE: $\hat{{\alpha}}={est_alpha:.2f}, \hat{{\beta}}={est_beta:.2f}$)"
    )
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()

    axes[1].plot(time, prob_history[:, 0], label=r"$P(a_t=A)$ true", linewidth=2)
    axes[1].plot(time, prob_history[:, 1], label=r"$P(a_t=B)$ true", linewidth=2)
    axes[1].plot(time, est_prob_history[:, 0], "--", label=r"$P(a_t=A)$ MLE", linewidth=2)
    axes[1].plot(time, est_prob_history[:, 1], "--", label=r"$P(a_t=B)$ MLE", linewidth=2)
    axes[1].set_ylabel("choice probability")
    axes[1].set_ylim(0.0, 1.0)
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()

    axes[2].step(time, action_history == 0, where="mid", label="action A", linewidth=1.5)
    axes[2].scatter(time, reward_history, label=r"reward $r_t$", s=18, color="tab:green")
    axes[2].set_xlabel("trial t")
    axes[2].set_ylabel("action / reward")
    axes[2].set_yticks([0, 1], labels=["B or 0", "A or 1"])
    axes[2].grid(True, alpha=0.3)
    axes[2].legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
