from flask import Flask
import pickle
from flask import request

app = Flask(__name__)


@app.route("/predict")
def predict():
    model = pickle.load(open("model.pkl", "rb"))
    # data = request.args.get('data')

    return str(model.predict([[0, 24.0,	0.000003, 0.03369]]))

if __name__ == "__main__":
    app.run(debug=True)