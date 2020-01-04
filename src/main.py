from flask import Flask, jsonify
import math as m
import mpmath as mp

app = Flask(__name__)
app.debug = True

@app.route('/<int:start>/<int:end>')
def index(start,end):
    if start < 1:
        start = 1
    mp.dps = 100
    mp.pretty = True
    pi = mp.mpf(0)
    for i in range(start,end+1,2):
        pi += mp.mpf(1)/mp.mpf(2*i-1)
    for i in range(start+1,end+1,2):
        pi -= mp.mpf(1)/mp.mpf(2*i-1)
    pi *= mp.mpf(4)
    return str(pi)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)