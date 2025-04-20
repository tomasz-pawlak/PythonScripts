# VirusTotal Hash Checker

## This script allows you to:

    Calculate the hash of a local file or a file from a remote URL,

    Check the hash using the VirusTotal API,

    (Optionally) generate a detection report and save it to a text file.

## Requirements

    Python 3.x

    Installed Python packages:

pip install vt colorama requests

## Usage

python script.py [-f FILE_PATH | -u URL | -hs HASH] -k API_KEY [-ht {md5,sha1,sha256}] [-r]

Arguments
Argument	Description
-f, --file	Path to a local file
-u, --url	URL to the file to download
-hs, --hash	Hash string to check directly
-k, --key	VirusTotal API key (required)
-ht, --hash_type	Hash algorithm to use: md5, sha1, or sha256 (default: sha256)
-r, --report	Generate a text report: virustotal_report.txt
Examples

Check a local file using the default SHA256 hash:

python script.py -f file.exe -k YOUR_API_KEY

Check a file from a URL using MD5 and generate a report:

python script.py -u https://example.com/file.exe -ht md5 -k YOUR_API_KEY -r

Check an already known SHA256 hash:

python script.py -hs d2d2d2... -k YOUR_API_KEY

## How It Works

    The script supports local files or downloads files from URLs.

    It calculates a hash using the selected algorithm (md5, sha1, sha256).

    It queries the VirusTotal API to retrieve detection statistics.

    Optionally, it writes a report to virustotal_report.txt, including malicious, suspicious, and undetected counts.

Notes

    You must have a valid VirusTotal API key: https://www.virustotal.com

    Only one of the following options can be used at the same time: --file, --url, or --hash.

    If --report is specified, a report file will be saved in the current working directory.
-------------------------------------------
# VirusTotal Hash Checker

## Skrypt służy do:

    Obliczania skrótu (hasha) pliku lokalnego lub pliku pobranego z Internetu (URL),

    Sprawdzania tego hasha przy użyciu interfejsu API VirusTotal,

    (Opcjonalnie) generowania raportu detekcji do pliku tekstowego.

## Wymagania

    Python 3.x

    Zainstalowane biblioteki:

pip install vt colorama requests

## Sposób użycia

python script.py [-f ŚCIEŻKA_DO_PLIKU | -u URL | -hs HASH] -k API_KEY [-ht {md5,sha1,sha256}] [-r]

Argumenty
Argument	Opis
-f, --file	Ścieżka do lokalnego pliku
-u, --url	Adres URL do pliku do pobrania
-hs, --hash	Podany ręcznie hash do sprawdzenia
-k, --key	Klucz API do VirusTotal (wymagany)
-ht, --hash_type	Rodzaj hasha: md5, sha1, sha256 (domyślnie: sha256)
-r, --report	Zapisanie raportu do pliku virustotal_report.txt
Przykłady

Sprawdzenie lokalnego pliku (domyślnie SHA256):

python script.py -f plik.exe -k TWÓJ_API_KEY

Sprawdzenie pliku z URL, obliczenie hash MD5 i wygenerowanie raportu:

python script.py -u https://example.com/plik.exe -ht md5 -k TWÓJ_API_KEY -r

Sprawdzenie konkretnego hasha SHA256:

python script.py -hs d2d2d2... -k TWÓJ_API_KEY

## Działanie skryptu

    Skrypt może przetwarzać pliki lokalne lub zdalne (URL).

    Oblicza hash za pomocą wybranego algorytmu (md5, sha1, sha256).

    Wysyła zapytanie do VirusTotal w celu uzyskania informacji o wykryciu zagrożeń.

    (Opcjonalnie) Zapisuje raport w pliku virustotal_report.txt, zawierający liczbę wyników: malicious, suspicious, undetected.

Uwagi

    Klucz API do VirusTotal można uzyskać na stronie: https://www.virustotal.com

    Użycie opcji --report zapisze dane do pliku tekstowego w katalogu uruchomienia skryptu.

    Tylko jeden z argumentów --file, --url lub --hash może być użyty jednocześnie.