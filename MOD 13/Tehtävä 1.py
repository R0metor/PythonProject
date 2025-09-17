from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/alkuluku/<int:luku>")
def alkuluku(luku: int):
    if luku < 2:
        return jsonify({"Number":luku, "isPrime":False})

    for i in range(2, int(luku**0.5)+1):
        if luku % i == 0:
            return jsonify({"Number":luku, "isPrime":False})

    return jsonify({"Number":luku, "isPrime":True})

@app.errorhandler(404)
def page_not_found(virhekoodi):
    return jsonify({"Error": "not found", "message": "Wrong input"}), 404

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port = 3000)