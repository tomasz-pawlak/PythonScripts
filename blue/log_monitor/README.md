# LogMonitor - Log Monitoring & Email Alert Tool

**LogMonitor** is a real-time log monitoring tool designed to detect suspicious events, such as failed login attempts, and send automatic email alerts for quick response.

This project is intended for simple SOC (Security Operations Center) systems and system administration purposes.

---

### Features

- Real-time log file monitoring (similar to `tail -f`)
- Detection of specific patterns, such as **"Failed password"**
- Automatic email notifications using SMTP
- Secure connection to the SMTP server via `SMTP_SSL`
- Easy configuration of SMTP server parameters
- Easily extendable to include other patterns or logs

---

### How to Run

```bash
python3 logmonitor.py \
  -f /var/log/auth.log \
  -ss smtp.example.com \
  --smtp-port 465 \
  -su your@email.com \
  -pw your_password \
  -r recipient@example.com
```
-------------------------------------------

# LogMonitor - Log Monitoring & Email Alert Tool

**LogMonitor** to narzędzie do monitorowania logów systemowych w czasie rzeczywistym. Skrypt umożliwia wykrywanie podejrzanych zdarzeń, takich jak nieudane próby logowania (Failed login attempts), oraz automatyczne wysyłanie powiadomień e-mail w celu szybkiej reakcji.

Projekt jest przeznaczony do prostych systemów SOC (Security Operations Center) oraz administracji systemowej.

---

### Funkcje

- Monitorowanie pliku logów w czasie rzeczywistym (podobnie jak `tail -f`)
- Wykrywanie specyficznych wzorców, takich jak **"Failed password"**
- Automatyczne wysyłanie powiadomień e-mail za pomocą SMTP
- Bezpieczne połączenie z serwerem SMTP za pomocą `SMTP_SSL`
- Łatwa konfiguracja parametrów serwera SMTP
- Możliwość łatwego rozszerzenia o inne wzorce lub logi

---

### Jak uruchomić

```bash
python3 logmonitor.py \
  -f /var/log/auth.log \
  -ss smtp.example.com \
  --smtp-port 465 \
  -su your@email.com \
  -pw your_password \
  -r recipient@example.com