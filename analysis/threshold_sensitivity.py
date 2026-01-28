import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# If you already generate 'data' in another script,
# you can either:
# 1) copy the same data generation block here (recommended for independence)
# 2) or load from a CSV if you saved it
# =========================================================

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

data["last_day"] = data["first_day"] + np.random.randint(1, 90, size=n_users)

# -----------------------------
# 2. Consistency metrics
# -----------------------------
data["activity_span"] = data["last_day"] - data["first_day"] + 1
data["consistency_score"] = data["active_days"] / data["activity_span"]

# Reuse behavioral diversity idea (simple simulation)
data["behavioral_diversity"] = np.random.randint(1, 4, size=n_users)

# -----------------------------
# 3. Threshold sensitivity
# -----------------------------
# Focus on users with sufficient diversity (same as README)
subset = data[data["behavioral_diversity"] >= 2].copy()

thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

results = []
for t in thresholds:
    # define Full Access under this threshold
    subset["full_access_t"] = (subset["consistency_score"] >= t).astype(int)

    full_rate = subset["full_access_t"].mean()
    n_full = int(subset["full_access_t"].sum())
    n_total = int(len(subset))

    results.append({
        "threshold": t,
        "full_access_rate": full_rate,
        "n_full_access": n_full,
        "n_total": n_total
    })

res = pd.DataFrame(results)

print("\nThreshold sensitivity results (behavioral_diversity >= 2):")
print(res.to_string(index=False))

# -----------------------------
# 4. Visualization: threshold vs Full Access rate
# -----------------------------
plt.figure()
plt.plot(res["threshold"], res["full_access_rate"], marker="o")
plt.title("Threshold Sensitivity: Consistency Threshold vs Full Access Rate")
plt.xlabel("Consistency threshold")
plt.ylabel("Full Access rate (within behavioral_diversity >= 2)")
plt.ylim(0, 1)
plt.show()

# -----------------------------
# 5. Optional: bucketization to make 0.5 vs 0.7 intuitive
# -----------------------------
bins = [-np.inf, 0.3, 0.6, np.inf]
labels = ["<0.3", "0.3-0.6", ">0.6"]

subset["consistency_bucket"] = pd.cut(subset["consistency_score"], bins=bins, labels=labels)

bucket_summary = subset.groupby("consistency_bucket")["consistency_score"].agg(
    count="count",
    mean="mean",
)

# Under a chosen threshold (e.g., 0.5), show bucket-wise Full Access rate
chosen_t = 0.5
subset["full_access_chosen"] = (subset["consistency_score"] >= chosen_t).astype(int)
bucket_rates = subset.groupby("consistency_bucket")["full_access_chosen"].mean()

print(f"\nBucket summary (behavioral_diversity >= 2), chosen threshold = {chosen_t}:")
print(bucket_summary)
print("\nFull Access rate by bucket (chosen threshold):")
print(bucket_rates)

plt.figure()
bucket_rates.plot(kind="bar")
plt.title(f"Full Access Rate by Consistency Bucket (threshold={chosen_t})")
plt.xlabel("Consistency bucket")
plt.ylabel("Full Access rate")
plt.ylim(0, 1)
plt.show()
