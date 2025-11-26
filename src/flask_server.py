from flask import Flask, jsonify,request

from users import add_user, list_users, user_exists, delete_user

app = Flask(__name__)





@app.get("/users")
def get_users():
    users = list_users()
    return jsonify({"users": users})






app.run(host="0.0.0.0", port=5000)