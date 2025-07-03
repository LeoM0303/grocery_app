from flask import Flask, request, jsonify
import prod_dao
from sql_connection import get_sql_connection

app = Flask(__name__)


@app.route('/getProducts', methods=['GET'])
def get_products():

    prod_dao.get_all_prod(connection)

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Manegement System")
    app.run(port=5000)