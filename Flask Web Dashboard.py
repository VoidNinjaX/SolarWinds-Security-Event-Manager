from flask import Flask, render_template
import os

app = Flask(__name__)

# Read the log file and display recent log entries on the dashboard
@app.route('/')
def dashboard():
    log_file = '/var/log/syslog'  # Path to the log file
    logs = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = f.readlines()[-50:]  # Display the last 50 log entries
    return render_template('dashboard.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
