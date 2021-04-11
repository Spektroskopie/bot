from tokens import cmc_token

import json
import requests


from flask import Flask

token = '1700264465:AAEn4sbm6oBUbZNZqCT0LnQYhOfmKv1G4QM'

app = Flask(__name__)


def write_json(data, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_cmc_data(crypto):
    #url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    #params = {'start': '1', 'limit': '5000', 'convert': 'USD'}
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol': crypto, 'convert': 'USD'}
    headers = {'X-CMC_PRO_API_KEY': cmc_token}

    r = requests.get(url, headers=headers, params=params).json()
    write_json(r)
    price = r['data'][crypto]['quote']['USD']['price']
    return price

@app.route('/')
def index():
    return '<h1>Test</h1>'



def main():
    print(get_cmc_data('BTC'))

    # https://api.telegram.org/bot1700264465:AAEn4sbm6oBUbZNZqCT0LnQYhOfmKv1G4QM/getMe
    # https://api.telegram.org/bot1700264465:AAEn4sbm6oBUbZNZqCT0LnQYhOfmKv1G4QM/sendMessage?chat_id=1789037547&text=Hello user


if __name__ == '__main__':
    #main()
    app.run(debug=True)


    #https://www.youtube.com/watch?v=XiBA5LRQFLM
