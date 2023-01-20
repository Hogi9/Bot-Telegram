import json
from flask import Flask, request

app = Flask(__name__)
# Routes for API
@app.route("/getData", methods=["POST"])
def index():
    pass

# Running the app
app.run(debug=True)