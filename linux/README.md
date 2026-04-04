# 🐧 Linux

> Mastery of Linux is the foundation of everything in cybersecurity.

This section covers Linux fundamentals through the lens of a security practitioner — file system navigation, permissions, user management, process monitoring, privilege escalation techniques, and scripting.

---

## Topics

- File system layout (`/etc`, `/var`, `/proc`, `/dev`)
- Users, groups, and permissions (`chmod`, `chown`, `sudo`, SUID/SGID)
- Process inspection (`ps`, `netstat`, `lsof`, `/proc`)
- Bash scripting for automation
- Cron jobs and persistence mechanisms
- Privilege escalation vectors (SUID binaries, weak sudo rules, writable paths)
- Log analysis (`/var/log/auth.log`, `journalctl`)

---

## Daily Logs

| Day | Focus | File |
|-----|-------|------|
| 001 | Linux file system navigation & permissions | [day-001.md](logs/day-001.md) |
| 002 | User enumeration & SUID privilege escalation | [day-002.md](logs/day-002.md) |

---

## Key Commands Quick Reference

```bash
# Find SUID binaries
find / -perm -4000 -type f 2>/dev/null

# List all users
cat /etc/passwd | awk -F: '{print $1}'

# Check sudo permissions
sudo -l

# Find world-writable files
find / -writable -type f 2>/dev/null | grep -v proc

# Monitor processes
ps aux --sort=-%mem | head -20
```
