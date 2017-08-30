from flask import Flask
from redis import Redis, RedisError

redis = Redis(host="redis")
app = Flask(__name__)


@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Can't connect to Redis, counter disabled</i>"

    html = "<h3>Hello Docker!</h3>" \
           "<b>Visits:</b> {visits}"

    return html.format(visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
