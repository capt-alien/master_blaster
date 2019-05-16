from flask import Flask, jsonify, request, render_template

from routeing import open_target_phone_numbers, get_costs, cost_return

app = Flask(__name__)

@app.route('/')
def main():
    numbers = open_target_phone_numbers("phone-numbers-10000.txt")
    dictionary = get_costs('route-costs-1000000.txt')
    result = cost_return('+14105548390', dictionary)
    return result


if __name__ == "__main__":
    app.run()
