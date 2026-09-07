# Executive Summary: PowerCo SME Customer Churn Analysis

## **Situation**
PowerCo, a major utility company supplying gas and electricity to Small and Medium Enterprises (SMEs), was experiencing high levels of customer churn. With increased market competition and pricing variability following market deregulation, PowerCo sought **BCG X’s support** to understand customer churn behavior and design a targeted retention strategy.

---

## **Complication**
PowerCo's executive leadership assumed that **price sensitivity** was the primary driver of churn. However, PowerCo lacked empirical data to confirm this hypothesis. Without solid data, implementing blanket price cuts across all SME clients would severely damage profit margins without guaranteeing customer retention.

---

## **Key Business Questions**
1. To what extent is **price sensitivity** influencing churn at PowerCo?
2. Are there other non-price factors that better explain customer departure behavior?
3. Can we build a predictive machine learning model to identify high-risk churn customers before their contracts expire?

---

## **Findings & Key Answers**
Using a **Random Forest Classifier** trained on a curated dataset of **14,606 SME customers** with **63 predictive features**, we found:

* **Price sensitivity is influential, but NOT the primary driver of churn.**
* **Major non-price churn predictors:**
  1. **Customer Tenure (`num_years_antig`):** Shorter tenure / recent onboarding correlates with significantly higher churn risk.
  2. **Net Margin (`margin_net_pow` & `margin_gross_pow_ele`):** Financial margin profile strongly indicates account stability.
  3. **Usage Volatility & Consumption (`cons_12m`):** Fluctuations in electricity consumption relative to forecasts.

---

## **Model Performance & Improvements**

### **Baseline Model (Default 0.50 Threshold, Standard Class Weights)**
* **Accuracy:** 91.1%
* **Precision:** 81.0%
* **Recall:** 5.10% *(Missed 95% of actual churners due to severe 90:10 class imbalance)*
* **F1-Score:** 0.0962
* **ROC-AUC Score:** 0.67

### **Improved Model (Class-Weighted & Threshold Tuned @ 0.10 Threshold)**
* **Accuracy:** 63.6% - 71.5%
* **Recall:** **63.0% – 73.0%** *(Up from 5.1% — catches up to 73% of all churned customers!)*
* **Precision:** 14.6% - 16.5%
* **ROC-AUC Score:** 0.69
* **ID Column & Low-Variance Features:** Removed to eliminate noise and overfitting.

---

## **Proposed Solution & Business Recommendations**
Deploy the churn prediction model into PowerCo's **CRM System** to enable:

1. **Targeted Interventions:** Automatically trigger custom **20% retention discount offers** exclusively for high-risk customers with high lifetime value.
2. **Proactive Risk Scoring:** Score all SME accounts monthly to catch churn signals 1–3 months before contract renewal dates.
3. **Avoid Blanket Price Cuts:** Focus promotional discounts only on high-churn-risk clients, saving millions in wasted discount costs.

---

## **Potential Business Impact**
* **Predict Churn Risk:** Detect up to **73% of churn-prone accounts** prior to departure.
* **Expected Churn Reduction:** **25% – 30% reduction** in customer churn.
* **Revenue Recovery:** Recovery of millions of dollars in lost annual recurring revenue.
