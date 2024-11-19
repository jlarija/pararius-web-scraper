import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Email configuration
    from_email = "<INSERT YOUR EMAIL>"  # Your email
    from_password = "sdsq qlhh lveq oapw"  # Your email password (use app password if 2FA enabled)
    
    # Set up the SMTP server (for Gmail in this case)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create message container
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Add body to email
    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

 # Predefined fixed email content
subject = "New House Listings Alert"
body = """
Hi,
There are new house listings available on Pararius that match your search criteria. 
Best regards,
Pararius Web Scraper
"""
