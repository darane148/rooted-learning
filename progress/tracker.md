# 📊 Progress Tracker

> Consistency beats intensity. Log every day.

---

## Master Progress Table

| Day | Date | Topic | Focus | Key Commands / Tools | Difficulty | Status |
|-----|------|-------|-------|----------------------|------------|--------|
| 001 | 2026-04-04 | Linux | File system navigation & permissions | `ls`, `find`, `chmod`, `stat` | ⭐ | ✅ |
| 002 | 2026-04-04 | Linux | SUID binaries & privilege escalation | `find -perm -4000`, `sudo -l` | ⭐⭐ | ✅ |
| 003 | 2026-04-04 | Networking | Nmap scanning techniques | `nmap -sS -sV -sC` | ⭐ | ✅ |
| 004 | 2026-04-04 | Networking | Packet capture with tcpdump | `tcpdump`, `Wireshark` | ⭐⭐ | ✅ |
| 005 | 2026-04-04 | Web Security | SQL Injection on DVWA | `sqlmap`, manual `'OR 1=1--` | ⭐⭐ | ✅ |
| 006 | 2026-04-04 | Web Security | XSS attacks & Burp Suite | Burp Proxy, `<script>alert(1)</script>` | ⭐⭐ | ✅ |
| 007 | 2026-04-04 | APIs | JWT analysis & BOLA testing | `curl`, base64, Burp Repeater | ⭐⭐ | ✅ |
| 008 | 2026-04-04 | Python | Port scanner from scratch | `socket`, Python 3 | ⭐⭐ | ✅ |
| 009 | 2026-04-04 | Kali Tools | Metasploit basics | `msfconsole`, EternalBlue | ⭐⭐⭐ | ✅ |
| 010 | 2026-04-04 | Attack Sim | Full Linux box compromise | `nmap`, `gobuster`, `nc`, SUID privesc | ⭐⭐⭐ | ✅ |

---

## Topic Completion Summary

| Topic | Days Logged | Concepts Mastered | In Progress |
|-------|-------------|-------------------|-------------|
| Linux | 2 | File permissions, SUID escalation | Cron persistence |
| Networking | 2 | Nmap scanning, packet analysis | Wireshark filters |
| Web Security | 2 | SQLi, XSS basics | CSRF, SSRF |
| APIs | 1 | JWT structure, BOLA | Mass assignment |
| Python | 1 | Port scanner | HTTP automation |
| Kali Tools | 1 | Metasploit workflow | Hydra, John |
| Attack Sims | 1 | Full kill chain (Linux) | HTB machines |

---

## Milestones

- [x] Day 1 — First log entry committed
- [x] Day 10 — Completed first attack simulation
- [ ] Day 30 — Root on first HackTheBox machine
- [ ] Day 60 — Complete TryHackMe Jr Penetration Tester path
- [ ] Day 90 — First CTF submission
- [ ] Day 180 — eJPT or CompTIA Security+ certified

---

## Weekly Reflection

### Week 1 (2026-04-04)
**What went well:** Set up the lab environment, completed first full attack simulation, built first Python tool.

**What was hard:** Understanding the difference between a SYN scan and a full connect scan. SUID escalation felt like magic until I read how Linux executes SUID binaries.

**Next week focus:** Deepen web security (CSRF, SSRF, XXE), start HackTheBox "Starting Point" machines.
