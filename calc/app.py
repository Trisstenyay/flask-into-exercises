# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_view_function():
    first_number = request.args.get('a')
    second_number = request.args.get('b')
    result = add(int(first_number), int(second_number))
    return str(result)

@app.route('/sub')
def sub_view_function():
    first_number = request.args.get('a')
    second_number = request.args.get('b')
    result = sub(int(first_number), int(second_number))
    return str(result)

@app.route('/mult')
def mult_view_function():
    first_number = request.args.get('a')
    second_number = request.args.get('b')
    result = mult(int(first_number), int(second_number))
    return f'{result}'

@app.route('/div')
def div_view_function():
    first_number = request.args.get('a')
    second_number = request.args.get('b')
    result = div(int(first_number), int(second_number))
    return f'{result}'


operations = {'add': add, 'sub': sub, 'mult': mult, 'div': div}


@app.route('/math/<operator>')
def all_operations(operator):
    first_number = request.args.get('a')
    second_number = request.args.get('b')
    result = operations[operator](int(first_number), int(second_number))
    return f'{result}'

