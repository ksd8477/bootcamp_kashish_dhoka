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

## Data Storage
- `data/raw/` — unedited source data as pulled from Yahoo Finance
- `data/processed/` — cleaned/derived data (populated in later stages)
- File format: CSV
- Code reads/writes via `save_raw_data()` / `load_raw_data()` in `src/utils.py`, which resolve paths from the `DATA_DIR` environment variable (set in `.env`) rather than hardcoded paths.

## Data Preprocessing
Cleaning functions live in `src/cleaning.py`: datetime indexing, duplicate removal, chronological sorting, forward-fill for missing values. Applied via `preprocess_pipeline()`, output saved to `data/processed/spy_processed.csv`.

## Exploratory Data Analysis
See `notebooks/project_pipeline.ipynb` for full EDA. Summary stats and visualizations generated via `src/eda.py`. Key observations: [fill in one honest sentence once you've looked at the plots - e.g., "returns show fat tails typical of financial data" or "volatility clusters visibly around 2020"].

## Feature Engineering

| Feature | Rationale |
|---|---|
| `ma_5`, `ma_10`, `ma_20` | Moving averages smooth noise and reveal trend direction; price relative to its MA is a standard momentum signal |
| `momentum` | Captures recent price change magnitude; short-term momentum has historically shown some persistence |
| `volatility` | Rolling std of returns gives regime context - same price move means different things in calm vs. turbulent markets |
| `rsi` | Standard technical indicator flagging potential overbought/oversold reversal points |
| `target` | Label: whether next day's close is higher than today's (binary classification target) |

**Important note on `target`:** this is the only feature that looks forward (`shift(-1)`), which is intentional since it's the label being predicted. All other features use only past/current data (`shift()` positive, `.rolling()`) to avoid lookahead bias.