import hashlib
import requests
import vt
import argparse
from colorama import Fore


def get_hash_from_file(file_path, hash_type):
    hash_func = getattr(hashlib, hash_type)()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_func.update(byte_block)

    if args.report:
        try:
            print("generating report to file...")
            generate_report(hash_func.hexdigest())
        except Exception as e:
            pass

    print("-----------------------------")
    print(str(hash_func.hexdigest()))
    return hash_func.hexdigest()


def get_hash_from_url(url, hash_type):
    hash_func = getattr(hashlib, hash_type)()
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        print(f"Failed to retrieve file from URL. Status code: {response.status_code}")
        return None

    for byte_block in response.iter_content(4096):
        hash_func.update(byte_block)

    if args.report:
        try:
            print("generating report to file...")
            generate_report(hash_func.hexdigest())
        except Exception as e:
            pass

    return hash_func.hexdigest()


def generate_report(hash_calculated):
    filex = client.get_object(f"/files/{hash_calculated}")
    with open("virustotal_report.txt", "w") as f:
        f.write(f"Report for hash: {hash_calculated}\n")
        f.write("[INFO] Detection ratios:\n")
        f.write(f"  Malicious: {filex.last_analysis_stats['malicious']}\n")
        f.write(f"  Suspicious: {filex.last_analysis_stats['suspicious']}\n")
        f.write(f"  Undetected: {filex.last_analysis_stats['undetected']}\n")


parser = argparse.ArgumentParser(description="VirusTotal hash checker")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", help="Path to file")
group.add_argument("-hs", "--hash", help="Hash to check")
group.add_argument("-u", "--url", help="url to check")
parser.add_argument("-ht", "--hash_type", choices=["md5", "sha1", "sha256"], default="sha256",
                    help="Hash type to use for file (default: sha256)")
parser.add_argument("-k", "--key", type=str, required=True, help="VirusTotal API key")
parser.add_argument("-r", "--report", action="store_true", help="Outputs report of scanned file/hash")

args = parser.parse_args()
client = vt.Client(args.key)
hash_value = ""

if args.file:
    hash_value = get_hash_from_file(args.file, args.hash_type)
    print(Fore.CYAN + f"[INFO] {args.hash_type} from file: {hash_value}")
elif args.hash:
    hash_value = args.hash
    if args.report:
        try:
            generate_report(hash_value)
        except Exception as e:
            pass
    print(Fore.CYAN + f"[INFO] Using provided hash: {hash_value}")
elif args.url:
    hash_value = get_hash_from_url(args.url, args.hash_type)
    print(Fore.CYAN + f"[INFO] Using provided hash from url: {hash_value}")

try:
    file = client.get_object(f"/files/{hash_value}")
    print(Fore.RED + "[INFO] Detection ratios:")
    print(f"  Malicious: {file.last_analysis_stats['malicious']}")
    print(f"  Suspicious: {file.last_analysis_stats['suspicious']}")
    print(f"  Undetected: {file.last_analysis_stats['undetected']}")
except vt.error.APIError as e:
    print("We currently don't have any comments that fit your search")
finally:
    client.close()
