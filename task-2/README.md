# Statistical Engineering & Simulation Project

## 📌 Project Overview

This project implements a pure Python statistical engine from scratch. It analyzes raw numerical data and performs Monte Carlo simulations to demonstrate the Law of Large Numbers (LLN).

---

## 🧠 Features

- Mean, Median, Mode (supports multimodal distributions)
- Variance (Sample & Population)
- Standard Deviation
- Outlier Detection
- Monte Carlo Simulation for server crash probability

---

## 📊 Mathematical Logic

### Variance

- Population Variance:
  sum((x - mean)^2) / n
- Sample Variance:
  sum((x - mean)^2) / (n - 1)

(Bessel’s correction is used to adjust bias in sample data.)

### Median

- Odd length → middle value
- Even length → average of two middle values

---

## 📈 Law of Large Numbers (LLN) Interpretation

The Monte Carlo simulation demonstrates the Law of Large Numbers.

When the number of simulated days is small (e.g., 30 days), the observed crash probability fluctuates significantly and may differ greatly from the true probability of 0.045.

As the number of days increases (e.g., 10,000 days), the simulated probability converges toward the true probability.

### ⚠️ Business Risk

It is dangerous for the startup to rely on a small dataset (e.g., 30 days) to estimate yearly maintenance costs. Small samples are highly variable and may lead to:

- Underestimating failure rates → insufficient budget
- Overestimating failure rates → wasted resources

A larger dataset provides more reliable estimates and reduces decision risk.

## ⚙️ Setup Instructions

```bash
git clone <your-repo-link>
cd statistical_engine
python main.py
```
