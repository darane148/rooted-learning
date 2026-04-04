#!/usr/bin/env python3
"""
port_scanner.py — A simple multi-threaded TCP port scanner
Usage: python3 port_scanner.py <host> <start_port> <end_port>

Built as part of the 'From Zero to Root' cybersecurity learning journey.
For educational use in authorized lab environments only.
"""

import socket
import sys
import threading
from datetime import datetime

open_ports = []
lock = threading.Lock()


def scan_port(host: str, port: int) -> None:
    """Attempt a TCP connection to host:port. Record and print if open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "unknown"

            with lock:
                open_ports.append(port)
                print(f"  [+] Port {port:5d}/tcp  OPEN  ({service})")

    except socket.error:
        pass


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <host> <start_port> <end_port>")
        sys.exit(1)

    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"[-] Cannot resolve host: {host}")
        sys.exit(1)

    print("-" * 50)
    print(f"Scanning target: {host} ({target_ip})")
    print(f"Port range:      {start_port} - {end_port}")
    print(f"Started at:      {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    print("-" * 50)
    print(f"Scan complete. {len(open_ports)} open port(s) found.")
    if open_ports:
        print(f"Open ports: {sorted(open_ports)}")


if __name__ == "__main__":
    main()
