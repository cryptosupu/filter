from flask import Flask, request
import json


app = Flask(__name__)

@app.route('/filter', methods=['POST'])
def filter():
    request_body = request.get_json(force=True)
    print request_body
    content = request_body['content']
    for data in content:
        print data['name']
        print data['type']
    return json.dumps(content)

if __name__ == '__main__':
    app.run(threaded=True)
