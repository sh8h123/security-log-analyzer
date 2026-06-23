log_data = [
            "2026-06-23 12:01:05 INFO User 'admin' logged in successfully.",
    "2026-06-23 12:02:14 WARNING Failed login attempt from IP 192.168.1.50",
    "2026-06-23 12:02:18 WARNING Failed login attempt from IP 192.168.1.50",
    "2026-06-23 12:02:22 WARNING Failed login attempt from IP 192.168.1.50",
    "2026-06-23 12:03:40 ALERT Brute-force flag triggered for IP 192.168.1.50",
    "2026-06-23 12:05:11 INFO User 'boca_bull' logged in successfully."
]

print("=== SECURITY LOG ANALYZER ===")
failed_attempts = 0
alerts = []

for log in log_data:
    if "Failed login" in log:
        failed_attempts += 1
    if "ALERT" in log:
        alerts.append(log)

print(f"[+] Total Lines Scanned: {len(log_data)}")
print(f"[!] Suspected Brute-Force Attempts Found: {failed_attempts}")
print(f"[CRITICAL] Security Alerts Flagged: {len(alerts)}")

for alert in alerts:
    print(f"    --> {alert}")
