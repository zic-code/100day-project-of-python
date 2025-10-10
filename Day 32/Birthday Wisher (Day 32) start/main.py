import smtplib
import datetime as dt
import random
my_email = "jisoostest@gmail.com"
app_password ="pgtg ghbd hity mkpp"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Friday Motivation \n\n{quote}")












# # import smtplib
# #
# # my_email = "jisoostest@gmail.com"
# # app_password ="pgtg ghbd hity mkpp"
# #
# # with smtplib.SMTP("smtp.gmail.com") as connection:
# #     connection.starttls()
# #     connection.login(user=my_email, password=app_password)
# #     connection.sendmail(from_addr=my_email,
# #                         to_addrs="jisoostest@yahoo.com",
# #                         msg="Subject: Whats up \n\n This is body of my email"
# #                         )
# #
# #
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year = 1991, month=4,day=13,hour=6,minute=30)
# print(date_of_birth)
