import smtplib
import ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SUBJECT = os.getenv("SUBJECT", "Add your subject in env file")


def create_message(sender, recipient, subject, body, attachment_path=None):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject

    # Add plain-text fallback
    msg.set_content("Your email client does not support HTML emails.")

    # Add the HTML version
    msg.add_alternative(body, subtype="html")

    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    return msg


def send_email(message):
    """Send a single email via Gmail SMTP"""
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)
            server.send_message(message)
    except ssl.SSLError:
        print("⚠️ SSL verification failed, falling back to unverified context.")
        context = ssl._create_unverified_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(EMAIL, PASSWORD)
            server.send_message(message)


def send_bulk_emails(recipients, template):
    """Send bulk plain emails (no attachments)"""
    for recipient in recipients:
        name = recipient["name"]
        email = recipient["email"]

        # custom email body
        body = template.substitute(name=name)

        msg = create_message(
            sender=EMAIL,
            recipient=email,
            subject=SUBJECT,
            body=body,
        )

        try:
            send_email(msg)
            print(f"[+] Email sent to {name} - ({email})")
        except Exception as e:
            print(f"[-] Failed to send {name} - ({email}) : {e}")


def send_bulk_certificates(recipients, template):
    """Send bulk emails with certificates attached"""
    for recipient in recipients:
        name = recipient["name"]
        email = recipient["email"]

        body = template.substitute(name=name)

        # Certificate file has the same name as participant
        cert_file = f"{name}.pdf"
        attachment_path = os.path.join("data", "certificates", cert_file)

        msg = create_message(
            sender=EMAIL,
            recipient=email,
            subject=SUBJECT,
            body=body,
            attachment_path=attachment_path,
        )

        try:
            send_email(msg)
            print(f"[+] Email sent to {name} - ({email})")
        except Exception as e:
            print(f"[-] Failed to send {name} - ({email}) : {e}")
