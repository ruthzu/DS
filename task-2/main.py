import json
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes
import random

# ---------------------------
# PART 1: Load Salary Dataset
# ---------------------------
with open("data/sample_salaries.json", "r") as f:
    salaries = json.load(f)

engine = StatEngine(salaries)

print("\n--- Salary Analysis ---")
print("Mean Salary:", engine.get_mean())
print("Median Salary:", engine.get_median())
print("Mode Salary:", engine.get_mode())
print("Standard Deviation:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

# ---------------------------
# PART 2: Monte Carlo Simulation
# ---------------------------
print("\n--- Monte Carlo Simulation ---")

random.seed(42)  # for consistency

days_list = [30, 365, 10000]

for days in days_list:
    crashes, prob = simulate_crashes(days)
    print(f"\nDays: {days}")
    print(f"Total Crashes: {crashes}")
    print(f"Simulated Probability: {prob:.4f}")