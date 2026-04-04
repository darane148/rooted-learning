# 🐍 Python for Security

> If you can script it, you can automate it. If you can automate it, you can scale it.

This section covers Python scripting specifically for security use cases — port scanners, exploit automation, network tools, web scrapers, and payload generators.

---

## Topics

- Socket programming and raw TCP/UDP connections
- Building a port scanner from scratch
- HTTP requests with the `requests` library
- Automating web vulnerability checks
- Writing Netcat-style tools in Python
- Password spraying and brute-force scripts
- Parsing and manipulating data (JSON, XML, HTML)

---

## Daily Logs

| Day | Focus | File |
|-----|-------|------|
| 001 | Building a Python port scanner | [day-001.md](logs/day-001.md) |

---

## Key Snippets Quick Reference

```python
# Basic TCP port scanner
import socket

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except:
        return False

# HTTP GET with custom headers
import requests
headers = {"User-Agent": "Mozilla/5.0", "X-Forwarded-For": "127.0.0.1"}
r = requests.get("http://target.com/admin", headers=headers)
print(r.status_code, r.text[:200])
```
