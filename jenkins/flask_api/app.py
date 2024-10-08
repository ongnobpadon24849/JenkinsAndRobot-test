from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "SDPX GROUP 3"

@app.route('/getcode', methods=['GET'])
def getcode():
    return "SDPX GROUP 3 (200 OK)"


@app.route('/plus/<num1>/<num2>', methods=['GET'])
def plus(num1, num2):
    try:
        num1 = eval(num1)
        num2 = eval(num2)

        results = {
            'Num1' : num1,
            'Num2' : num2,
            'Operator' : 'plus (+)',
            'Results' : num1 + num2,
            }
    except:
        results = { 'ERROR' : 'NOT NUMBER' }

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
