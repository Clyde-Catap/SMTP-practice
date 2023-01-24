import  smtplib
import  datetime as dt
import random

quotelist = open(file="quotes.txt").read().splitlines()


my_email = "cataptrial@gmail.com"
password = "ogkilmewyhynbjns"

now = dt.datetime.now()
year = now.weekday()

if year == 3:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="cataptrial@yahoo.com", msg="Subject:Quote for the day\n\n "
                                                                                 f"{random.choice(quotelist)}")
    connection.quit()




