import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# AWS SES SMTP credentials
SMTP_USERNAME = "AWS_SECRET_ID"      # Your AWS_SECRET_ID
SMTP_PASSWORD = "AWS_SECRET_KEY"     # Your AWS_SECRET_KEY
REGION = "REGION"                    # SMTP REGION
SMTP_SERVER = f"email-smtp.{REGION}.amazonaws.com" 
SMTP_PORT = 587

#Mail Details
SENDER = "FROM_MAIL_ID"
RECIPIENTS = ["TO_MAIL_ID1", "TO_MAIL_ID2", "TO_MAIL_ID3"]
SUBJECT = "Test Email from AWS SES via SMTP"
BODY_TEXT = "This is a test email sent through AWS SES SMTP using Python."
BODY_HTML = """<html>
<head></head>
<body>
  <p>This is a test email sent through <b>AWS SES SMTP</b> using Python.</p>
</body>
</html>"""

msg = MIMEMultipart('alternative')
msg['Subject'] = SUBJECT
msg['From'] = SENDER
msg['To'] = ", ".join(RECIPIENTS)

part1 = MIMEText(BODY_TEXT, 'plain')
part2 = MIMEText(BODY_HTML, 'html')

msg.attach(part1)
msg.attach(part2)

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo() 
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(SENDER, RECIPIENTS, msg.as_string())
    print(f"Email sent to {', '.join(RECIPIENTS)}!")
    server.quit()

except Exception as e:
    print(f"Error: {e}")
