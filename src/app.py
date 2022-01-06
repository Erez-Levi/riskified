from flask import Flask
import os


os.environ['RESPONSE'] = 'Hello World'

api = Flask(__name__)


@api.route('/messages', methods=['GET'])
def get():
    print(os.environ['RESPONSE'])


if __name__ == "__main__":
    api.run(debug=True, port=8080, host="0.0.0.0")
