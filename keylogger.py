import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
smtp_port = 587

Sender = input("Enter your email: ")
SentTo = input("Enter recipient's email: ")
password = input("Enter your password: ")

subject = "Keylogger"
message = "Test message"

msg = MIMEMultipart()
msg["From"] = Sender
msg["To"] = SentTo
msg.attach(MIMEText(message, "plain"))
msg["Subject"] = subject

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(Sender, password)
    text = msg.as_string()  # Changed 'test' to 'text' for the message
    server.sendmail(Sender, SentTo, text)
    server.quit()
    print("Email sent successfully")
except Exception as e:
    print("An error occurred:", e)
