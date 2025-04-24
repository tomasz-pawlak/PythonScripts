import argparse
import requests
from pathlib import Path

parser = argparse.ArgumentParser(description='Directory/Path Bruteforcer (like DirBuster)')

parser.add_argument("-u", "--url", required=True, type=str, help='Base URL to scan (e.g., https://example.com)')
parser.add_argument("-w", "--wordlist", type=Path, required=True, help="Wordlist file for brute-force")
parser.add_argument("-c", "--codes", type=int, nargs='*', default=[200, 204, 301, 403],
                    help='HTTP status codes to consider as valid (default: 200, 204, 301, 403)')
args = parser.parse_args()


def brute_force(base_url, wordlist_path, accepted_codes):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                path = line.strip()
                url = base_url + path
                try:
                    response = requests.get(url, timeout=5)
                    if response.status_code in accepted_codes:
                        print(f'Found {url}. Status code: {response.status_code}')
                except requests.RequestException as error:
                    print(f'Error accessing {url}: {error}')


    except FileNotFoundError:
        print(f'Error: Wordlist file {wordlist_path} not found')
    except Exception as error:
        print(f"Error occured: {error}")

brute_force(args.url, args.wordlist, args.codes)