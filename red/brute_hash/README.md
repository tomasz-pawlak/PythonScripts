# Brute-Force Hash Cracker

This script attempts to crack a given hash using a brute-force attack, leveraging a password list (wordlist). It supports the most common hashing algorithms: MD5, SHA1, SHA256, and SHA512.

## Features

- **Multiple Hash Algorithm Support**: Choose from four supported algorithms: `md5`, `sha1`, `sha256`, `sha512`.
- **Compatible with Popular Wordlists**: The script reads passwords from a text-based wordlist (e.g., `rockyou.txt`).
- **Encoding Error Handling**: Skips lines with invalid characters that can't be decoded (e.g., due to encoding issues).
- **Simple CLI Usage**: Easy to use with intuitive command-line arguments.

## Requirements

- Python 3.8 or higher
- Standard Python library (no external dependencies)

## Usage

To run the script, use the following syntax:

```bash
python brute_hash.py -p <hash_to_crack> -w <path_to_wordlist> -a <algorithm>
````
## Examples

Crack a SHA256 hash using a wordlist:
```
python brute_hash.py -p 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 \
-w /path/to/rockyou.txt -a sha256
```
Use the default algorithm (sha512):
```
python brute_hash.py -p <hash> -w <path_to_wordlist>
```
## How It Works

The script reads all lines from the provided wordlist file.

For each password, it generates a hash using the selected algorithm.

It compares the generated hash with the user-provided hash.

If a match is found, it prints the original password.

If no match is found, it continues until the end of the list.

If no password matches, the script will notify you.

## Notes

Make sure your wordlist file is in plain text format and UTF-8 encoded.

Processing large wordlists may take significant time.

----------------------------------------

# Brute-Force Hash Cracker

Skrypt ten próbuje złamać podany hash metodą brute-force, wykorzystując plik z listą haseł (wordlist). Obsługuje najpopularniejsze algorytmy skrótu: MD5, SHA1, SHA256 i SHA512.

## Funkcje

- **Obsługa wielu algorytmów**: Możliwość wyboru jednego z czterech algorytmów: `md5`, `sha1`, `sha256`, `sha512`.
- **Zgodność z popularnymi wordlistami**: Skrypt czyta listę haseł z pliku tekstowego, np. `rockyou.txt`.
- **Ignorowanie błędów kodowania**: Skrypt pomija błędy związane z nieprawidłowymi znakami w wordliście.
- **Prosta składnia uruchamiania**: Intuicyjne argumenty wiersza poleceń.

## Wymagania

- Python 3.8 lub wyższy
- Standardowa biblioteka Pythona (brak zewnętrznych zależności)

## Użycie

Aby uruchomić skrypt, użyj następującej składni:

```bash
python brute_hash.py -p <hash_do_złamania> -w <ścieżka_do_wordlisty> -a <algorytm>
```
## Przykłady

Złamanie hasha SHA256 z wykorzystaniem wordlisty:

``` 
   python brute_hash.py -p 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 \
   -w /ścieżka/do/rockyou.txt -a sha256
```
Użycie domyślnego algorytmu (sha512):

python brute_hash.py -p <hash> -w <ścieżka_do_wordlisty>

## Jak to działa

Skrypt odczytuje wszystkie linie z pliku wordlisty.

Dla każdego hasła generuje hash z wybranego algorytmu.

Porównuje wygenerowany hash z wartością podaną przez użytkownika.

Jeśli nastąpi dopasowanie – wypisuje hasło.

W przeciwnym razie – kontynuuje do końca listy.

W przypadku braku dopasowania, skrypt poinformuje o niepowodzeniu.

## Uwagi

Upewnij się, że plik wordlisty jest zapisany w formacie tekstowym i kodowany jako UTF-8.

Dla bardzo dużych wordlist proces może zająć więcej czasu.