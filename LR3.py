# file: kaggle_narfu_baseline.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# === Load data ===
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
sample = pd.read_csv("sample_submission.csv")

X = train.drop(columns=["id", "smoking"])
y = train["smoking"]
X_test = test.drop(columns=["id"])

# === Train/val split ===
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# === Model ===
rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)

# === Train ===
rf.fit(X_train, y_train)

# === Validation ===
y_val_pred = rf.predict_proba(X_val)[:, 1]
roc_auc = roc_auc_score(y_val, y_val_pred)
print("Validation ROC-AUC:", roc_auc)

# === Retrain on full data ===
rf.fit(X, y)

# === Predict test ===
test_preds = rf.predict_proba(X_test)[:, 1]

# === Submission ===
submission = sample.copy()
submission["smoking"] = test_preds
submission.to_csv("submission.csv", index=False)
print("submission.csv saved")
