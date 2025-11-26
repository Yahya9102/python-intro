from flask import Flask, jsonify,request

from users import add_user, list_users, user_exists, delete_user

app = Flask(__name__)





@app.get("/users")
def get_users():
    users = list_users()
    return jsonify({"users": users})



@app.get("/users/<name>")
def check_user(name):
    exists, message = user_exists(name)
    return jsonify({"exists": exists, "message": message})



@app.post("/users")
def create_user():
    data = request.get_json(silent=True)
    if not data or "name" not in data:
        return jsonify({"error": "Missing name in the json body"}), 400

    name = data["name"]
    success = add_user(name)

    if success:
        return jsonify({"success": True, "message": f"Added '{name.strip()}'"}), 201
    
    else: 
        return jsonify({"success": False, "message": "User invalid or already exists"}), 400



@app.delete("/users/<name>")
def remove_user(name):
    success, message = delete_user(name)
    if success:
        return jsonify({"success": True, "message": message})
    else: 
        return jsonify({"success": False, "message": message})



app.run(host="0.0.0.0", port=5000)