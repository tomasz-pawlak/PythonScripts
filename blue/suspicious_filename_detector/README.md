# Detect Suspicious Filenames

This script scans a specified directory to detect suspicious filenames that could potentially be harmful. It looks for files with certain extensions, hidden files, files with double extensions, and filenames containing suspicious keywords commonly associated with malicious files.

## Features

- **Extension Checks**: The script scans for files with certain extensions that are commonly associated with executable or malicious files (e.g., `.exe`, `.js`, `.vbs`, `.bat`, `.cmd`).
- **Hidden Files**: It detects hidden files based on operating system-specific attributes.
- **Double Extensions**: The script identifies files that have more than one extension (e.g., `file.txt.exe`).
- **Suspicious Keywords**: It flags files with names that contain suspicious keywords such as "invoice", "password", "login", "bank", or "report".

## Requirements

- Python 3.8 or higher
- Standard Python library (no external dependencies)

## Usage

To use the script, run the following command:

```bash
python detect_suspicious_filenames.py -d <directory_path>
```
Where <directory_path> is the path of the directory you want to scan. By default, the current directory is scanned if no directory is provided.
Example

To scan the current directory:

    python detect_suspicious_filenames.py

To scan a specific directory:

    python detect_suspicious_filenames.py -d /path/to/directory

## How It Works

The script recursively scans all files in the specified directory.

    It checks each file against the following criteria:

        File extension is suspicious (e.g., .exe, .bat, .js).

        File contains keywords that suggest potential malicious intent.

        File is hidden (on Windows systems, files with the hidden attribute are flagged).

        File has double extensions (e.g., file.txt.exe).

Suspicious files are printed to the console.

---------------------------------------
# Wykrywanie podejrzanych nazw plików

Skrypt ten skanuje określony katalog w poszukiwaniu podejrzanych nazw plików, które mogą być potencjalnie niebezpieczne. Sprawdza pliki z określonymi rozszerzeniami, pliki ukryte, pliki z podwójnymi rozszerzeniami oraz nazwy plików zawierające podejrzane słowa kluczowe, które są często związane z plikami złośliwymi.

## Funkcje

- **Sprawdzanie rozszerzeń**: Skrypt skanuje pliki z rozszerzeniami, które są często związane z plikami wykonywalnymi lub złośliwymi (np. `.exe`, `.js`, `.vbs`, `.bat`, `.cmd`).
- **Pliki ukryte**: Wykrywa pliki ukryte na podstawie atrybutów specyficznych dla systemu operacyjnego.
- **Podwójne rozszerzenia**: Skrypt identyfikuje pliki, które mają więcej niż jedno rozszerzenie (np. `plik.txt.exe`).
- **Podejrzane słowa kluczowe**: Flagi pliki, których nazwy zawierają podejrzane słowa kluczowe, takie jak "invoice", "password", "login", "bank", czy "report".

## Wymagania

- Python 3.8 lub wyższy
- Standardowa biblioteka Pythona (brak zewnętrznych zależności)

## Użycie

Aby użyć skryptu, uruchom następującą komendę:

```bash
python detect_suspicious_filenames.py -d <ścieżka_do_katalogu>
```
Gdzie <ścieżka_do_katalogu> to ścieżka do katalogu, który chcesz przeskanować. Domyślnie, jeśli nie podasz katalogu, skrypt przeskanuje bieżący katalog.
Przykład

Aby przeskanować bieżący katalog:

    python detect_suspicious_filenames.py

Aby przeskanować konkretny katalog:

    python detect_suspicious_filenames.py -d /ścieżka/do/katalogu

## Jak to działa

Skrypt rekurencyjnie skanuje wszystkie pliki w podanym katalogu.

    Sprawdza każdy plik pod kątem następujących kryteriów:

        Rozszerzenie pliku jest podejrzane (np. .exe, .bat, .js).

        Nazwa pliku zawiera słowa kluczowe sugerujące potencjalne złośliwe działanie.

        Plik jest ukryty (na systemach Windows pliki z atrybutem hidden są flagowane).

        Plik ma podwójne rozszerzenie (np. plik.txt.exe).

Podejrzane pliki są wypisywane w konsoli.