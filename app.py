#!flask/bin/python
from flask import Flask, jsonify, request, make_response, abort
from flask_cors import CORS
import json
from Modelo import *

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def recibir():
    return json.dumps(Modelo.predict(request.json))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)