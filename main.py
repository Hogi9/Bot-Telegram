from token import cmc_token
import requests
import json

telegram_token = '5869999720:AAEDBjY6bSIK9QWeM_4iX15qNL2Hh8ENVGY'

# Untuk membuat file json dengan nama response.json (supaya mudah membaca json)
def write_json(data,filename='response.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_data(cryp):
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    
    parameters = {
    'symbol':cryp,
    'convert':'USD'
    }

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': cmc_token,
    }

    r = requests.get(url,params=parameters,headers=headers).json()
    price = r['data'][cryp]['quote']['USD']['price']
    # write_json(r)
    return price


def main():
    print(get_data('ETH'))
    #https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe

main()