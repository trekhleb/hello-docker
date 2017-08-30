from flask import Flask
from redis import Redis, RedisError

# Connect to Redis.
redis = Redis(host="redis")
app = Flask(__name__)


# Define / route.
@app.route("/")
def hello():
    try:
        # Try to increment Redis value.
        visits = redis.incr("counter")
    except RedisError:
        # In case if Redis is unreachable display error message.
        visits = "<i>Can't connect to Redis, counter disabled</i>"

    # Markup for response.
    html = "<h3>Hello Docker!</h3>" \
           "<b>Visits:</b> {visits}"

    # Replace variables from template with actual values.
    return html.format(visits=visits)

if __name__ == "__main__":
    # Run application on port 80.
    app.run(host='0.0.0.0', port=80)
