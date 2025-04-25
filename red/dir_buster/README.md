# Directory/Path Bruteforcer

This script performs a brute-force attack against a given URL to discover hidden directories or files. It mimics tools like DirBuster or gobuster using a wordlist to find valid HTTP paths.

## Features

- **Custom Status Code Filtering**: Choose which HTTP status codes (e.g. 200, 403) should be considered as valid hits.
- **Progress Indicator**: Displays progress in the format `X/Y` as it tests each path.
- **Wordlist Compatible**: Works with wordlists from SecLists and similar sources.
- **Handles Errors Gracefully**: Ignores timeout or connection errors to ensure smooth execution.

## Requirements

- Python 3.8 or higher
- `requests` library (`pip install requests`)

## Usage

```bash
python dir_bruteforce.py -u <base_url> -w <path_to_wordlist> [-c <valid_http_codes>]
```
Arguments

    -u, --url: Target URL (e.g., https://example.com)

    -w, --wordlist: Path to the wordlist file

    -c, --codes: Optional HTTP status codes to be treated as valid (default: 200 204 301 403)

## Examples

Scan a WordPress site with a wordlist:
```
python dir_bruteforce.py -u https://mywordpresssite.com -w /path/to/common.txt
```
Use custom status codes:
```
python dir_bruteforce.py -u https://site.com -w wordlist.txt -c 200 403
```
## How It Works

The script reads all lines from the wordlist.

Each word is appended to the base URL and sent as a request.

If the HTTP response matches a valid code, the path is printed.

Progress is shown in the format [123/5000].

## Notes

Wordlist must be a UTF-8 text file with one entry per line.

Large wordlists will take longer to process.

Use responsibly and only against targets you own or are authorized to test.

-----------------------------
# Bruteforcer Ścieżek/Katalogów

Ten skrypt wykonuje atak brute-force na wskazany URL, aby odnaleźć ukryte katalogi lub pliki. Działa podobnie do narzędzi takich jak DirBuster czy gobuster, wykorzystując plik wordlisty.
Funkcje

- **Filtrowanie kodów HTTP**: Możliwość określenia, które kody (np. 200, 403) są traktowane jako trafienia.

- **Licznik postępu**: Wyświetla postęp w formacie X/Y w czasie skanowania.

- **Zgodność z wordlistami**: Współpracuje z popularnymi listami z SecLists i podobnych źródeł.

- **Obsługa błędów**: Ignoruje błędy połączenia lub timeouty.

## Wymagania

- **Python 3.8 lub wyższy**

- **Biblioteka requests (pip install requests)**

## Użycie
```
python dir_bruteforce.py -u <url_bazowy> -w <ścieżka_do_wordlisty> [-c <kody_HTTP>]
```
## Argumenty

    -u, --url: URL bazowy, np. https://example.com

    -w, --wordlist: Ścieżka do pliku wordlisty

    -c, --codes: (Opcjonalne) Kody HTTP traktowane jako trafienia (domyślnie: 200 204 301 403)

## Przykłady

Skanowanie strony WordPress:
```
python dir_bruteforce.py -u https://mojastrona.pl -w /ścieżka/common.txt
```
Użycie własnych kodów:
```
python dir_bruteforce.py -u https://strona.pl -w wordlist.txt -c 200 403
```
## Jak to działa

Skrypt wczytuje wszystkie linie z wordlisty.

Do każdego słowa dopisuje / i wysyła żądanie.

Jeśli kod HTTP jest zgodny z zaakceptowanymi, ścieżka zostaje wypisana.

Postęp wyświetlany jest jako [123/5000].

## Uwagi

Wordlista powinna być zakodowana w UTF-8 i zawierać jeden wpis na linię.

Dla dużych wordlist czas działania może być długi.

Używaj tylko na legalnych celach, które należą do Ciebie lub masz na nie zgodę.