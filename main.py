from flask import Flask, request, jsonify
import numpy as np
import math
import json


api = Flask(__name__)


@api.route('/api/temp', methods=['GET'])
def convert_celsuis_to_kelvin():
    cel = request.args.get("celsius", default=25, type=float)

    temp_data = {

        "celsius": cel,

        "kelvin": cel + 273.15,

    }

    return jsonify(temp_data), 200


@api.route('/api/prime', methods=['GET'])
def find_prim_numbers():
    limit = request.args.get("limit", default=7, type=int)
    prime_num = json.dumps({'prime': sieve_eratosthenes(limit).tolist()})
    return jsonify(prime_num), 200


def sieve_eratosthenes(lim):
    arr = np.ones(lim+1)
    arr[0:2] = False
    i = 2
    while i <= math.sqrt(lim):
        if arr[i]:
            j = i**2
            while j <= lim:
                arr[j] = False
                j = j+i
        if i == 2:
            i = i+1
        else:
            i = i+2
    return np.nonzero(arr)[0]


@api.route('/api/number', methods=['GET'])
def fibonacci():
    num = request.args.get("n", default=45, type=int)
    fibonacci_num = np.ones(num+1)
    fibonacci_num[0] = 0
    if num > 0:
        fibonacci_num[1] = 1
        i = 2
        while i <= num:
            fibonacci_num[i] = fibonacci_num[i-1]+fibonacci_num[i-2]
            i += 1

    fibonacci_ans = {

        "number":  fibonacci_num[num]

    }
    return jsonify(fibonacci_ans), 200


if __name__ == "__main__":
    api.run(debug=True)
