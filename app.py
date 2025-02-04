"""
Run a Flask application with all functionalities in a single file.
"""
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
import requests
import math

# Helper functions
def is_prime(n):
    # Handle negative numbers
    n = abs(n)
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    # Handle negative numbers
    n = abs(n)
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    # Handle negative numbers
    n = abs(n)
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def sum_of_digits(n):
    # Handle negative numbers
    return sum(int(digit) for digit in str(abs(n)))

def fetch_fun_fact(n):
    # Use absolute value for API call
    abs_n = abs(n)
    url = f"http://numbersapi.com/{abs_n}/math?json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            fact = response.json().get("text", "No fun fact available.")
            
            # Add context for negative numbers
            if n < 0:
                fact = f"Fact about the absolute value {abs_n}: {fact}"
            
            return fact
        return "Could not fetch fun fact."
    except requests.exceptions.RequestException:
        return "Fun fact service unavailable."

# Create Flask app
def create_app():
    app = Flask(__name__)
    CORS(app)

    # Create blueprint for number API
    number_api = Blueprint('number', __name__)

    # Flask API route
    @number_api.route("/api/classify-number", methods=["GET"])
    def classify_number():
        number = request.args.get("number")

        # Validate input
        if number is None or not number.lstrip('-').isdigit():
            return jsonify({"number": number, "error": True}), 400

        number = int(number)

        # Compute properties
        prime = is_prime(number)
        perfect = is_perfect(number)
        armstrong = is_armstrong(number)
        digit_sum = sum_of_digits(number)
        parity = "even" if number % 2 == 0 else "odd"

        # Determine properties list
        properties = ["armstrong"] if armstrong else []
        properties.append(parity)

        # Fetch fun fact
        fun_fact = fetch_fun_fact(number)

        # Return JSON response
        return jsonify({
            "number": number,
            "is_prime": prime,
            "is_perfect": perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }), 200

    app.register_blueprint(number_api, url_prefix='/')
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)