import random

def simulate_crashes(days, crash_probability=0.045):
    crashes = 0

    for _ in range(days):
        if random.random() < crash_probability:
            crashes += 1

    simulated_probability = crashes / days
    return crashes, simulated_probability