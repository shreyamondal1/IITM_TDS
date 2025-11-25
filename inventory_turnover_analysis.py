import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP

# Data
df = pd.DataFrame({
    "quarter": ["Q1", "Q2", "Q3", "Q4"],
    "turnover": [4.82, 8.04, 2.84, 6.16]
})

benchmark = 8.0

# Calculate average
decimal_values = [Decimal("4.82"), Decimal("8.04"), Decimal("2.84"), Decimal("6.16")]
avg_decimal = (sum(decimal_values) / Decimal(len(decimal_values))).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP
)

print("Average Inventory Turnover:", avg_decimal)

# -----------------------------
# Plot 1: Line Trend Chart
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["quarter"], df["turnover"], marker="o", linewidth=2, label="Turnover")
plt.axhline(benchmark, color="red", linestyle="--", label=f"Benchmark ({benchmark})")

plt.title("Inventory Turnover Ratio - 2024 Quarterly Trend")
plt.ylabel("Inventory Turnover")
plt.xlabel("Quarter")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend()

plt.savefig("inventory_trend.png")
plt.close()

# -----------------------------
# Plot 2: Bar Chart
# -----------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["quarter"], df["turnover"], color="skyblue")
plt.axhline(benchmark, color="red", linestyle="--", label=f"Benchmark ({benchmark})")

plt.title("Inventory Turnover Ratio - 2024 Quarterly (Bar Chart)")
plt.ylabel("Inventory Turnover")
plt.xlabel("Quarter")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend()

plt.savefig("inventory_bar_chart.png")
plt.close()

print("Charts saved: inventory_trend.png, inventory_bar_chart.png"
