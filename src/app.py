from flask import Flask, request
import os


api = Flask(__name__)


@api.route('/messages', methods=['GET'])
def get():
    key = request.args.get('word')
    f = open("/opt/app-volume/messages.log", "a")
    f.write(key + "\n")
    f.close()
    return(os.environ['RESPONSE'])


if __name__ == "__main__":
    api.run(debug=True, port=8080, host="0.0.0.0")
