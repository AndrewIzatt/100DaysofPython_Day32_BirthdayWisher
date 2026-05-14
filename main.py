import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

# Enter Credentials in .env file (See .env.example)

HOSTNAME = os.environ["SMTP_HOSTNAME"]
PORT = int(os.environ["SMTP_PORT"])
USERNAME = os.environ["SMTP_USERNAME"]
PASSWORD = os.environ["SMTP_PASSWORD"]
TEST_EMAIL_1 = os.environ["TEST_EMAIL_1"]

with smtplib.SMTP(HOSTNAME, PORT) as connection:
    connection.starttls()
    connection.login(user=USERNAME, password=PASSWORD)
    connection.sendmail(from_addr=USERNAME,to_addrs=TEST_EMAIL_1,msg = "Subject: Test email\n\nHello")
