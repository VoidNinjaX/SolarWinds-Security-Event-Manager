
---

# Security Event Monitoring System

This is a simple security monitoring system that collects logs, parses them for security events (e.g., multiple failed login attempts), sends alerts, and provides a web-based dashboard for viewing logs.

## Components

1. **Log Collection and Parsing System**: 
   - Monitors a log file in real-time and detects specific events (like failed login attempts).
2. **Alerting and Dashboard System**: 
   - Sends email alerts when suspicious events are detected.
   - Provides a web-based dashboard for viewing recent logs.

## Requirements

- **Python 3.x**
- The following Python libraries:
  - `Flask` for the web-based dashboard.
  - `smtplib` for sending email alerts (built into Python).

## Installation

### Step 1: Clone the Repository
First, clone this repository to your local machine or download the files directly.

```bash
git clone https://github.com/your-repo/security-event-monitoring.git
cd security-event-monitoring
```

### Step 2: Install Dependencies
You need to install the required dependencies for running the web dashboard.

```bash
pip install flask
```

## Configuration

### Log Collection and Parsing System
The **Log Collection and Parsing System** monitors the `/var/log/syslog` file by default. You can change the log file path to any file you'd like to monitor, such as `/var/log/auth.log`.

Modify the path in the `log_collection_and_parsing.py` script:

```python
log_file = '/var/log/syslog'  # Change this to the log file you want to monitor
```

### Email Alerting System
To send alerts via email, update the SMTP settings and login credentials in `email_alerts.py`:

```python
def send_alert(subject, body, to_email):
    from_email = "your_email@example.com"
    server = smtplib.SMTP('smtp.example.com', 587)  # Change to your SMTP server
    server.starttls()
    server.login(from_email, "your_password")  # Update with your credentials
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(from_email, to_email, message)
    server.quit()
```

Make sure to update:
- `from_email`: Your sender email.
- `smtp.example.com`: The SMTP server address for sending emails (e.g., `smtp.gmail.com` for Gmail).
- `your_password`: Your email password or app-specific password.
- `to_email`: The email address where alerts will be sent.

## Usage

### 1. Log Collection and Parsing System

Run the **Log Collection and Parsing System** to start monitoring the logs in real-time:

```bash
python3 log_collection_and_parsing.py
```

This will monitor the log file for specific events like failed login attempts and print alerts to the console.

### 2. Email Alerting System

You can run the **Email Alerting System** separately to send alerts when suspicious activity is detected. Make sure you have configured the SMTP settings in the script.

```bash
python3 email_alerts.py
```

### 3. Web-Based Dashboard

To view the logs in a web-based dashboard, run the **Flask Web Dashboard**:

```bash
python3 dashboard.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

This will display the most recent log entries from the specified log file.

### 4. Modifying Log Files and Ports

You can customize the log files and ports to scan by editing the following variables:

- **Log file**: Change the `log_file` variable in `log_collection_and_parsing.py` and `dashboard.py`.
- **Port**: You can configure which logs to display or which ports to run your Flask app by modifying the default Flask configuration in `dashboard.py`.

## File Structure

```
.
├── log_collection_and_parsing.py   # Collects and parses logs in real-time
├── email_alerts.py                 # Sends email alerts for security events
├── dashboard.py                    # Flask web-based dashboard for viewing logs
└── templates
    └── dashboard.html              # HTML template for displaying logs in the dashboard
```

## Customization

- **Add Custom Log Parsing**: Modify the `parse_log()` function in `log_collection_and_parsing.py` to handle more complex log formats.
- **Add More Security Event Detection**: Modify or add new event detection rules (e.g., detect port scans, DoS attacks) in the `detect_failed_logins()` function.
- **Change Dashboard Design**: Edit the `dashboard.html` file located in the `templates/` directory to customize the design of the web-based dashboard.

## License

This project is licensed under the MIT License.

---

