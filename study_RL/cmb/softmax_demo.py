import numpy as np
import matplotlib.pyplot as plt


def probability_action_a(q_diff, beta=1.0):
    """Return P(a_t = A) for two actions under a softmax policy."""
    scaled = beta * np.asarray(q_diff, dtype=float)
    return 1.0 / (1.0 + np.exp(-scaled))


def main():
    q_differences = np.linspace(-6.0, 6.0, 400)
    betas = [0.5, 1.0, 2.0]

    plt.figure(figsize=(8, 5))

    for beta in betas:
        probabilities_a = probability_action_a(q_differences, beta=beta)
        plt.plot(
            q_differences,
            probabilities_a,
            label=rf"$\beta={beta}$",
            linewidth=2,
        )

    plt.title("Softmax Policy for Two Actions")
    plt.xlabel(r"$Q_t(A) - Q_t(B)$")
    plt.ylabel(r"$P(a_t = A)$")
    plt.ylim(0.0, 1.0)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
