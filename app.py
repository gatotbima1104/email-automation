import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

def email_automation(subject, body_template, to_emails):
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = 25
    smtp_username = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASS')

    for to_email in to_emails:
        # Create the MIME object
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Replace the placeholder with the recipient's name
        personalized_body = body_template.format(name=get_name_from_email(to_email))

        # Attach the personalized email body
        msg.attach(MIMEText(personalized_body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, to_email, msg.as_string())

        # Close the connection
        server.quit()

def get_name_from_email(email):
    # You can implement logic to extract the name from the email address
    # For simplicity, let's assume the part before the '@' symbol is the name
    return email.split('@')[0]

# Example usage
to_emails = ['example1@gmail.com', 'example2@gmail.com']
subject = "Hello from Email Automation"
body_template = "Hello {name},\n\nThis is a personalized email sent using Python."

email_automation(subject, body_template, to_emails)
