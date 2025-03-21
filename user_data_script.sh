#!/bin/bash
apt update -y
apt install python3-pip -y
pip3 install flask

cat <<EOF > /home/ubuntu/app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from EC2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
EOF

nohup python3 /home/ubuntu/app.py &
