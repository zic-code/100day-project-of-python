import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

#api_key setting
load_dotenv()
alpha_api_key =os.environ.get("Alpha_Vintage_api_key")
news_api_key = os.environ.get("news_api_key")
Twillio_account_sid =os.environ.get("Twillio_account_sid")
Twillio_auth_token = os.environ.get("Twillio_auth_token")

#param setting
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":alpha_api_key
}

r= requests.get(url=STOCK_ENDPOINT,params=STOCK_PARAMS)
stock_data = r.json()

#list comprehension --> list_name = new expression for item in iterable.
daily_data = stock_data["Time Series (Daily)"]
dates=list(daily_data.keys())
daily_closing_price= [ (date, float(daily_price["4. close"]))for date, daily_price  in daily_data.items()]
today_price=daily_closing_price[0]

# top3_list =


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday=daily_closing_price[1]
#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday=daily_closing_price[2]
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
if yesterday[1]-before_yesterday[1] < 0:
    plus_minus = "🔻"
elif yesterday[1]-before_yesterday[1] >0:
    plus_minus = "🔺"
else:
    plus_minus = "⏸️"

abs_diff= abs(yesterday[1]-before_yesterday[1])
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff= round((abs_diff/before_yesterday[1])*100,2)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_diff > 1:
    NEWS_PARAMS = {
        "q":STOCK_NAME,
        "from":yesterday[0],
        "sortBy":"popularity",
        "apiKey":news_api_key
    }
    rn= requests.get(url=NEWS_ENDPOINT,params=NEWS_PARAMS)
    news_data = rn.json()


    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    list_articles= [(articles["title"],articles["description"]) for articles in news_data["articles"][:3]]
    print(list_articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    client = Client(Twillio_account_sid, Twillio_auth_token)
    for article in list_articles:
        title = article[0]
        description =article[1]

        client = Client(Twillio_account_sid, Twillio_auth_token)
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"{STOCK_NAME}: {plus_minus}{percent_diff}\nHeadline: {title}\n Breif: {description}",
            to='whatsapp:+19147279719'
        )


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

