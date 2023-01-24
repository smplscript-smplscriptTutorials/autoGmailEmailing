from email.message import EmailMessage
import ssl
import smtplib

def email(sender: str, password: str, receiver: str, subject: str, body: str):
    sender = sender
    password = password
    receiver = receiver

    subject = subject
    body = body

    em = EmailMessage()
    em["From"] = sender
    em["Password"] = password
    em["To"] = receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())
