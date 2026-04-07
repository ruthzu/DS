from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes
import random
random.seed(42)

data = [2, 4, 4, 4, 5, 5, 7, 9]
days_list = [30, 365, 10000]

engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Variance (Sample):", engine.get_variance())
print("Variance (Population):", engine.get_variance(is_sample=False))
print("Standard Deviation:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

for days in days_list:
    crashes, prob = simulate_crashes(days)
    print(f"\nDays: {days}")
    print(f"Total Crashes: {crashes}")
    print(f"Simulated Probability: {prob:.4f}")