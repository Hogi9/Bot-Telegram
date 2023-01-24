from token_1 import cmc_token
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

def send_message(chat_id,text="blablabla",message_id=None):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    payload = {'chat_id':chat_id,'text':text,'reply_to_message_id':message_id}

    r = requests.post(url,json=payload)
    return r

def main():
    print(get_data('ETH'))
    #https://api.telegram.org/bot5869999720:AAEDBjY6bSIK9QWeM_4iX15qNL2Hh8ENVGY/getMe

main()