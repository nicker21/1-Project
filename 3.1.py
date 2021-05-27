from flask import Flask, render_template
from webargs import fields, validate
from webargs.flaskparser import use_kwargs
import string
import requests
app = Flask(__name__)




# def get_bitcoin_rate() -> /bitcoin_rate?currency=UAH
@app.route("/bitcoin_rate")
@use_kwargs({
    "currency": fields.Str(
        required=False,
        missing='USD',
        validate=[validate.ContainsOnly(string.ascii_uppercase)]
    )},
    location="query"
)
def get_bitcoin_rate(currency):
    r = requests.get('https://bitpay.com/api/rates')
    if r.status_code == 200:
        for key in r.json():
            if key['code'] == currency:
                return render_template('bitcoin.html', code=key['rate'], rate=currency, name=key['name'])
    return (f'Код ошибки: {r.status_code}')


app.run(debug=True)