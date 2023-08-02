from flask import Flask,jsonify,request
from classifier import get_prediction


app = Flask(__name__)

@app.route("/alpha", methods=["POST"])

def pred_data():
  image = request.files.get("alpha")
  pred = get_prediction(image)
  return jsonify({"Prediction": pred}, 345)

if __name__ == "__main__":
  app.run(debug=True)