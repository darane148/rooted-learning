# 🕷️ Web Security

> Most of the internet is broken. Learn to find the cracks.

This section covers web application security following the OWASP Top 10 framework, using tools like Burp Suite, curl, and specialized scanners. Hands-on labs from DVWA, WebGoat, and HackTheBox.

---

## Topics

- OWASP Top 10 (2021)
- SQL Injection (error-based, blind, time-based)
- Cross-Site Scripting (reflected, stored, DOM)
- Insecure Direct Object Reference (IDOR)
- CSRF, XXE, SSRF
- Authentication flaws and broken access control
- Directory brute-forcing and content discovery
- Burp Suite workflow (intercepting, repeating, scanning)

---

## Daily Logs

| Day | Focus | File |
|-----|-------|------|
| 001 | SQL Injection fundamentals on DVWA | [day-001.md](logs/day-001.md) |
| 002 | XSS attacks and Burp Suite interception | [day-002.md](logs/day-002.md) |

---

## Key Commands Quick Reference

```bash
# Directory bruteforce
gobuster dir -u http://target.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# Nikto web scanner
nikto -h http://target.com

# SQLMap automated injection
sqlmap -u "http://target.com/page?id=1" --dbs

# Curl with custom headers
curl -H "Cookie: session=abc123" http://target.com/admin

# Fetch robots.txt
curl http://target.com/robots.txt
```

---

## OWASP Top 10 (2021) Checklist

- [ ] A01 – Broken Access Control
- [ ] A02 – Cryptographic Failures
- [ ] A03 – Injection
- [ ] A04 – Insecure Design
- [ ] A05 – Security Misconfiguration
- [ ] A06 – Vulnerable and Outdated Components
- [ ] A07 – Identification and Authentication Failures
- [ ] A08 – Software and Data Integrity Failures
- [ ] A09 – Security Logging and Monitoring Failures
- [ ] A10 – Server-Side Request Forgery (SSRF)
