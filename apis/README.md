# 🔌 APIs

> Modern apps are APIs. Secure the API, secure the app.

This section covers API security testing — REST API enumeration, authentication bypass, JWT attacks, broken object-level authorization (BOLA/IDOR), and mass assignment vulnerabilities.

---

## Topics

- REST API fundamentals (verbs, status codes, headers)
- API enumeration and documentation discovery
- JWT (JSON Web Token) structure, decoding, and attacks
- Broken Object Level Authorization (BOLA)
- Mass assignment vulnerabilities
- API key leakage in JS files and source code
- Testing with `curl`, Postman, and Burp Suite

---

## Daily Logs

| Day | Focus | File |
|-----|-------|------|
| 001 | API enumeration and JWT analysis | [day-001.md](logs/day-001.md) |

---

## Key Commands Quick Reference

```bash
# Decode a JWT (header + payload only — no verification)
echo "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ" | base64 -d

# curl API with auth token
curl -H "Authorization: Bearer <token>" https://api.target.com/users/1

# Change user ID to test BOLA
curl -H "Authorization: Bearer <token>" https://api.target.com/users/2

# Search JS files for API keys
grep -r "api_key\|apiKey\|Authorization" --include="*.js" .

# Enumerate API endpoints
gobuster dir -u https://api.target.com -w /usr/share/wordlists/api_endpoints.txt
```
