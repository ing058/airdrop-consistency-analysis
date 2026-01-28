import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Simulated data generation
# -----------------------------
np.random.seed(42)
n_users = 1000

data = pd.DataFrame({
    "user_id": range(1, n_users + 1),
    "tx_count": np.random.poisson(lam=50, size=n_users),
    "active_days": np.random.randint(1, 90, size=n_users),
    "first_day": np.random.randint(1, 30, size=n_users),
})

# last activity day (ensure last_day >= first_day)
data["last_day"] = data["first_day"] + np.random.randint(1, 90, size=n_users)

# -----------------------------
# 2. Consistency metrics
# -----------------------------
data["activity_span"] = data["last_day"] - data["first_day"] + 1
data["consistency_score"] = data["active_days"] / data["activity_span"]

# Behavioral diversity (reuse idea from previous project)
data["behavioral_diversity"] = np.random.randint(1, 4, size=n_users)

# Full Access condition (hidden rule)
data["full_access"] = (
    (data["behavioral_diversity"] >= 2) &
    (data["consistency_score"] >= 0.3)
).astype(int)

print(data.head())
print("\nFull access distribution:")
print(data["full_access"].value_counts())

# -----------------------------
# 3. Group comparison
# -----------------------------
summary = data.groupby("full_access")[[
    "tx_count",
    "active_days",
    "activity_span",
    "consistency_score"
]].mean()

print("\nAverage comparison:")
print(summary)

# -----------------------------
# 4. Visualization
# -----------------------------
plt.figure()
data.boxplot(column="consistency_score", by="full_access")
plt.title("Consistency Score by Full Access")
plt.suptitle("")
plt.xlabel("Full Access (0 = No, 1 = Yes)")
plt.ylabel("Consistency Score")
plt.show()

plt.figure()
data.boxplot(column="tx_count", by="full_access")
plt.title("Transaction Count by Full Access")
plt.suptitle("")
plt.xlabel("Full Access (0 = No, 1 = Yes)")
plt.ylabel("Transaction Count")
plt.show()
