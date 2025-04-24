import argparse
import requests
from pathlib import Path

parser = argparse.ArgumentParser(description='Directory/Path Bruteforcer (like DirBuster)')

parser.add_argument("-u", "--url", required=True, type=str, help='Base URL to scan (e.g., https://example.com)')
parser.add_argument("-w", "--wordlist", type=Path, required=True, help="Wordlist file for brute-force")
parser.add_argument("-c", "--codes", type=int, nargs='*', default=[200, 204, 301, 403],
                    help='HTTP status codes to consider as valid (default: 200, 204, 301, 403)')
args = parser.parse_args()

