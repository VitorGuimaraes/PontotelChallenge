import requests
import json
import time

from flask import Flask, render_template, request
from collections import namedtuple
from forms import CompanyForm 

app = Flask(__name__)
app.secret_key = "development key"
API_KEY = "C7SE1KQ40TQ82QNZ"

Company = namedtuple("Company", "name close")
companies = []

best_companies = [("Magazine Luiza", "MGLU3"), ("Gol Linhas Aereas", "GOLL4"), 
                  ("Usinas Siderúrgicas de Minas Gerais", "USIM5"), 
                  ("Bradespar", "BRAP4"), ("Eletrobras", "ELET3"), 
                  ("Rumo", "RAIL3"), ("Localiza Rent a Car", "RENT3"), 
                  ("Banco do Brasil", "BBAS3"), ("Vale S.A", "VALE3"), 
                  ("Gerdau", "GOAU4")]

def do_request(symbol):
    try:
        req = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" 
            + symbol + ".SAO&interval=1min&apikey=" + API_KEY)
        
        response = json.loads(req.text)

        return response

    except Exception as e:
        print("A requisição deu erro: {}".format(e))
        
@app.route("/result", methods = ["POST", "GET"])
def store_companies():
    
    if request.method == "POST":
        result = request.form

        company_input = result["name"]

        # Filter string 
        company_input = company_input.lower()
        company_input = company_input.replace(" ", "")

    for company in best_companies:
        
        search = company[0].lower()
        search = search.replace(" ", "")

        if company_input in search:  
            
            company_data = do_request(company[1])
            handler = company_data["Meta Data"]["3. Last Refreshed"]
            
            close = company_data["Time Series (1min)"][handler]["4. close"]               
            result = {company[0]: close} 

            return render_template("result.html", result = result)

def get_ibovespa():

    ibovespa = do_request("BOVA11")
    
    time = ibovespa["Meta Data"]["3. Last Refreshed"]
    last_refreshed = ibovespa["Meta Data"]["3. Last Refreshed"]
    last_close = ibovespa["Time Series (1min)"][last_refreshed]["4. close"]

    return last_close

@app.route("/")
def render_html():

    form = CompanyForm()

    if request.method == "POST":
        if form.validate() == False:
            flash("Preencha o campo!")
            return render_template("bovespa.html", form = form)

    actual_cotation = get_ibovespa()
    return render_template("bovespa.html", value = actual_cotation, data = best_companies, form = form)

if __name__ == '__main__':
    app.run('localhost', port = 5000, debug = True)