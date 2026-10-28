import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    pod_ip = os.environ.get('POD_IP', 'Local/Not Set')
    return f"""
    <html>
        <head><title>Cloud-Native Demo</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1 style="color: #2b5c8f;">Kubernetes Deployment Challenge</h1>
            <p><strong>Host / Pod Name:</strong> {hostname}</p>
            <p><strong>Status:</strong> Healthy & Running</p>
        </body>
    </html>
    """

@app.route('/healthz')
def healthz():
    return jsonify(status="ok"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)