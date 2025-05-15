import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv("predictions.csv")

# Filter for human_development_index rows
df_population = df[df["Predicate"] == "human_development_index"]

# Extract rows
y_pred = df_population[df_population["Set"] == "y_pred"].iloc[0, 2:]
y_true = df_population[df_population["Set"] == "y_true"].iloc[0, 2:]
y_min = df_population[df_population["Set"] == "y_min"].iloc[0, 2:]
y_max = df_population[df_population["Set"] == "y_max"].iloc[0, 2:]
heads = df_population[df_population["Set"] == "heads"].iloc[0, 2:]

# Combine into a DataFrame
data = pd.DataFrame({
    "head": heads.values,
    "y_true": pd.to_numeric(y_true, errors='coerce'),
    "y_pred": pd.to_numeric(y_pred, errors='coerce'),
    "y_min": pd.to_numeric(y_min, errors='coerce'),
    "y_max": pd.to_numeric(y_max, errors='coerce'),
})
data.dropna(inplace=True)

# Sort by true value for alignment
data_sorted = data.sort_values("y_true").reset_index(drop=True)

# Filter range from "angola" to "singapore"
start_idx = data_sorted[data_sorted["head"] == "angola"].index[0]
end_idx = data_sorted[data_sorted["head"] == "norway"].index[0] + 1
subset = data_sorted.iloc[start_idx:end_idx].reset_index(drop=True)

# Plot
x = np.arange(len(subset))
plt.figure(figsize=(12, 6))
plt.vlines(x, subset["y_min"], subset["y_max"], color="teal")
plt.scatter(x, subset["y_pred"], color="blue", marker="x")
plt.scatter(x, subset["y_true"], color="black", marker="o")

plt.xticks(x, subset["head"], rotation=90, fontsize=8)
plt.title("Regression Predictions with Intervals vs. Ground Truth")
plt.ylabel("Human Development Index")
plt.tight_layout()
plt.grid(True)

# Save it
plt.savefig("human_development_index_plot.pdf", dpi=300, bbox_inches='tight')
plt.show()