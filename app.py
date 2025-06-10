import requests
from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('TRADINGECONOMICS_API_KEY')

@app.route('/')
def index():
    url = f"https://api.tradingeconomics.com/country/all?c={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return render_template("index.html", data=data)
    except Exception as e:
        return f"Error: {str(e)}"
