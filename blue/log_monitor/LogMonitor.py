import argparse
import smtplib
import time
from email.mime.text import MIMEText

parser = argparse.ArgumentParser(description="LogMonitor - A tool to monitor log files in real-time and send email alerts for suspicious activities.")
parser.add_argument("-f", "--filename", required=True, help="Path to log file")
parser.add_argument("-ss", "--smtp-server", required=True, help="SMTP server address")
parser.add_argument("--sp", "--smtp-port", type=int, default=465, help="SMTP server port (default: 465)")
parser.add_argument("-u", "--smtp-username", required=True, help="SMTP username")
parser.add_argument("-up", "--smtp-password", required=True, help="SMTP password")
parser.add_argument("-r", "--receiver", required=True, help="Receiver email address")

args = parser.parse_args()
filename = args.filename

def send_email(subject, body):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = f'SOC team <{args.smtp_username}>'
        msg['To'] = args.receiver

        server = smtplib.SMTP_SSL(args.smtp_server, args.sp)
        server.login(args.smtp_username, args.smtp_password)
        server.sendmail(args.smtp_username, args.receiver, msg.as_string())

        print("Email sent successfully")
        server.quit()

    except Exception as e:
        print(f"Error sending email: {e}")


def scan_file(file):
    with open(filename, "r") as f:
        f.seek(0, 2)

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            if "Failed".lower() in line.lower():
                print(f"Alert found: {line.lower()}")
                send_email("Alert found", line)

print(f"Started active scanning: {filename}")

scan_file(filename)
