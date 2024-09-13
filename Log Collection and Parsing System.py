import os
import re
import time

# Monitor logs and yield new entries
def monitor_logs(log_file):
    with open(log_file, 'r') as f:
        f.seek(0, os.SEEK_END)  # Start at the end of the file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

# Parse log entries and extract useful info
def parse_log(log):
    log_pattern = r'(\S+)\s+(\S+)\s+(\S+):\s+(\S+)\s+(.+)'
    match = re.match(log_pattern, log)
    if match:
        timestamp, host, process, pid, message = match.groups()
        return {
            'timestamp': timestamp,
            'host': host,
            'process': process,
            'pid': pid,
            'message': message
        }
    return None

# Detect security events, such as failed login attempts
failed_login_attempts = {}

def detect_failed_logins(parsed_log):
    if "Failed password" in parsed_log['message']:
        ip = extract_ip(parsed_log['message'])
        failed_login_attempts[ip] = failed_login_attempts.get(ip, 0) + 1
        if failed_login_attempts[ip] > 3:
            print(f"ALERT: Multiple failed login attempts from {ip}")
    return

# Extract IP address from the log message
def extract_ip(message):
    ip_pattern = r'[0-9]+(?:\.[0-9]+){3}'
    match = re.search(ip_pattern, message)
    return match.group(0) if match else 'Unknown'

# Main function to collect logs and detect security events
def run_log_monitor(log_file):
    print(f"Monitoring {log_file} for suspicious activity...")
    for log in monitor_logs(log_file):
        parsed_log = parse_log(log)
        if parsed_log:
            detect_failed_logins(parsed_log)

# Example usage
if __name__ == "__main__":
    log_file = '/var/log/syslog'  # Path to the log file
    run_log_monitor(log_file)
