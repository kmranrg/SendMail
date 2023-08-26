# importing libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(receiver_email, subject, message, message_type):
    # email configurations
    sender_email = 'smartgurucool@gmail.com'

    # email server configuration for gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'smartgurucool@gmail.com'
    smtp_password = open('key.txt').read()

    # creating a MIMEText object to represent the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message,str(message_type)))

    # connecting to SMTP server
    try:
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls() # use TLS for secure connection
        server.login(smtp_username, smtp_password)

        # send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit() # quit the server
        return 'Email sent successfully'

    except Exception as e:
        return 'Error sending email:',str(e)
        