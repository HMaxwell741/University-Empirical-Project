# How has market sentiment changed with oil over the course of the 2026 Iran war?

**Blog Link:**  https://hmaxwell741.github.io/University-Empirical-Project/blog/blog.html

Welcome, this is my university empirical project for module BEE2041 Data Science in Economics.

This is a data driven research project on how financial news sentiment changed during the Iran war, as well as how oil and the wider markets reacted. We will see if sentiment aligns well with key events, if it can be used as a measure of fear, its relation with oil, and what factors, if any, can help us predict tomorrow’s sentiment. In order to do this, we have done the following:

 -  Collect relevant news stories and financial data from API’s.
-   Use NLP models to calculate sentiment scores.
-   Explore any relationships through graphs and regression modelling.

I have created the code necessary to do this, and then a final output in the form of a blog post using Quarto. These figures will auto update if you run the blog.qmd file and preview it. Although the final gitpages blog post link wont be changed unless you push the new blog.html (no need to do this, just use my link in the (blog link and data/) or in the README.

This project is in no way linked to politics or beliefs, it just examines what has happened through accessible news and market data.

Best,
Harrison

  

>***Both contributors are me (Harrison Maxwell)**; one is an old account and the other is a new one using my student email. For some reason my laptop seems to use my BritishThyme account.*

  

## Please see blog for research breakdown, findings, and decision justification

This README covers how to run the code as well as a brief overview and its links to the course for my examiner.

**Blog Link:**  https://hmaxwell741.github.io/University-Empirical-Project/blog/blog.html

The blog has an introduction for the research topic, discussing our code and collection data, our data findings and graphs, regression models, limitations, and then a conclusion.

  

**README Contents:**

- [Introduction](#please-see-blog-for-research-breakdown-findings-and-decision-justification)

- [Overview](#Overveiw)

- [Setup & Replicability](#Setup-&-Replicability)

- [Alignment with course content and assessment instructions](#Alignment-with-course-content-and-assessment-instructions)

- [References](#References)

  

## Overview

>**All scripts are also fully commented.**

  

Script 1 (`Scripts/Scraping.ipynb`) covers scraping and cleaning. It uses 3 API's to get news data (The Guardian Open Platform API, Alpha Vantage, NewsAPI). It then parses HTML, wrangles and cleans data, and runs an NLP model (all-MiniLM-L6-v2) to check for relevancy. It also uses yfinance to get financial data.

>*Runtime*: Around 7 minutes due to rate limiting

  

Script 2 (`Scripts/Sentiment.ipynb`) merges all data and runs our another NLP model (ProsusAI/finbert) that has been pre trained on financial news data to find the sentiment of each news article. Data is then aggregated per day, and SQL is used to create new columns such as moving averages or lagging.

>*Runtime*: Around 2 min on a average laptop (NLP models)

  

Script 3 (`Scripts/Outputs.ipynb`) uses our dataset from script 2 to generate our outputted graphs and regression models.

  

## Setup & Replicability

  

>**Note:** I am using Python 3.14 as the kernel, I have also tested it on 3.13.

 I have used make files to automate the process.  All pip install commands and requirements are covered within the make files for ease of use (other than ```pip install papermill``` which is detailed separately, all details below). 

If you wish to re-render the html, you will also require quarto, although this is not required for reproducing the code.

**There are 2 options:**

- **Option 1:** you will need api keys to run all 3 scripts. 
- **Option 2:** this wont need API keys, as you will just run sentiment and outputs scripts using precompiled date, this option is here to save time as you wont need to create your ```.env``` file and API keys. 

### 1. Clone the repository (general to both methods)

  

```bash

git  clone  https://github.com/HMaxwell741/University-Empirical-Project.git

cd  University-Empirical-Project

```
Then open the folder ```University-Empirical-Project```
### 2. Set up API keys (if using option 1, thus all 3 scripts and need API keys)

>**Note:** If using option 2, you can skip this step, as you will just run sentiment and outputs scripts, not the scraping script, thus you will not need API keys

  

Create an `.env` file, and fill it with your keys. Ensure file name is `.env`. Ensure it is not in any further folders (But is still within the main local repo folder of course)

  

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

### 3. Run
> **All pip install commands are located inside the make files for your ease of use**, other than papermill which is installed before.

> **Here is a list of what is installed:** papermill, requests, pandas, beautifulsoup4, sentence-transformers, python-dateutil, newsapi-python, python-dotenv, yfinance, transformers, torch, statsmodels, matplotlib, scikit-learn, scipy, huggingface_hub, folium, and jupyter.

>**Note:** First time install of libraries may take a couple of minutes

**Option 1 (3 scripts and API keys setup, ensure ```.env``` file is setup)**
```
pip install papermill
python Make/Make_with_API.py
```
**Option 2 (Saving time using pre complied date, no API keys, just sentiment and output scripts)**
```
pip install papermill
python Make/Make_no_api.py
```

## Alignment with course content and assessment instructions

  

-  **Languages used:** All **python**, except for some **SQL** used for the creation and calculation of new columns, python could have been used instead but I chose to do it in SQL to further demonstrate skills learned in this module. **Git/Bash** used for github.

-  **Unit 5 Content:** Web scraping via APIs, however this still required calling html requests and then cleaning/parsing HTML with Beautifulsoup. Regression models with dummy variables, interaction terms, and accounting for heteroskedasticity (HC3).

  

## References

Please see pdf copy of reference in main.
