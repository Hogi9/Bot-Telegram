import json
import werkzeug
from flask import Flask, request

from main import predict

app = Flask(__name__)
# Routes for API
@app.route("/getData", methods=["POST"])
def index():
    pass

# Running the app
app.run()