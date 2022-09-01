from bs4 import BeautifulSoup
import smtplib
import requests
import os

MY_EMAIL = os.environ.get("my_email")
MY_PASSWORD = os.environ.get("my_password")

cryptocurrency_name = "bitcoin"  # lowwer case only.
target_price = 22900.00

url = f"https://www.coindesk.com/price/{cryptocurrency_name}/"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

price = soup.find("span", {"class": "typography__StyledTypography-owin6q-0 jvRAOp"})
price_text = price.text

message = f"{cryptocurrency_name} is now ${price.text}"
print(message)

float_price = price_text.replace(",", "")
float_price = float(float_price)

if float_price < target_price:
    # ENTER HERE YOUR EMAIL HOST SMTP ADDRESS
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:{cryptocurrency_name} Price Alert!\n\n{message},\nlink:- {url}"
                            )
    print("Email is Send.")
