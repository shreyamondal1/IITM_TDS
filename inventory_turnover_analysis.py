import pandas as pd
import matplotlib.pyplot as plt

data = {
    "quarter": ["Q1", "Q2", "Q3", "Q4"],
    "turnover": [4.82, 8.04, 2.84, 6.16]
}

df = pd.DataFrame(data)

# Industry benchmark
benchmark = 8.0

# Calculate average
average_turnover = df["turnover"].mean()
print("Average Inventory Turnover:", round(average_turnover, 2))

# -----------------------------
# Plot 1: Basic trend chart
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["quarter"], df["turnover"], marker="o", linewidth=2, label="Turnover")
plt.axhline(benchmark, color="red", linestyle="--", label=f"Target Benchmark ({benchmark})")

plt.title("Inventory Turnover Ratio - 2024 Quarterly Trend")
plt.ylabel("Inventory Turnover")
plt.xlabel("Quarter")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.savefig("inventory_trend.png")
plt.close()

# -----------------------------
# Plot 2: Bar chart
# -----------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["quarter"], df["turnover"], color="skyblue")
plt.axhline(benchmark, color="red", linestyle="--", label=f"Target Benchmark ({benchmark})")

plt.title("Inventory Turnover Ratio - 2024 Quarterly (Bar Chart)")
plt.ylabel("Inventory Turnover")
plt.xlabel("Quarter")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.savefig("inventory_bar_chart.png")
plt.close()
