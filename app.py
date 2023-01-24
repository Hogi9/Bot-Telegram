import json
from flask import Flask, request,Response
from main import write_json,send_message

app = Flask(__name__)
# Routes for API
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        msg = request.get_json()
        chat_id = msg['message']['chat']['id']
        txt = msg['message']['text']
        message_id=msg['message']['message_id']
        # write_json(msg,'telegram_message.json')
        send_message(chat_id,txt,message_id)
        return Response('Ok',status=200)
    else :
        return '<h1>Testing</h1>'

# Running the app
app.run(debug=True)