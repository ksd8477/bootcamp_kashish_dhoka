
# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
This project aims to understand whether an ETF trading strategy that has performed well on historical data will continue to be effective going forward,a core question a portfolio manager faces before committing further capital to it. Because market conditions and patterns can shift over time, a strategy built on past price behavior carries the risk that the conditions it relied on may no longer hold, meaning strong historical performance does not guarantee future results. Understanding this risk is critical before continuing capital allocation to the strategy, since a rule that looked profitable in a backtest could underperform once market conditions change.

## Stakeholder & User
Decision owner: Portfolio Manager — decides whether to continue, adjust, or discontinue capital allocation to the strategy.
Tool/operator: Quant analyst/researcher — monitors strategy performance and produces the assessment the PM works with.

## Useful Answer & Decision
Type: Predictive (forecasting whether the strategy will continue performing), with descriptive elements as supporting context (historical performance to date)
Metric/artifact: A forecast with risk bands (not a single point estimate), scenario analysis under different market conditions, and a clear recommendation: continue / adjust / discontinue

## Assumptions & Constraints
Stationarity: assumes the market patterns the strategy historically exploited will persist
Liquidity: assumes the ETF can be traded in the needed size without materially moving its price
Transaction costs: assumes the costs used in the original backtest reflect real trading costs going forward
Capacity: assumes the strategy can scale to the capital allocated without returns degrading
Time horizon: framed specifically around the PM's "next year" question

## Known Unknowns / Risks
Uncertain whether historical patterns will hold (regime change risk)
Strategy may be overfit to the specific historical period it was tested on
Unknown future market shocks or volatility regime shifts
Mitigation: rolling out-of-sample validation, monitoring live performance against backtest expectations over time

## Lifecycle Mapping
Determine strategy viability going forward → Problem Framing & Scoping (Stage 01) → Scoping README + stakeholder memo
Validate historical performance robustness → later modeling/EDA stage → backtest and stress-test report
Communicate risk-adjusted recommendation to PM → evaluation/reporting stage → stakeholder memo or dashboard

## Repo Plan
data/, src/, notebooks/, docs/
