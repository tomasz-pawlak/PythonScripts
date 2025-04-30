import argparse
import platform
import smtplib
import os
import time
from dotenv import load_dotenv
import logging
import psutil
from email.mime.text import MIMEText

load_dotenv(".env.example")

parser = argparse.ArgumentParser(description="")
parser.add_argument("-ss", "--smtp-server", required=True, help="SMTP server address")
parser.add_argument("--sp", "--smtp-port", type=int, default=465, help="SMTP server port (default: 465)")
parser.add_argument("-u", "--smtp-username", required=True, help="SMTP username")
parser.add_argument("-up", "--smtp-password", required=True, help="SMTP password")
parser.add_argument("-r", "--receiver", required=True, help="Receiver email address")

args = parser.parse_args()

logging.basicConfig(filename='edr_alerts.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

system = platform.system()

if system == "Windows":
    suspicious_processes = ["powershell.exe", "cmd.exe", "certutil.exe", "wget.exe"]
    monitored_dirs = ["C:\\Windows\\Temp"]
elif system == "Linux":
    suspicious_processes = ["nc", "bash", "wget", "curl"]
    monitored_dirs = ["/tmp"]
else:
    suspicious_processes = []
    monitored_dirs = []


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


def monitor_processes():
    logging.info("Monitoring processes...")
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                proc_name = proc.info['name'].lower()
                if proc_name in suspicious_processes:
                    msg = f"[Process] Suspicious process: {proc_name} (PID: {proc.pid})"
                    logging.warning(msg)
                    send_email("Alert", msg)
                    os.kill(proc.pid, 9)
                    logging.info(f"Proces {proc_name} (PID: {proc.pid}) terminated")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        time.sleep(5)

monitor_processes()