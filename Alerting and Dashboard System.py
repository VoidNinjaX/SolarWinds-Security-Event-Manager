import smtplib

# Send an email alert
def send_alert(subject, body, to_email):
    from_email = "your_email@example.com"
    server = smtplib.SMTP('smtp.example.com', 587)  # Change to your SMTP server
    server.starttls()
    server.login(from_email, "password")  # Enter your email login details
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(from_email, to_email, message)
    server.quit()

# Example usage
if __name__ == "__main__":
    subject = "Security Alert: Multiple Failed Login Attempts"
    body = "Multiple failed login attempts detected from IP address 192.168.1.1."
    to_email = "admin@example.com"
    send_alert(subject, body, to_email)
