# 💀 Attack Simulations

> Theory ends. The kill chain begins.

This section documents end-to-end attack simulations in controlled lab environments — HTB, TryHackMe, and local VMs. Each simulation follows a complete attack methodology: reconnaissance, enumeration, exploitation, privilege escalation, and post-exploitation.

---

## Attack Methodology

```
1. Reconnaissance     → passive/active information gathering
2. Enumeration        → services, users, shares, web paths
3. Exploitation       → gaining initial foothold
4. Privilege Escalation → local → root/SYSTEM
5. Post-Exploitation  → persistence, pivoting, data exfil (simulated)
6. Reporting          → document everything
```

---

## Simulations Logged

| Day | Target | Platform | Outcome | File |
|-----|--------|----------|---------|------|
| 001 | Basic Linux box (local VM) | Local Lab | Root | [day-001.md](logs/day-001.md) |

---

## Lab Environments Used

- **TryHackMe** – guided learning paths and rooms
- **HackTheBox** – realistic machines with no hand-holding
- **Local VMs** – Metasploitable2, DVWA, VulnHub machines

---

## ⚠️ Legal Notice

All simulations are performed in isolated, legal lab environments. **Never test against systems you do not own or have explicit written permission to test.** Unauthorized access is illegal.
