import argparse
import platform
import smtplib
import os
import threading
import time
from dotenv import load_dotenv
import logging
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from email.mime.text import MIMEText

load_dotenv(".env.example")

parser = argparse.ArgumentParser(description="")
args = parser.parse_args()

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT", "465"))
smtp_username = os.getenv("SMTP_USERNAME")
smtp_password = os.getenv("SMTP_PASSWORD")
email_receiver = os.getenv("EMAIL_RECEIVER")


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
        msg['From'] = f'SOC team <{smtp_username}>'
        msg['To'] = email_receiver

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, email_receiver, msg.as_string())

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
        time.sleep(2)

class FolderHandler(FileSystemEventHandler):
    def process(self, event, action):
        msg = f"[Folder] {action} {event.src_path}"
        logging.warning(msg)
        send_email("Alert", msg)

    def on_created(self, event):
        self.process(event, "created")

    def on_modified(self, event):
        self.process(event, "Modified")

    def on_deleted(self, event):
        self.process(event, "Deleted")

def monitor_directories():
    logging.info("Monitoring directories...")
    event_handler = FolderHandler()
    observer = Observer()

    for path in monitored_dirs:
        if os.path.exists(path):
            observer.schedule(event_handler, path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    t1 = threading.Thread(target=monitor_processes, daemon=True)
    t2 = threading.Thread(target=monitor_directories, daemon=True)

    t1.start()
    t2.start()

    logging.info("System EDR-lite is working...")
    while True:
        time.sleep(60)