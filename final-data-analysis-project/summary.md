# Hotel Booking Cancellation Analysis

## Project Documentation

## 1. Project Overview

This project analyzes hotel booking data to understand cancellation behavior and generate actionable business recommendations.

### Main objectives

- Identify high-risk cancellation segments
- Measure key operational and behavioral drivers
- Validate findings statistically
- Convert insights into policy recommendations

---

## 2. Dataset and Preparation

## 2.1 Dataset characteristics

The dataset includes:

- **Numerical features**: `lead_time`, `adr`, nights, requests
- **Categorical features**: `hotel`, `market_segment`, `deposit_type`, `company`
- **Temporal features**: arrival date fields
- **Missing values** with potential business meaning

## 2.2 Data governance

Personally identifiable information was excluded from analysis:

- `name`
- `email`
- `phone-number`
- `credit_card`

---

## 3. Methodology

## 3.1 Baseline profiling

Initial cross-tab and pivot analysis established cancellation baselines.

**Output highlights**

- Overall cancellation rate: **37.0%**
- City Hotel cancellation: **41.7%**
- Resort Hotel cancellation: **27.8%**
- Unadjusted gap: **+13.97 percentage points**

## 3.2 Quantile-based risk analysis

`lead_time` was binned into quantiles (Q1–Q4) to detect non-linear risk behavior.

**Output highlights**

- Q1 cancellation: **14.6%**
- Q4 cancellation: **55.4%**

## 3.3 Interaction segmentation

Three-way segmentation was performed on:

`hotel × market_segment × lead_time_quantile`

**Output highlight**

- **City Hotel + Groups + Q4 lead time = 82.9% cancellation**

## 3.4 Behavioral proxy analysis

`total_of_special_requests` was analyzed as engagement signal.

**Output highlights**

- 0 requests: **47.7%** cancellation
- 2–5 requests: **16.8%** cancellation

## 3.5 Outlier value contribution

Instead of removing high-end values, economic contribution of the top tail was measured.

**Output highlight**

- Top 5% bookings contribute **19.8%** of total revenue proxy

## 3.6 Missingness as information

Missing values were treated as potential signal, not only data-quality issues.

**Output highlights**

- `company` missing: **38.2%** cancellation
- `company` present: **17.5%** cancellation

## 3.7 Statistical validation

Results were validated with inferential methods:

- Bootstrap confidence intervals
- Permutation testing

**Output highlights**

- Unadjusted hotel gap CI: **[13.4, 14.5] pp**
- Risk ratio (City vs Resort): **1.50**, CI **[1.48, 1.53]**

## 3.8 Confounder adjustment

Mix-standardization was used with matched `lead_time + deposit` composition across hotel types.

**Output highlights**

- Standardized City cancellation: **38.7%**
- Standardized Resort cancellation: **34.0%**
- Adjusted gap: **4.71 pp**

---

## 4. Key Findings

1. Cancellation risk strongly increases with lead time (**14.6% → 55.4%**).
2. Risk is highly interaction-dependent; extreme segment reaches **82.9%**.
3. Customer engagement is associated with lower cancellation (**47.7% → 16.8%**).
4. Raw hotel-type differences are partially confounded (**13.97 pp raw vs 4.71 pp adjusted**).
5. Outliers and missingness contain business signal and should be modeled intentionally.

---

## 5. Business Recommendations

- Apply stricter deposit/prepayment for high-risk long-lead group segments.
- Increase pre-arrival engagement to grow special-request behavior.
- Report both unadjusted and adjusted cancellation metrics in dashboards.
- Treat top-value bookings as VIP segment for retention strategy.
- Include missingness flags (e.g., `company` NA) in cancellation-risk scoring.

---

## 6. Limitations

- Findings are observational and indicate association, not strict causality.
- Policy impact should be monitored with controlled rollouts where possible.
- Temporal drift checks are needed for long-term reliability.

---

## 7. Next Steps

- Build calibrated cancellation prediction model
- Add seasonality-aware validation
- Simulate policy impacts by segment
- Integrate model outputs into operational decision workflows

---

## 8. Techniques Used (Checklist)

- Cross-tabulation and pivot analysis
- Quantile binning and cohort analysis
- Multi-dimensional interaction segmentation
- Outlier contribution analysis
- Missingness pattern analysis
- Bootstrap confidence intervals
- Permutation testing
- Mix-standardized adjustment for confounder control
- Business translation of statistical outputs
