# Import Libraries
from flask import Flask, jsonify
from data import transactions_list



# Create Web App
app = Flask(__name__)


# returns list of transactions
@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    response = {'Transactions': transactions_list}
    return jsonify(response), 200




# Returns list of 10 transactions with highest fees
@app.route('/get_ten_highest_fees', methods=['GET'])
def get_ten_highest_fees():
    response = {} # placeholder
    return jsonify(response), 200




# Returns list of 10 transactions with lowest fees
@app.route('/get_ten_lowest_fees', methods=['GET'])
def get_ten_lowest_fees():
    response = {} # placeholder
    return jsonify(response), 200


    


# Returns second highest total fee sum after picking 10 transactions
@app.route('/get_next_highest_total', methods=['GET'])
def get_next_highest_total():
    response = {} # placeholder
    return jsonify(response), 200
    



# Run app
app.run(host='0.0.0.0', port=5050)