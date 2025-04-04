
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mypage():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f"Hello {name}!"
    return "Hello!"

@app.route("/api/v1.0/predict")
def predict():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    
    if num1 is None or num2 is None:
        return jsonify({"error": "Proszę podać dwa parametry: num1 i num2."}), 400
    
    prediction = 1 if (num1 + num2) > 5.8 else 0
    
    return jsonify({
        "prediction": prediction,
        "features": {"num1": num1, "num2": num2}
    })
    

if __name__ == "__main__":
    app.run()
