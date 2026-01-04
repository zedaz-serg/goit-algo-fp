import random
import matplotlib.pyplot as plt

def monte_carlo_dice(num_rolls=100000):
    sums_count = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums_count[die1 + die2] += 1
    probabilities = {s: (count / num_rolls) * 100 for s, count in sums_count.items()}
    return probabilities

def plot_results(mc_probs, analytical_probs):
    sums = list(mc_probs.keys())
    mc_values = list(mc_probs.values())
    an_values = [analytical_probs[s] for s in sums]
    plt.figure(figsize=(10, 6))
    plt.bar(sums, mc_values, alpha=0.6, label='Monte Carlo', color='blue')
    plt.plot(sums, an_values, 'ro-', label='Analytical', linewidth=2)
    plt.xlabel('Sum')
    plt.ylabel('Probability (%)')
    plt.xticks(range(2, 13))
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

num_samples = 100000
mc_results = monte_carlo_dice(num_samples)

print(f"{'Sum':<5} | {'MC (%)':<10} | {'An (%)':<10}")
print("-" * 30)
for s in range(2, 13):
    print(f"{s:<5} | {mc_results[s]:<10.2f} | {analytical_probabilities[s]:<10.2f}")

plot_results(mc_results, analytical_probabilities)