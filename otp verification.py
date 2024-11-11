import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
otp = random.randint(1111,9999)

smtp_server = "smtp.gmail.com"
smtp_port = 587
mailusername = "tadepallisairajesh@gmail.com"
mailpassword = "ugwe cqdz ujwd mzrd"
from_email = "tadepallisairajesh@gmail.com"
to_email = input("Enter mail id: ")
subject = "OTP For Verification"
body = f"Otp for Verification is {otp}\nThanks for choosing codegnan"
msg = MIMEMultipart ()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(mailusername,mailpassword)
server.send_message(msg)

verifyotp = int(input("Enter OTP sent to your mail({to_email}): "))
if verifyotp == otp:
    print("Verification successfull")
else:
    print("Verification failed")
