# Bulk Email Sender

A simple Python tool for sending personalized bulk emails using a CSV contact list and a template. Supports Gmail and other SMTP services with customizable fields.

## Features
- Send personalized emails to a list of recipients from a CSV file.
- Use template files with dynamic variables (e.g., `{name}`).
- Supports Gmail and custom SMTP servers.
- Interactive menu or command-line mode selection.
- Handles HTML and plain text emails.

## Requirements
- Python 3.8 or newer
- pip (Python package manager)

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/bulkEmailSenderRepo.git
   cd bulkEmailSenderRepo
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**
   - Copy the example environment file and edit it:
     ```sh
     cp .env.example .env
     ```
   - Open `.env` and set your email credentials and SMTP settings.

## Usage
You can run the script in interactive menu mode or specify a mode via command line:

**Interactive menu:**
```sh
python3 main.py
```

**Direct mode (e.g., send):**
```sh
python3 main.py --mode send
```

## CSV and Template Format Examples
### CSV Contacts Example
```csv
email,name
sohan@example.com,Sohan
neshka@example.com,Neshka
```

### Email Template Example
```html
Hello {name},

Welcome to {company}. We're glad to have you on board!
```

## Troubleshooting
- **SSL Issues:** By default, the script will fall back to an unverified SSL context if SSL certificate verification fails, so you generally do not need to manually fix SSL issues.
- **Gmail Users:** If using Gmail, you need to [generate an App Password](https://support.google.com/accounts/answer/185833) and use it in your `.env` file. Regular account passwords will not work with "Less secure app access" disabled.

## License
MIT License (see `LICENSE` file for details).