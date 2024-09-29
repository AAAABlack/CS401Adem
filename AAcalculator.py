from flask import Flask, request, render_template

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! You can't divide by 0."
    return x / y

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    choice = request.form['choice']
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        result = "Invalid Input"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
