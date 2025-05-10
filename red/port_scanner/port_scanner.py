import argparse

def scan_ports(target, ports, timeout):
    pass


def port_range(port_range):
    pass

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
parser.add_argument("-p", "--ports", help="Ports to scan, e.g., 22,80,443 or 20-100", default="80,443")
parser.add_argument("--timeout", type=float, default=0.5, help="Timeout for each port in seconds (default: 0.5)")

args = parser.parse_args()
