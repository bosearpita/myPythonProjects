##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


from datetime import datetime, date
import smtplib
from random import choice, randint
import pandas as pd

NAME = ''
USER = 'arpi.mona@gmail.com'
PASSWORD = 'xmrj mhgb muhs jcds'
TO_ADDRESS = ''
def letter_select():
    global NAME, TO_ADDRESS
    ch = randint(0,2)


    with open('./letter_templates/'f"letter_{ch+1}.txt",mode='r') as file:
        body = file.read()
        new_body = body.replace('[NAME]', NAME)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs=TO_ADDRESS,
                            msg=f"Subject: Happy Birthday!\n\n{new_body}")


date_today = datetime.now()

print(f"Month is {date_today.month}, Day is {date_today.day}")
data=pd.read_csv('birthdays.csv')
new_data=data.values.tolist()

for i in new_data:
    print(i)
    if i[3] == int(date_today.month) and i[4] == int(date_today.day):
        NAME = i[0]
        TO_ADDRESS = i[1]
        print(f"Address to be sent: {TO_ADDRESS}")
        letter_select()







