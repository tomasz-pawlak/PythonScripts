# EDR-lite: Lightweight Process and Folder Monitoring System

This script functions as a lightweight EDR (Endpoint Detection and Response) system, monitoring processes and directories in real time. When suspicious activity is detected, it sends an email alert and logs the event.

## Features

- Monitoring of suspicious processes (e.g., `powershell`, `wget`, `nc`)
- Watch for changes in temporary directories (`/tmp`, `C:\Windows\Temp`)
- Email notifications upon detecting incidents
- Automatic termination of suspicious processes (Windows/Linux)
- Event logging to `edr_alerts.log`
- Configuration via `.env` file
- Works on both Windows and Linux systems

## Used Libraries

- **`psutil`** – for monitoring and managing running system processes (e.g., listing or killing a process).
- **`watchdog`** – for detecting filesystem changes (file/folder creation, modification, deletion).
- **`smtplib` + `email.mime.text`** – for sending email alerts when suspicious activity is detected.
- **`dotenv`** – for securely loading configuration variables (e.g., SMTP credentials) from an external file.
- **`argparse`** – for preparing command-line options (currently unused but can be expanded).
- **`logging`** – for writing detailed logs about detected events.
- **`threading`** – to run process and folder monitoring simultaneously.

## Requirements

- Python 3.8 or newer
- Install required libraries:
  ```bash
  pip install psutil watchdog python-dotenv

## Project Files
```
├── edr_lite.py           # Main script
├── .env                  # Configuration file (excluded from repository)
├── edr_alerts.log        # Log file
├── README.md             # Documentation
```
## Running the Script

Fill in the .env file with appropriate values (SMTP server, login, password, recipient email), then run:

```
python edr_lite.py
```
## How It Works

   The script detects running processes from a predefined list of suspicious names and immediately terminates them.

   It monitors temporary folders for any changes (creation, modification, deletion).

   Alerts are sent via email, and all events are written to the edr_alerts.log file.

## Notes

   The list of suspicious processes and folders is system-dependent.

   The script can be extended to include log analysis, VirusTotal integration, or a web interface.

   Intended for educational and internal use only — not a replacement for a full-scale EDR solution.

-----------------------------------------------------------

# EDR-lite: Prosty system monitorowania procesów i folderów

Ten skrypt działa jako lekki system typu EDR (Endpoint Detection and Response), monitorując procesy i katalogi w czasie rzeczywistym. W przypadku wykrycia podejrzanej aktywności, wysyła alert e-mail oraz loguje zdarzenie.

## Funkcje

- Monitoring podejrzanych procesów (np. `powershell`, `wget`, `nc`)
- Nasłuch na zmiany w katalogach tymczasowych (`/tmp`, `C:\Windows\Temp`)
- Powiadomienia e-mail przy wykryciu incydentu
- Automatyczne kończenie podejrzanych procesów (Windows/Linux)
- Logowanie do pliku `edr_alerts.log`
- Obsługa konfiguracji przez plik `.env`
- Działa na systemach Windows i Linux

## Wykorzystywane biblioteki

- **`psutil`** – do monitorowania i kontrolowania procesów działających w systemie (np. pobieranie listy procesów, zabijanie procesu).
- **`watchdog`** – do śledzenia zmian w systemie plików (tworzenie, modyfikacja, usuwanie plików/katalogów).
- **`smtplib` + `email.mime.text`** – do wysyłania wiadomości e-mail z alertami o wykrytych zdarzeniach.
- **`dotenv`** – do bezpiecznego przechowywania danych konfiguracyjnych (np. dane SMTP) poza kodem źródłowym.
- **`argparse`** – do przygotowania opcji uruchomieniowych (obecnie pusta, ale można ją rozbudować).
- **`logging`** – do tworzenia pliku logów z informacjami o wykrytych zdarzeniach.
- **`threading`** – do równoległego uruchamiania monitorowania procesów i folderów.

## Wymagania

- Python 3.8 lub nowszy
- Instalacja wymaganych bibliotek:
  ```bash
  pip install psutil watchdog python-dotenv

Pliki projektu

```
├── edr_lite.py           # Główny skrypt
├── .env                  # Dane konfiguracyjne (pomijany w repozytorium)
├── edr_alerts.log        # Plik logów
├── README.md             # Dokumentacja
```
## Uruchomienie

Uzupełnij plik .env odpowiednimi danymi (SMTP serwera, login, hasło, odbiorca maila), a następnie uruchom:

```
python edr_lite.py
```
# Jak to działa

  Skrypt wykrywa działające procesy z listy podejrzanych i natychmiast je kończy.

  Monitoruje foldery tymczasowe, reagując na zmiany (tworzenie, modyfikacja, usunięcie).

  Wysyła e-maile z alertami oraz zapisuje wszystkie zdarzenia do logu edr_alerts.log.

# Uwagi

  Lista podejrzanych procesów oraz folderów różni się w zależności od systemu operacyjnego.

  Skrypt można rozbudować o analizę logów, integrację z VirusTotal, lub interfejs webowy.

  Projekt przeznaczony do nauki i wewnętrznego użytku – nie zastępuje pełnoprawnego EDR.