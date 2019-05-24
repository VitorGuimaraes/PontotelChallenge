import requests
import json
from flask import Flask, render_template
import time

app = Flask(__name__)

API_KEY = "Q0X3O4K2KMPKLQJW"

def request_bovespa():
    try:
        req = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=BOVA11.SAO&interval=1min&apikey=" + API_KEY)
        response = json.loads(req.text)
        return response

    except Exception as e:
        print("Requisição deu erro: {}".format(e))

@app.route("/")
def render_html():
    bovespa = request_bovespa()
    
    last_refreshed = bovespa["Meta Data"]["3. Last Refreshed"]
    last_close = bovespa["Time Series (1min)"][last_refreshed]["4. close"]

    return render_template("bovespa.html", value = last_close)

if __name__ == '__main__':
    app.run(debug = True)