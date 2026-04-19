from flask import Flask, request, jsonify

app = Flask(__name__)

licenses = {
    "ABC123": None,
    "BOTILY-001": None,
    "TEST-KEY": None
}

@app.route("/")
def home():
    return "License Server Running"

@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    code = data.get("code")
    machine = data.get("machine")

    if code not in licenses:
        return jsonify({"valid": False})

    if licenses[code] is None:
        licenses[code] = machine
        return jsonify({"valid": True})

    if licenses[code] == machine:
        return jsonify({"valid": True})

    return jsonify({"valid": False})

app.run(host="0.0.0.0", port=10000)
