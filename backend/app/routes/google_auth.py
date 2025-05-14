# filepath: /home/kur0/University/NT208/backend/app/routes/auth.py
from flask import Flask, redirect, url_for, session, request
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "your_secret_key")

CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"

@app.route('/login')
def login():
    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        "?response_type=code"
        "&client_id={}"
        "&redirect_uri={}"
        "&scope={}"
    ).format(
        CLIENT_ID,
        url_for('callback', _external=True),
        "openid email profile"
    )
    return redirect(google_auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    # Exchange code for token (implement token exchange logic here)
    # Verify token and extract user info
    return "Logged in successfully!"