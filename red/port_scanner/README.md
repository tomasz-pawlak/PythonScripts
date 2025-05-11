# Live Port Scanner

This script performs a simple TCP port scan on a specified target. It supports single ports, multiple ports, or entire
port ranges. Results are displayed in real-time.

## Features

- **Live Feedback**: Shows open ports as they are found.
- **Port Range or List Support**: Accepts single ports, comma-separated lists (e.g. `22,80,443`), or ranges (e.g.
  `20-100`).
- **Custom Timeout**: Adjustable timeout value for each connection attempt.
- **Cross-platform**: Works on Linux, macOS, and Windows (Python-based).

## Requirements

- Python 3.8 or higher
- No external dependencies (uses only Python standard library)

## Usage

```bash
python port_scanner.py -t <target_ip_or_host> -p <ports> [--timeout <seconds>]
```

Parameters

    -t, --target – Target IP or hostname to scan (e.g. 127.0.0.1 or example.com)

    -p, --ports – Ports to scan. You can specify:

        A single port: 80

        Multiple ports: 22,80,443

        A range: 20-100

    --timeout – Timeout in seconds per port (default: 0.5)

## Examples

Scan default ports 80 and 443:

```
python port_scanner.py -t example.com
```

Scan a specific list of ports:

```
python port_scanner.py -t 192.168.1.1 -p 21,22,23,80
```

Scan a full range with increased timeout:

```
python port_scanner.py -t 192.168.0.10 -p 1-1024 --timeout 1
```

## How It Works

Parses the target and port options using argparse.

For each port, it attempts a TCP connection using socket.

If the connection succeeds (connect_ex returns 0), the port is considered open.

Results are printed immediately for each scanned port.

## Notes

This is a basic scanner — no stealth techniques (like SYN scan).

Use responsibly and only on systems you own or have permission to scan.

Large port ranges will take more time, especially with longer timeouts.

---------------------------------------------------------

# Live Port Scanner

Ten skrypt wykonuje prosty skan portów TCP na wskazanym celu. Obsługuje pojedyncze porty, wiele portów oraz całe
zakresy. Wyniki są wyświetlane na bieżąco.

## Funkcje

- **Bieżące informacje zwrotne**: Pokazuje otwarte porty w czasie rzeczywistym.
- **Obsługa zakresów i list portów**: Akceptuje pojedyncze porty, listy oddzielone przecinkami (np. `22,80,443`) lub
  zakresy (np. `20-100`).
- **Dostosowywany timeout**: Możliwość ustawienia czasu oczekiwania na odpowiedź dla każdego portu.
- **Wieloplatformowość**: Działa na Linuxie, macOS i Windowsie (napisany w Pythonie).

## Wymagania

- Python 3.8 lub wyższy
- Brak zewnętrznych zależności (wykorzystuje tylko standardową bibliotekę Pythona)

## Użycie

```bash
python port_scanner.py -t <adres_ip_lub_host> -p <porty> [--timeout <sekundy>]
```

Parametry

    -t, --target – Docelowy adres IP lub nazwa hosta do skanowania (np. 127.0.0.1 lub example.com)

    -p, --ports – Porty do przeskanowania. Można podać:

        Jeden port: 80

        Wiele portów: 22,80,443

        Zakres: 20-100

    --timeout – Czas oczekiwania w sekundach dla każdego portu (domyślnie: 0.5)

### Przykłady

Skanowanie domyślnych portów 80 i 443:

```
python port_scanner.py -t example.com
```

Skanowanie konkretnych portów:

```
python port_scanner.py -t 192.168.1.1 -p 21,22,23,80
```

Skanowanie pełnego zakresu z dłuższym timeoutem:

python port_scanner.py -t 192.168.0.10 -p 1-1024 --timeout 1

## Jak to działa

Skrypt przetwarza podane opcje celu i portów za pomocą argparse.

Dla każdego portu próbuje nawiązać połączenie TCP przy użyciu socket.

Jeśli połączenie się powiedzie (connect_ex zwróci 0), port jest uznany za otwarty.

Wyniki są drukowane na bieżąco w konsoli.

## Uwagi

To prosty skaner — nie używa technik ukrytych (takich jak SYN scan).

Używaj odpowiedzialnie i tylko na systemach, do których masz prawo dostępu.

Skanowanie dużych zakresów portów może potrwać dłużej, szczególnie przy większym timeoutcie.