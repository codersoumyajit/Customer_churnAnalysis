import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)

# 1. Load Cleaned Dataset
print("Loading dataset...")
df = pd.read_csv('cleaned2_dataset.csv')

# 2. Separate Features and Target
X = df.drop(columns=['churn'])
y = df['churn']

# Keep numeric features
X_numeric = X.select_dtypes(include=['number'])

# 3. Train-Test Split (70/30)
X_train, X_test, y_train, y_test = train_test_split(
    X_numeric, y, test_size=0.3, random_state=0
)

# 4. Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train Improved Random Forest Model (Balanced Class Weights)
print("Training Random Forest Classifier with class_weight='balanced'...")
rfc_improved = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=0
)
rfc_improved.fit(X_train_scaled, y_train)

# 6. Predict Probabilities
churn_proba = rfc_improved.predict_proba(X_test_scaled)[:, 1]

# 7. Apply Tuned Decision Threshold (0.10 for ~63% Recall)
OPTIMAL_THRESHOLD = 0.10
y_pred_tuned = (churn_proba >= OPTIMAL_THRESHOLD).astype(int)

# 8. Calculate Metrics
acc = accuracy_score(y_test, y_pred_tuned)
prec = precision_score(y_test, y_pred_tuned)
rec = recall_score(y_test, y_pred_tuned)
f1 = f1_score(y_test, y_pred_tuned)
auc = roc_auc_score(y_test, churn_proba)
cm = confusion_matrix(y_test, y_pred_tuned)

print("\n==========================================")
print("     IMPROVED MODEL PERFORMANCE METRICS   ")
print("==========================================")
print(f"Classification Threshold: {OPTIMAL_THRESHOLD}")
print(f"Accuracy:                {acc:.4f} ({acc*100:.1f}%)")
print(f"Precision:               {prec:.4f} ({prec*100:.1f}%)")
print(f"Recall (Catch Rate):     {rec:.4f} ({rec*100:.1f}%) <--- [HUGE IMPROVEMENT FROM 5.1%]")
print(f"F1 Score:                {f1:.4f}")
print(f"ROC-AUC Score:           {auc:.4f}")
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(classification_report(y_test, y_pred_tuned, target_names=["No Churn", "Churned"]))

# 9. Export Updated Predictions to CSV
results_df = pd.DataFrame({
    'Customer_Index': X_test.index,
    'Churn_Probability': churn_proba,
    'Predicted_Churn_Baseline': (churn_proba >= 0.50).astype(int),
    'Predicted_Churn_Tuned': y_pred_tuned
})

results_df.to_csv('predicted_churn_improved.csv', index=False)
print("\nSaved updated predictions to 'predicted_churn_improved.csv' successfully!")
