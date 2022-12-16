import requests
import flask
import redis

app = flask.Flask(__name__)
redis_db = redis.Redis(host='redis', port=6379)

app.route('/get_coin_price')
def get_coin_price():
    
    coin = flask.request.args.get('coin')

    # Get the coin price from the cache
    coin_price = redis_db.get(coin)

    # If the coin price is not in the cache, get it from the API
    if coin_price is None:
        coin_price = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd').json()[coin]['usd']
        redis_db.set(coin, coin_price, ex=300)

    # Return the coin price
    return redis_db.get(coin)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)