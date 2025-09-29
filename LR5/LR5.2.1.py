import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("E:/IT/AI/3/LR5/mtcars.csv")

# Convert categorical variables
df["cyl"] = df["cyl"].astype("category")
df["am"] = df["am"].astype("category")

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
colors = {0: "red", 1: "cyan"}
for am_val in df["am"].unique():
    subset = df[df["am"] == am_val]
    ax.scatter(
        subset["cyl"], subset["disp"], color=colors[am_val], label=f"am={am_val}"
    )

ax.set_xlabel("as.factor(cyl)")
ax.set_ylabel("disp")
ax.set_title("График №5")
ax.legend(title="as.factor(am)")
plt.show()
