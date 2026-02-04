from flask import Flask
import os

app = Flask(__name__)

# We use environment variables to show different versions
VERSION = os.getenv("APP_VERSION", "1.0.0")
COLOR = os.getenv("APP_COLOR", "blue")

@app.route('/')
def hello():
    return f"""
    <body style='background-color: {COLOR}; color: white; font-family: sans-serif; padding: 50px;'>
        <h1>Capstone Project: Canary Rollout</h1>
        <h2>Current Version: {VERSION}</h2>
        <p>Managed by Cloud Build & Cloud Deploy</p>
    </body>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)