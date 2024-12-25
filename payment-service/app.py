from flask import Flask, jsonify, request

app = Flask(__name__)

payments = []

@app.route('/payments', methods=['POST'])
def make_payment():
    data = request.get_json()
    payments.append(data)
    return jsonify({"message": "Payment processed"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
