from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(__name__)

FULL_NAME = "SANJEEV S PURANIK"

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv('USER') or os.getenv('USERNAME') or "Unknown"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get "top" command output
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -15", shell=True, text=True)
    except subprocess.CalledProcessError:
        top_output = "Error: Unable to fetch top output"

    html_content = f"""
    <html>
    <head><title>HTop Output</title></head>
    <body>
        <h1>HTop System Details</h1>
        <p><strong>Name:</strong> {FULL_NAME}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 