import requests
import flask
import redis
import os
import json

app = flask.Flask(__name__)
redis_db = redis.Redis(host='redis', port=6379)

CACHE_PORT = os.environ.get('CACHE_PORT')
CACHE_EXPIRATION_TIME = int(os.environ.get('CACHE_EXPIRATION_TIME'))
COIN_NAME = os.environ.get('COIN_NAME')

@app.route('/')
def get_coin_price():
    # Get the coin name from the environment variables
    coin = COIN_NAME

    # If the coin price is not in the cache, get it from the API
    if redis_db.get(coin) is None:
        coin_price = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd').json()[coin]['usd']
        redis_db.set(coin, coin_price, ex=CACHE_EXPIRATION_TIME)

    # Get the coin price from the cache
    coin_price = redis_db.get(coin)

    result = flask.jsonify({'name':coin, 'price': coin_price.decode('utf-8')})
    # Return the coin price
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=CACHE_PORT)