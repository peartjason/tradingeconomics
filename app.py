import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_data = {}
    if request.method == 'POST':
        country1 = request.form['country1']
        country2 = request.form['country2']
        indicator = request.form['indicator']
        api_key = '6c828f4bbe58471:uq5ohmz0tarx7ii'  # Replace this with your real API key

        url1 = f"https://api.tradingeconomics.com/historical/country/{country1}/indicator/{indicator}?c={api_key}"
        url2 = f"https://api.tradingeconomics.com/historical/country/{country2}/indicator/{indicator}?c={api_key}"

        res1 = requests.get(url1).json()
        res2 = requests.get(url2).json()

        chart_data = {'country1': res1, 'country2': res2}

    return render_template('index.html', data=chart_data)

if __name__ == '__main__':
    app.run(debug=True)
