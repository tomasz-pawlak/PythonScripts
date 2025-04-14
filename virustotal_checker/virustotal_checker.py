import hashlib
import vt
from colorama import Fore
import argparse


def get_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


parser = argparse.ArgumentParser(description="VirusTotal hash checker")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", help="Path to file")
group.add_argument("-hs", "--hash", help="Hash to check")
parser.add_argument("-k", "--key", type=str, required=True, help="VirusTotal API key")

args = parser.parse_args()
client = vt.Client(args.key)

if args.file:
    sha256 = get_sha256(args.file)
    print(Fore.CYAN + f"[INFO] SHA256 from file: {sha256}")
else:
    sha256 = args.hash
    print(Fore.CYAN + f"[INFO] Using provided hash: {sha256}")

try:
    file = client.get_object(f"/files/{sha256}")
    print(Fore.RED + f"{file.last_analysis_stats}")
except vt.error.APIError as e:
    print("We currently don't have any comments that fit your search")
finally:
    client.close()
