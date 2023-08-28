# importing libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(receiver_email, subject, message, message_type, attachment_files):
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

    # attaching a file
    for attachment_file in attachment_files:
        attachment = open(attachment_file,'rb')
        base = MIMEBase('application','octet-stream')
        base.set_payload((attachment).read())
        encoders.encode_base64(base)
        base.add_header('Content-Disposition', f'attachment; filename={attachment_file}')
        msg.attach(base)

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
        