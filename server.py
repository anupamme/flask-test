import json

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route("/upload/", methods=['POST'])
def upload():
    print('in upload')
    import pdb
    pdb.set_trace()
    print('in upload: ' + str(request.files))
    req_json = json.loads(request.files['data'].decode('utf-8'))
    print(str(req_json))
    return jsonify(status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)