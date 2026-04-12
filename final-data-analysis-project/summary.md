# Hotel Booking Analysis Summary

## Dataset Suitability

This dataset is well-suited for advanced techniques. It has a mix of categorical and numeric fields, time components (arrival date parts), and meaningful missingness patterns. It also includes PII columns (name, email, phone-number, credit_card), which were excluded from analysis for privacy.

## Key Insights (Level 4-5)

1. **Cancellation risk is strongly tied to lead time and segment.** The overall cancellation rate is **37.0%**, but it rises from **14.6% in Q1 lead-time** to **55.4% in Q4**. In a multi-dimensional slice, **City Hotel + Groups + long lead time (Q4)** reaches **82.9%** cancellation, suggesting high-risk segments that should face stricter policies or upfront deposits.

2. **Engagement signals reduce churn.** Bookings with **0 special requests** cancel at **47.7%**, while those with **2-5 requests** cancel at **16.8%**. This indicates that proactive engagement or upsell interactions can materially reduce cancellations.

3. **Hotel type differences are partly mix-driven, not purely causal.** Unadjusted cancellation is **41.7% (City)** vs **27.8% (Resort)**, a **+13.97 pp** gap (bootstrap CI **[13.4, 14.5] pp**, risk ratio **1.50**, CI **[1.48, 1.53]**). After standardizing to the same **lead-time + deposit mix**, the gap shrinks to **4.71 pp** (**38.7% vs 34.0%**), implying that much of the observed gap is driven by booking-mix differences rather than hotel type alone.

4. **Outliers are economically meaningful.** The top **5%** of bookings by revenue proxy contribute about **19.8%** of total revenue proxy, indicating a VIP segment worthy of specialized retention and service strategies rather than removal as noise.

5. **Missingness is informative, not random.** When **company** is missing, cancellations are **38.2%**, but when company is present, cancellations drop to **17.5%**. Missing corporate affiliation appears to signal more volatile leisure traffic.

## Techniques Used

- Cross-tabulation and pivot analysis
- Multi-dimensional segmentation (3-way interaction)
- Percentile analysis
- Cohort/time analysis
- Outlier investigation
- Derived ratios (revenue per guest)
- Missing-data pattern analysis
- Statistical validation (permutation test, bootstrap CI)
- Mix-standardized (adjusted) rates for confounder control
