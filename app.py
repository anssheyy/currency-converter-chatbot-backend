from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FCA_API_KEY")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    unit_currency = data['queryResult']['parameters']['unit-currency'][0]
    source_currency = unit_currency['currency']
    amount = unit_currency['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    url = "https://api.freecurrencyapi.com/v1/latest"
    params = {
        "apikey": API_KEY,
        "base_currency": source_currency,
        "currencies": target_currency
    }
    response = requests.get(url, params=params).json()
    rate = response['data'][target_currency]
    converted_amount = round(amount * rate, 2)

    return {
        "fulfillmentText": f"{amount} {source_currency} is approximately {converted_amount} {target_currency}"
    }

if __name__ == '__main__':
    app.run(debug=True)