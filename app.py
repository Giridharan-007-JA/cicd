from flask import Flask, request, jsonify
from factorial import factorial

app = Flask(__name__)


@app.route("/factorial")
def calculate_factorial():
    number = int(request.args.get("number"))

    return jsonify({
        "number": number,
        "factorial": factorial(number)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
