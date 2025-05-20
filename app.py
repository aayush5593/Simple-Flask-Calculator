from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
app = Flask(__name__, template_folder='Templates')
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return render_template('CalcFront.html')

@app.route('/Calculating', methods=['POST'])
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
    app.run(debug=True, host='0.0.0.0', port=5000)
