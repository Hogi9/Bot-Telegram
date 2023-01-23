import json
from flask import Flask, request,Response
from main import write_json

app = Flask(__name__)
# Routes for API
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        msg = request.get_json()
        write_json(msg,'telegram_message.json')
        return Response('Ok',status=200)
    else :
        return '<h1>Testing</h1>'

# Running the app
app.run(debug=True)