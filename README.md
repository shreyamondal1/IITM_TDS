# Retail Performance Analysis — Inventory Turnover (2024 Q1–Q4)

**Email:** 23f1001792@ds.study.iitm.ac.in

**Short summary:**  
The company’s 2024 quarterly inventory turnover ratios show volatility and an overall average below the industry benchmark of 8. The current average inventory turnover for 2024 Q1–Q4 is **5.47**. The recommended solution is: **optimize supply chain and demand forecasting**.

---

## Dataset
Quarterly Inventory Turnover Ratio for 2024:

| Quarter | Inventory Turnover |
|---------|--------------------|
| Q1      | 4.82               |
| Q2      | 8.04               |
| Q3      | 2.84               |
| Q4      | 6.16               |

**Average (2024, Q1–Q4): 5.47**

**Industry Target (Benchmark): 8.00**

---

## What I did
1. Loaded the quarterly data and computed descriptive statistics and the overall average (5.47).  
2. Visualized the quarter-wise trend and compared it against the industry benchmark (8.0).  
3. Drafted a data story that links findings to business implications and recommendations centered on the solution: **optimize supply chain and demand forecasting**.

Files:
- `inventory_turnover_analysis.py` — analysis & visualization
- `inventory_trend.png` — line trend chart
- `inventory_bar_chart.png` — bar trend chart

---

## Key findings (data-driven)
1. **Average below benchmark** — The 2024 average turnover is **5.47**, materially below the industry target of 8.0. This indicates inventory is turning over ~1.5× slower than the benchmark.
2. **High volatility across quarters** — Q2 meets/exceeds the benchmark (8.04), but Q3 is very low (2.84). Such swings suggest demand inconsistency and/or replenishment timing issues.
3. **Possible seasonal or operational causes** — The deep dip in Q3 suggests either overstocking going into Q3 or weak sales (or delays in order fulfilment). Q2 outperformance may reflect a temporary strong sales window or favourable promotions.
4. **Average masks extremes** — While Q2 and Q4 are reasonable, Q3’s extremely low turnover drags the mean down; tactical solutions must address the drivers of Q3’s poor performance.

---

## Business implications
- **Working capital tied up** — Lower turnover increases inventory carrying costs (storage, insurance, obsolescence) and reduces liquidity.
- **Opportunity cost** — Money in excess inventory could be allocated to higher-return investments (marketing, store improvements, or price promotions).
- **Risk of obsolescence** — Slow-turning goods, if product lifecycles are short, risk markdowns and loss of margin.
- **Customer fulfilment risk** — If low turnover arises from poor replenishment (stockouts elsewhere), customer service and sales suffer.

---

## Specific recommendations to reach the target of 8
(Organized by timeline and owner)

### Immediate (0–3 months)
1. **Quick inventory triage (Ops & Merchandising):**
   - Identify the slow-moving SKUs (esp. those contributing to Q3 overstock).
   - Flag top 20% SKUs by value that have turnover < 2; pursue promotions, bundle deals, or targeted markdowns.
2. **Short promotions to convert excess stock:**
   - Time-limited discounts, flash sales, and targeted email campaigns for slow categories.
3. **Improve visibility of pipeline:**
   - Daily/weekly inventory reports for category leads showing days-of-inventory and inbound PO timing.

### Near-term (3–6 months)
1. **Demand forecasting improvements (Data/Analytics & Supply Chain):**
   - Implement a simple ensemble forecast combining (a) last 4-quarter seasonality, (b) promotion calendar adjustments, and (c) a short-term exponential smoothing model.
   - Start using a rolling forecast horizon (4–12 weeks) and measure forecast accuracy (MAPE).
2. **Replenishment policy tuning:**
   - Move from fixed-interval ordering to dynamic reorder points (safety stock + lead time variability).
3. **Vendor lead-time SLAs:**
   - Negotiate quicker replenishment or smaller, more frequent shipments to lower safety stock needs.

### Medium-term (6–12 months)
1. **Integrated S&OP (Sales & Ops Planning):**
   - Monthly cross-functional S&OP meetings to align promotions, purchases, and warehouse capacity.
2. **Advanced forecasting & inventory optimization:**
   - Explore ML models (gradient boosting, time series decomposition) for SKUs with stable history.
   - Implement multi-echelon inventory optimization if multiple warehouses/sites exist.
3. **SKU rationalization:**
   - Remove or consolidate SKUs with persistently low turnover and low margin.

### Metrics to monitor (KPIs)
- Inventory Turnover Ratio (monthly & rolling 4-quarter)
- Days Inventory Outstanding (DIO)
- Forecast accuracy (MAPE) by SKU/category
- % of SKUs with turnover < 2
- Carrying cost as % of sales

---

## Proposed roadmap (high-level)
- Weeks 0–4: Run triage, promotions for slow SKUs, and create weekly dashboard. (Tactical savings expected within 1–2 months.)
- Months 1–3: Implement short-term forecasting improvements, tune reorder points; expect 10–20% improvement in turnover for targeted categories.
- Months 3–12: Deploy advanced models and S&OP; aim to move company average from 5.47 toward 8.0 over 12 months, focusing on both demand uplift and inventory reduction.

---

## Risks & mitigations
- **Over-promoting can erode margins** — Use targeted promotions where margin protection is possible; consider bundles instead of blanket discounts.
- **Forecast changes take time** — Start with high-impact categories to get early wins.
- **Supplier constraints** — If vendors cannot ship more frequently, consider inventory pooling or local safety stock agreements.

---

## Conclusion
The data story shows that while there are quarters meeting the benchmark (Q2) the overall average **5.47** indicates excess inventory and inefficient turnover. The recommended overarching solution is to **optimize supply chain and demand forecasting**, backed by immediate tactical steps (promotions/triage), near-term replenishment and forecasting tuning, and medium-term investments in S&OP and advanced forecasting to reach the target turnover of **8**.

### LLM Assistance
This PR was developed with assistance from LLM tools:
- Claude Code for generating the analysis code
- ChatGPT for refining the README
