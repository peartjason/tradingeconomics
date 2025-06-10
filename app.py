from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        api_key = "6c828f4bbe58471:uq5ohmz0tarx7ii"
        url = f"https://api.tradingeconomics.com/country/united states?c={api_key}&f=json"
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()

        country_name = json_data[0]['Country']
        chart_data = {"country1": [{"Country": item["Country"], "Value": item.get("Value", "N/A")} for item in json_data]}
    except Exception as e:
        country_name = "Error"
        chart_data = {"country1": [{"Country": "Error", "Value": str(e)}]}

    return render_template("index.html", country_name=country_name, data=chart_data)
