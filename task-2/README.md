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

## ⚙️ Setup Instructions

```bash
git clone <your-repo-link>
cd statistical_engine
python main.py
```
