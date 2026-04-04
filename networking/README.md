# 🌐 Networking

> You can't hack what you can't understand. Know the network.

This section covers network fundamentals from a security perspective — TCP/IP stack, packet analysis, port scanning, service enumeration, DNS, ARP, and traffic interception.

---

## Topics

- OSI model and TCP/IP in practice
- Subnetting and CIDR notation
- Port scanning and service fingerprinting with `nmap`
- Packet capture and analysis with `Wireshark` and `tcpdump`
- Netcat for port listening, file transfer, and reverse shells
- ARP, DNS, and ICMP — protocol-level understanding
- Network reconnaissance methodology

---

## Daily Logs

| Day | Focus | File |
|-----|-------|------|
| 001 | Nmap scanning techniques | [day-001.md](logs/day-001.md) |
| 002 | Packet capture with tcpdump & Wireshark | [day-002.md](logs/day-002.md) |

---

## Key Commands Quick Reference

```bash
# SYN scan with service/version detection
nmap -sS -sV -O -p- 192.168.1.0/24

# Top 1000 ports with scripts
nmap -sC -sV -oN output.txt 10.10.10.1

# Capture packets on interface
tcpdump -i eth0 -w capture.pcap

# Capture only HTTP traffic
tcpdump -i eth0 port 80 -A

# Listen on a port (netcat)
nc -lvnp 4444

# Connect to a port
nc 10.10.10.1 80
```
