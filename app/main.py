from flask import Flask, request, jsonify
from hsn_validator import load_hsn_data, validate_hsn
import os

app = Flask(__name__)

hsn_data = load_hsn_data(os.path.join("app", "data", "HSN_Master_Data.xlsx"))

@app.route("/validate-hsn", methods=["POST"])
def validate_hsn_webhook():
    data = request.get_json()
    codes = data.get("codes", [])
    results = [validate_hsn(code, hsn_data) for code in codes]
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(port=5000)
