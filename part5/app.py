import time

from flask import Flask

app = Flask('http2web')

app.counter = 0


@app.route('/state')
def state():
    time.sleep(1)
    return str(app.counter)


@app.route('/increment')
def increment():
    app.counter += 1
    return str(app.counter)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
