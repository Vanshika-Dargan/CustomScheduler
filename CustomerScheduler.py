import os 
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from pathlib import Path



PORT=587
EMAIL_SERVER='smtp-mail.outlook.com'

curr_dir=Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()

env_variables=curr_dir/'.env'
load_dotenv(env_variables)

sender_email=os.getenv("EMAIL")
password_email=os.getenv("PASSWORD")


def send_email(subject,reciever_email,name,due_date,invoice_no,amount):
    
    msg=EmailMessage()
    msg["Subject"]=subject
    msg["From"]=sender_email
    msg["To"]=reciever_email
    msg["BCC"]=sender_email

    msg.set_content(
        f"""\
        Hi {name},
        {due_date}
        {invoice_no}
        {amount}
        """
    )

    with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
         server.starttls()
         server.login(sender_email,password_email)
         server.sendmail(sender_email,reciever_email,msg.as_string())


if __name__ == "__main__":
     send_email(
          subject="Invoice Reminder",
          reciever_email="vanshikadargan.vd@gmail.com",
          name="John Doe",
          due_date="18,September 2023",
          invoice_no="XABBC",
          amount="2000.00"
           )
     
     
    
    
   






