import pandas as pd
import smtplib
import datetime as dt
import random


#Hint1.
## file path
data_file = "./birthdays.csv"
# file read
df=pd.read_csv(data_file)

# Hint 2
today = dt.date.today()
today = (today.month, today.day)


# 내가 원하는 데이터는 현재 날짜와 birthday.cvs가 일치하는 데이터들을 가져와야한다.(key는 tuple로 값은 해당 데이터들을 가져와야한다.)
# today's date를 튜플로 뽑았기 때문에 tuple로 값을 매치해서 그에 해당하는 데이터들을 가져오는 방식을 선택해야한다.
#birthday에 해당하는 튜플과 그에 따른 데이터를 얻으려면 dictionary를 사용하는게 용이(key,value)
#새로운 dictionary를 얻기위해 dictionary comprehension을 사용:
#dictionary comprehension:
#dictionary 이름= {key 표현식:value 표현식 for 변수 in 반복가능 객체 if 조건 }
#key = (data중 "month", data중"day")
#value = 전체 데이터
#변수설정: 인덱스와 데이터 줄( data_row)
#반복가능객체 = df.iterrows()


birthdays_dict = {
    (data_row["month"], data_row["day"]) : data_row for ( index, data_row) in df.iterrows()
}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    name = birthday_person['name']
    email = birthday_person['email']
    template_number = 3
    chosen_template = random.choice(range(1,template_number+1))
    random_template = f"letter_{chosen_template}.txt"
    print(random_template)
    with open(f"letter_templates/{random_template}", "r",encoding="utf-8") as f:
        letter_contents = f.read()
        letter_contents = letter_contents.replace("[NAME]",name)
        print(letter_contents)
    #smtp
    my_email= "jisoostest@gmail.com"
    password="munn qguk iqmb gqzm"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!!\n\n {letter_contents}"
        )

##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day✅

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)--done

# HINT 2: Use pandas to read the birthdays.csv--done

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



