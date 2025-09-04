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