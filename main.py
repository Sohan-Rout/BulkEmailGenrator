import argparse
import csv
from email_sender import send_bulk_emails, send_bulk_certificates
from string import Template

def main():
    parser = argparse.ArgumentParser("Bulk Email & Certificate Sender", add_help=False)
    parser.add_argument(
        "--mode",
        choices=["Emails", "Certificates"],
        help="Choose 'Emails' to send bulk emails and 'Certificates' to attach certificates",
    )
    args = parser.parse_args()

    # Interactive menu if no mode is provided
    if not args.mode:
        print("Choose an option:")
        print("1. Send plain emails")
        print("2. Send emails with certificates")
        choice = input("Enter your choice [1/2]: ").strip()
        if choice == "1":
            args.mode = "Emails"
        elif choice == "2":
            args.mode = "Certificates"
        else:
            print("[*] Invalid choice. Exiting.")
            return

    recipients = []
    with open("data/email.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipients.append(row)

    with open("template/email.html", "r", encoding="utf-8") as f:
        template = Template(f.read())

    if args.mode == "Emails":
        send_bulk_emails(recipients, template)
    elif args.mode == "Certificates":
        send_bulk_certificates(recipients, template)

if __name__ == "__main__":
    main()