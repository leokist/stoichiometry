from flask import Flask

app = Flask(__name__)
app.secret_key = "ASDASDFASDFASDF"

from views.views import *


if __name__ == '__main__':
    app.run(port=8086, host='0.0.0.0', debug=True, threaded=True)