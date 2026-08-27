# Project Title
SPY Next-Day Direction Prediction — Systematic Trading Signal
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
This project aims to understand whether historical price data can help predict SPY's upcoming day direction. 
This is genuinely uncertain because market patterns can shift over time, and a model trained on past data risks overfitting to that specific historical pattern rather than learning something that generalizes going forward. 
This matters because a portfolio manager could use a prediction like this to make real trading decisions.So distinguishing a genuine, reliable signal from noise has real financial consequences.

## Stakeholder & User
Decision owner: Portfolio Manager — uses the model's output and backtested performance to decide whether a systematic signal is reliable enough to inform real capital allocation.
Tool/operator: Junior Quantitative Analyst — builds, validates, and reports on the signal's performance before it reaches the PM, prioritizing honest risk-adjusted reporting over raw accuracy.

## Useful Answer & Decision
Type: Predictive (forecasting next-day price direction), evaluated through a backtested trading simulation rather than accuracy alone.
Metric/artifact: A backtest report including Sharpe ratio, maximum drawdown, and performance versus a buy-and-hold benchmark, alongside a clear conclusion on whether the signal shows genuine, risk-adjusted edge.

## Assumptions & Constraints
Stationarity: assumes patterns identified in historical SPY data will continue to hold going forward.
Liquidity: assumes SPY can be traded at the needed size without materially moving its price (reasonable given SPY's high trading volume).
Transaction costs: assumes backtested costs and slippage reasonably reflect real trading costs.
Data granularity: limited to daily OHLCV data, no intraday price information.
Time horizon: framed around next-day direction prediction specifically, not longer-term forecasting.

## Known Unknowns / Risks
Uncertain whether the model's edge, if any, reflects a genuine pattern or overfitting to the historical test period.
Market regime shifts could invalidate learned patterns without warning.
Unknown future volatility spikes or market shocks not represented in historical training data.
Mitigation: walk-forward validation (not random train/test splits) to reduce lookahead bias, and comparison against a random-signal baseline to test whether performance exceeds chance.

## Lifecycle Mapping
Frame the prediction problem and its real-world relevance → Problem Framing & Scoping (Stage 01) → Project README + stakeholder persona
Acquire and structure historical SPY price data → Data Acquisition & Ingestion → Raw and processed datasets in data/
Engineer predictive features from price history → Feature Engineering → Documented feature set in notebooks/ and src/
Build and validate a classification model using walk-forward validation → Modeling → Trained model + validation results
Evaluate the strategy's risk-adjusted performance against a buy-and-hold benchmark → Evaluation & Risk Communication → Backtest report with Sharpe ratio, drawdown, and cost-adjusted returns
Communicate findings and honest limitations to a stakeholder → Reporting & Delivery → Stakeholder memo or summary report

## Repo Plan
data/, src/, notebooks/, docs/, model/, reports/ — full structure built in Stage 02, populated stage by stage through the course.