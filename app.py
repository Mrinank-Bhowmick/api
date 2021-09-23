from flask import Flask,make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask.json import jsonify
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
limiter = Limiter(
    app,
    key_func=get_remote_address
)

@app.route('/')
def hello_world():
    return 'Hello, World!'

##################### LIFE ################################

@app.route('/life')
@limiter.limit("15 per minute")
def life():
    from quote import life_quote
    return jsonify(life_quote())
@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
            jsonify(error="ratelimit exceeded %s" % e.description)
            , 429
    )

##################### BUSINESS ################################

@app.route('/business')
@limiter.limit("15 per minute")
def business():
    from quote import business_quote
    return jsonify(business_quote())
@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
            jsonify(error="ratelimit exceeded %s" % e.description)
            , 429
    )

######################## FRIENDSHIP ###############################

@app.route('/friendship')
@limiter.limit("15 per minute")
def friendship():
    from quote import friendship_quote
    return jsonify(friendship_quote())
@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
            jsonify(error="ratelimit exceeded %s" % e.description)
            , 429
    )

######################### POST #####################################

@app.route('/post')
@limiter.limit("3 per minute")
def quote_post():
    from quote import quote_post
    return jsonify(quote_post())
@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
            jsonify(error="ratelimit exceeded %s" % e.description)
            , 429
    )

@app.route('/random')
@limiter.limit("15 per minute")
def random():
    from quote import random_quote
    return jsonify(random_quote())
@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
            jsonify(error="ratelimit exceeded %s" % e.description)
            , 429
    )

if __name__ == "__main__":
    app.run(debug=True)