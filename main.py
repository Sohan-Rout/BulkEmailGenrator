import argparse
import csv
from email_sender import send_bulk_emails, send_bulk_certificates

def main():
    parser = argparse.ArgumentParser("Bulk Email & Certificate Sender")
    parser.add_argument(
        "--mode",
        choices=["Emails", "Certificates"],
        required=True,
        help="Choose 'Emails' to send bulk emails and 'Certificates' to attach certificates",
    )
    args = parser.parse_args()
    
    recipients = []
    with open("data/emails.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipients.append(row)
            
    with open("template/email.html", "r", encoding="utf-8") as f:
        template = f.read
        
    if args.mode == "Emails":
        send_bulk_emails(recipients, template)
    elif args.mode == "Certificates":
        send_bulk_certificates(recipients, template)
        
if __name__ == "__main__":
    main()