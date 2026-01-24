import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

def get_redis():
    return redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a Docker Challenge App.'

@app.route('/count')
def count():
    r = get_redis()
    count = r.incr('hits')
    return f'This page has been viewed {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)