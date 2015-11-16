# -*- coding: utf-8 -*-

import json
import redis
import random

from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)
r = redis.Redis(host='127.0.0.1', port=6379, db=0)


@app.route('/')
def index():
    # return 'Please, enter url!'
    return json.dumps({
        'links': [{
            'rel': '',
            'href': '/generate',
            'title': 'Generate short url for raw url',
            'type': 'application/json'
        }, {
            'rel': '',
            'href': '/short/<short-url>',
            'title': 'Get raw url by short url',
            'type': 'application/json'
        }]
    })


@app.route('/generate')
def shorturl():
    rawurl = request.args.get('rawurl', '')
    # # method 1
    # shorturl = hashlib.md5(rawurl).hexdigest()
    # method 2
    shorturl = transform(rawurl)
    r.setex(shorturl, rawurl, 3000)
    return json.dumps({'short': shorturl})


@app.route('/short/<shorturl>')
def rawurl(shorturl):
    rawurl = r.get(shorturl)
    if not rawurl.startswith('http://'):
        rawurl = 'http://' + rawurl
    return redirect(rawurl)


def transform(rawurl):
    mark = r.incr('index')
    pure_short = dto36(mark)

    # same lenght and ugly
    return pure_short + ''.join(
        chr(random.randint(65, 90))
        for i in range(10 - len(pure_short))
    )


def dto36(num):
    # dicimal to 36
    bits = []
    while num > 0:
        bits.append(etochar(num % 36))
        num = num / 36
    return ''.join(bits[::-1])


def etochar(num):
    # 0~36 to 0-9a-z
    if num < 0 or num >= 36:
        return
    elif num < 10:
        # return str(num)
        return chr(num + 48)
    else:
        return chr(num - 10 + 97)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
