import datetime as dt
import smtplib
from random import choice

USER='arpi.mona@gmail.com'
PASSWORD='xmrj mhgb muhs jcds'
TO_ADDRESS='bosearpita2711@yahoo.com'
with open('./quotes.txt') as file:
    data=file.readlines()

today=dt.datetime.now()
count=today.weekday()+1

msg_body=''

for _ in range(count):
    msg_body+=choice(data)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=USER, password=PASSWORD)
    connection.sendmail(from_addr=USER, to_addrs=TO_ADDRESS, msg=f"Subject: Motivational quotes for today\n\n{msg_body}")

