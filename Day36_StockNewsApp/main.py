import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_URL = "https://newsapi.org/v2/everything"
STOCK_URL = "https://www.alphavantage.co/query"

NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "apiKey": "4ef6324e3afb4389b1800efac0e93b4c"
}

STOCK_PARAMS = {
    'function': "TIME_SERIES_DAILY",
    'outputsize': "compact",
    'symbol': STOCK,
    'apikey': "A6BKI1CT8M9DVUWY"
}

today = dt.datetime(2023, 11, 3)  # yesterday was not available at this time. Therefore, hard code date
yesterday = today - dt.timedelta(days=1)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_response = requests.get(STOCK_URL, STOCK_PARAMS)
stock_response.raise_for_status()

stock_data = stock_response.json()
stock_data_slice = stock_data['Time Series (Daily)']
stock_data_today = float(stock_data_slice[today.strftime("%Y-%m-%d")]['4. close'])
stock_data_yester = float(stock_data_slice[yesterday.strftime("%Y-%m-%d")]['4. close'])

if abs((stock_data_today/stock_data_yester)-1) > .001:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get(NEWS_URL, NEWS_PARAMS)
    news_response.raise_for_status()

    news_data = news_response.json()
    news_articles = news_data['articles'][:3]
    formatted_articles = [f"url: {article['url']}\nheadline: {article['title']}\n{article['description']}" for article in news_articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# Can't do due to subscription

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

