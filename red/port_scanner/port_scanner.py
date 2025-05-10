import socket
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
parser.add_argument("-p", "--ports", help="Ports to scan, e.g., 22,80,443 or 20-100", default="80,443")
parser.add_argument("--timeout", type=float, default=0.5, help="Timeout for each port in seconds (default: 0.5)")

args = parser.parse_args()

def scan_ports(target, ports, timeout):
    print(f'Scanning {target}...\n')
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f'Port {port} is open')
            else:
                print(f'Port {port} is closed')


def port_range(port_range):
    try:
        start, end = map(int, port_range.split('-'))
        return list(range(start, end + 1))
    except:
        raise argparse.ArgumentTypeError("Port range must be in format START-END (e.g. 20-100)")




if "-" in args.ports:
    ports = port_range(args.ports)
else:
    ports = [int(p.strip()) for p in args.ports.split(",")]

start_time = datetime.now()

scan_ports(args.target, ports, args.timeout)
end_time = datetime.now()
print(f"\n[i] Scan completed in {end_time - start_time}")
