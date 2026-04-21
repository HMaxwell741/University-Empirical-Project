# University-Empirical-Project

Welcome, this project aims to explore **how market sentiment has changed with oil during the course of the Iran war**. It is in no way linked to politics or believes, it just examines what has happened through accessable news and market data. **Both contributors are me (Harrison Maxwell)**; one is an old account and the other is a new one using my student email. For some reason my laptop seems to use my BritishThyme account.

## Breif Overview

Script 1, Scraping.ipynb. This script uses a mix of 3 APIs to scrape news data (The Guardian Open Platform API, AlphaVantage, NewsAPI), and financial data from yfinance.The script also performs data cleaning before saving all the data.

Script 2, Sentiment.ipynb. This script merges the all of the data, and runs it through our sentiment analysis model. It then aggregates data by day, and creates new data columns such as lagged data or percentage changes.

Script 3, Outputs.ipynb. This script generates all graphs and regression outputs.

**Important note on time to run and laptop specs**

Depending on the specs of your device, the NLP models may take a couple of minutes to run. I am running an RTX 4070 super (desktop). However this still runs fine on my laptop (I5 ultra), where both scripts will complete after a total of 10min.
(Time to run should now be very feasible on any laptop due to batching, although more powerfull ones with accelerate it substancially).
