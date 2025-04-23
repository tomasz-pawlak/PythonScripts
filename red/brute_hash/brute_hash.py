import argparse
import hashlib

from pathlib import Path

parser = argparse.ArgumentParser(description='Brute-force hash cracker')

parser.add_argument('-p', '--password', help='Password to crack')
parser.add_argument("-a", '--hash_algorithm',
                    help='Hash algorithm used (default: sha512)',
                    choices=['md5', 'sha1', 'sha256', 'sha512'], default='sha512')
parser.add_argument('-w', '--wordlist', type=Path, help='Wordlist file for brute-force')
args = parser.parse_args()


def generate_hash(source, hash_algorithm):
    source_bytes = source.encode()
    if hash_algorithm == 'md5':
        return hashlib.md5(source_bytes).hexdigest()
    elif hash_algorithm == 'sha1':
        return hashlib.sha1(source_bytes).hexdigest()
    elif hash_algorithm == 'sha256':
        return hashlib.sha256(source_bytes).hexdigest()
    elif hash_algorithm == 'sha512':
        return hashlib.sha512(source_bytes).hexdigest()
    else:
        return ValueError('Unknown hash algorithm')


def brute_force_attack(password, hash_algorithm, wordlist: Path):
    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                if generate_hash(word, hash_algorithm) == password:
                    print(f'Found password: {word}')
                    return word
        print('No password found')
    except FileNotFoundError:
        print(f'Error: Wordlist file {wordlist} not found')
    except Exception as error:
        print(f"Error occured: {error}")


brute_force_attack(args.password, args.hash_algorithm, args.wordlist)
