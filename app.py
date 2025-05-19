from flask import Flask, render_template, request

Calc1 = Flask(__name__, template_folder='Templates')

@Calc1.route('/')
def index():
    return render_template('CalcFront.html')

@Calc1.route('/Calculating', methods=['POST'])
def Calculating():
    number1 = float(request.form['num1'])
    number2 =float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = number1 + number2

    elif operation == 'subtract':
        result = number1 - number2

    elif operation == 'multiply':
        result = number1 * number2

    elif operation == 'divide':
        result = number1 / number2
        
    return render_template('CalcFront.html', result=result)
if __name__ == '__main__':
    Calc1.run(debug=True, host='0.0.0.0', port=5000) 
