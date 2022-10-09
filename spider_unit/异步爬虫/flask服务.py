from flask import Flask
import time

app = Flask(__name__)


@app.route('/one')
def index_one():
    time.sleep(2)
    return 'hello one'


@app.route('/two')
def index_one():
    time.sleep(2)
    return 'hello two'


@app.route('/three')
def index_one():
    time.sleep(2)
    return 'hello three'


if __name__ == '__main__':
    app.run(threaded=True)
