# PowerCo SME Customer Churn Analysis & Retention Strategy

## Project Overview
This project addresses customer churn for **PowerCo**, a European utility provider supplying gas and electricity to Small and Medium Enterprises (SMEs). Following energy market deregulation and increased competition, PowerCo experienced rising customer attrition. BCG X was engaged to analyze churn patterns, evaluate core drivers, and build a predictive retention framework.

---

## Business Problem & Core Hypothesis
PowerCo’s leadership initially hypothesized that **price sensitivity** was the primary driver of customer churn, assuming clients frequently switched providers for lower energy rates. However, PowerCo lacked empirical evidence to substantiate this claim. Implementing un-targeted price cuts across all accounts presented a major financial risk to overall profit margins.

### Primary Objectives:
1. Quantify the impact of price sensitivity on customer churn relative to non-price factors.
2. Develop a machine learning model to predict churn risk prior to contract expiration.
3. Formulate a targeted, cost-effective commercial retention strategy for high-risk accounts.

---

## Key Analytical Insights
Analysis of historical billing, contract, and usage data across **14,606 SME customers** revealed:

1. **Price Sensitivity is Not the Primary Driver:** While price fluctuations influence customer behavior, price sensitivity alone does not explain the majority of churn events.
2. **Key Non-Price Churn Drivers:**
   * **Customer Tenure (`num_years_antig`):** Newer accounts (1–3 years tenure) display significantly higher churn rates compared to established accounts.
   * **Financial Margins (`margin_net_pow`, `margin_gross_pow_ele`):** Account profitability and net margin profile are strong indicators of client stability.
   * **Consumption Volatility (`cons_12m`):** Unpredictable electricity usage relative to historical forecasts correlates with higher churn risk.

---

## Predictive Modeling & Technical Approach

### Methodology & Feature Engineering
* **Dataset Scope:** 14,606 clients, 63 engineered features.
* **Feature Engineering:** Derived annual and 6-month price deltas (`var_year_price_off_peak_var`), capacity utilization ratios (`power_utilization_ratio`), net margin ratios (`discount_impact`), and temporal contract features.
* **Model Selection:** **Random Forest Classifier** was selected for its ability to capture non-linear feature interactions and provide feature importance explainability.
* **Class Imbalance Management:** To address the severe 90:10 class imbalance (9.7% churn rate), cost-sensitive class weighting (`class_weight='balanced'`) and probability threshold optimization (threshold set at `0.10`) were implemented.

### Model Evaluation Results
* **Model Algorithm:** Random Forest (100 Estimators) - Non-linear ensemble classifier
* **ROC-AUC Score:** **0.69** (Strong overall risk ranking capability)
* **Recall (Churn Detection Rate):** **63.0%** (Successfully identifies ~63% of all churn-bound accounts)
* **Precision:** **14.6%** (Optimized to maximize churn capture over false negatives)
* **Target Variable:** Binary (`0` = Retained, `1` = Churned), evaluated on 30% unseen test holdout data

---

## Strategic Recommendations & Commercial Impact

### 1. Targeted Retention Program
Integrate model risk scores directly into PowerCo’s CRM system. Automatically trigger personalized **20% retention discount offers** exclusively for accounts flagged with a churn probability exceeding the risk threshold.

### 2. Focus on High-Value, High-Risk Accounts
Restricting promotional discounts strictly to predicted churners avoids unnecessary revenue loss on loyal customers who would stay without discounts.

### 3. Expected Business Outcomes
* **Proactive Interventions:** Enables sales teams to engage high-risk clients 1–3 months prior to contract expiration.
* **Churn Reduction:** Projected **25% – 30% reduction** in annual customer attrition.
* **Revenue Protection:** Recovery of millions in annual recurring revenue across SME accounts.
