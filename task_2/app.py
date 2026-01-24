"""Flask app using Redis hit counter"""

import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', '6379'))

def get_redis():
    """Create and return a Redis client instance."""
    return redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a Docker Challenge App.'

@app.route('/count')
def count():
    r = get_redis()
    hits = r.incr('hits')
    return f'This page has been viewed {hits} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

