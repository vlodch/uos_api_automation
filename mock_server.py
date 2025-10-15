from flask import Flask, request, jsonify

app = Flask(__name__)
db = {}


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    user_id = str(len(db) + 1)
    db[user_id] = data
    return jsonify({"id": user_id, **data}), 201


@app.route("/api/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = db.get(user_id)
    if not user:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"id": user_id, **user})


@app.route("/api/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in db:
        del db[user_id]
        return "", 204
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(port=8080)
