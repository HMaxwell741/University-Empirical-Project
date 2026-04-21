# How has market sentiment changed with oil during the course of the 2026 Iran war?

Welcome, this is my university empirical project for module BEE2041 Data Science in Economics.
 
  - A data driven research project on how financial news sentiment changed during the Iran war, as well as how oil and the wider markets reacted.
  - It is in no way linked to politics or beliefs, it just examines what has happened through accessible news and market data. 

 >***Both contributors are me (Harrison Maxwell)**; one is an old account and the other is a new one using my student email. For some reason my laptop seems to use my BritishThyme account.*

## Please see blog for research breakdown, findings, and decision justification
This README covers how to run the code as well as a brief overview and its links to the course for my examiner.
> **Link to blog:** *(still need to make it)*

**Contents:** 
- [Introduction](#please-see-blog-for-research-breakdown-findings-and-decision-justification)
- [Overview](#Overveiw)
- [Setup & Replicatability](#Setup-&-Replicatability)
- [Alignment with course content and assessment instructions](#Alignment-with-course-content-and-assessment-instructions)
- [References](#References)

## Overview 
>*Please only run scripts in `Scripts/`.  
>All scripts are also fully commented.*

Script 1 (`Scripts/Scraping.ipynb`) covers scraping and cleaning. It uses 3 API's to get news data (The Guardian Open Platform API, Alpha Vantage, NewsAPI). It then parses HTML, wrangles and cleans data, and runs an NLP model (all-MiniLM-L6-v2) to check for relevancy. It also uses yfinance to get financial data.
>*Runtime*:  Around 6 minutes due to rate limiting

Script 2 (`Scripts/Sentiment.ipynb`) merges all data and runs our another NLP model (ProsusAI/finbert) that has been pre trained on financial news data to find the sentiment of each news article. Data is then aggregated per day, and SQL is used to create new columns such as moving averages or lagging.
>*Runtime*: Around 2 min on a average laptop (NLP models)

Script 3 (`Scripts/Output.ipynb`) uses our dataset from script 2 to generate our outputted graphs and regression models.

## Setup & Replicatability

>**Note:** I am using Python 3.14 as the kernal, I have also tested it on 3.13.

### 1. Clone the repository

```bash
git clone https://github.com/HMaxwell741/University-Empirical-Project.git
cd University-Empirical-Project
```

### 2. Install dependencies

```bash
pip install requests pandas beautifulsoup4 sentence-transformers python-dateutil
            newsapi-python python-dotenv yfinance transformers torch statsmodels
            matplotlib scikit-learn scipy huggingface_hub 
```

> **Note:** First run model downloads may take a few minutes.

### 3. Set up API keys
> **Note:** You can skip the entire `Scripts/Scraping.ipynb` and just run the other 2 scripts (sentiment and ouput) using pre-complied data. This will save you having to create API keys.

Create an `.env` file, and fill it with your keys. Ensure file name is `.env`

```bash
#.env example 
guardian_TOKEN='your_key_here'
newsapi_TOKEN='your_key_here'
HF_TOKEN='your_key_here'
ALPHA_TOKEN='your_key_here'
```
All keys are free, you can sign up for your own key at the following links. One paid API could have sufficed, but for the purpose of replicability (and cost) only free tiers are used.

**Where to get keys:**

- [The Guardian OpenPlatform](https://open-platform.theguardian.com/)
- [Alpha Vantage](https://www.alphavantage.co/)
- [NewsAPI](https://newsapi.org/)
- [Hugging Face](https://huggingface.co/docs/hub/en/security-tokens)
>**Note:** The Hugging Face API key is not strictly required, it just helps it run smoother.
### 4. Run Order
>*Please only run scripts in `Scripts/`.  
>All scripts are also fully commented.*
- **1:  Scraping** (`Scripts/Scraping.ipynb`) 
- **2:  Sentiment** (`Scripts/Sentiment.ipynb`)
- **3: Graphs & Regression** (`Scripts/Output.ipynb`)

## Alignment with course content and assessment instructions

- **Languages used:** All **python**, except for some **SQL** used for the creation and calculation of new columns, python could have been used instead but I chose to do it in SQL to further demonstrate skills learned in this module. **Git/Bash** used for github.
- **Unit 5 Content:** Web scraping via APIs, however this still required calling html requests and then cleaning/parsing HTML with Beautifulsoup. Regression models with dummy variables, interaction terms, and accounting for for heteroskedasticity (HC3).

## References
Please see references PDF in main.
