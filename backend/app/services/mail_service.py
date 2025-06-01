#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.utils.logging import warn, error
from app.global_config import mail_service_config

class EmailService:
    
    def __init__(self, email, verification_code):
        # please manually configure your email credential
        server_email = mail_service_config['email']
        server_passwd = mail_service_config['key']
        if not server_email or not server_passwd:
            warn("Your mail server does not have a credential, so the email will not be sent.", __file__)

        receiver_email = email
        verification_code = verification_code
        subject = 'Almacenar shop verification code'
        body = f'Here is your verification code: {verification_code}'

        msg = MIMEMultipart()
        msg['From'] = server_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        try:
            server.login(server_email, server_passwd.replace('_', ' '))
            server.sendmail(server_email, receiver_email, msg.as_string())
        except Exception as e:
            error(f"Failed to login! Reason: {e}", __file__)

        exit(0)
        server.quit()