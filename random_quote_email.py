
import smtplib
import datetime as dt
import random
now=dt.datetime.now()
week_day=now.weekday()
print(now.weekday())
my_email = "[Your Email Id From Which Email Will Be Sent]"
password="[Your App Generated Password]"
with open('quotes.txt') as file:
    quote=file.readlines()
    random_quote=random.choice(quote)
    print(random_quote)
with smtplib. SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection. sendmail(
        from_addr=my_email,
        to_addrs="[Recievers Email Id]",
        msg=f"Subject:Motivation\n\n{random_quote}"
    )
    print("email sent")


