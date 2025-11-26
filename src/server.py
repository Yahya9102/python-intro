from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from .users import add_user, list_users, user_exists, delete_user



class UserRequestHandler(BaseHTTPRequestHandler):



    def send_json(self, data, status=200):
        
        response = json.dumps(data).encode("utf-8") #Gör om till json-sträng

        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-length", str(len(response)))
        self.end_headers()


        self.wfile.write(response) # Skicka själva body till client



    def do_GET(self):
        
        path = self.path.strip("/") 

        if path == "users":
            users = list_users()
            return self.send_json({"users": users}, status=200)
        

        if path.startswith("users/"):
            parts = path.split("/")
            if len(parts) == 2:
                name = parts[1]
                exists, message = user_exists(name)
                return self.send_json({"exists": exists, "message": message}, status=200)
                

        self.send_json({"error": "Not found"}, status=404)



    def do_POST(self):

        if self.path != "/users":
            return self.send_json({"error": "Not found"}, status=404)
        
        content_lenght = int(self.headers.get("Content-Length"), 0)
        body = self.rfile.read(content_lenght)

        
        try:
           data = json.loads(body)
           name = data.get("name", "")
        except json.JSONDecodeError:
            return self.send_json({"error": "invalid JSON"}, status=400)


        sucess = add_user(name)

        if sucess:
            return self.send_json({
                "success": True,
                "message": f"Added user '{name.strip()}'"
            })

        else:
            return self.send_json({
                "success": False,
                "message": "User invalid or already exists"
            }, status=400)



    def do_DELETE(self):
        path = self.path.strip("/")

        if not path.startswith("users/"):
            return self.send_json({"error": "Not found"}, status=400)
        
        parts = path.split("/")
        if len(parts) != 2:
            return self.send_json({"error": "Bad request"}, status=400)
        
        name = parts[1]

        success, message = delete_user(name)

        if success:
            return self.send_json({"success": True, "message": message})

        else:
            return self.send_json({"success": False, "message": message}, status=404)





def run_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, UserRequestHandler)

    print("servern körs på port http://localhost:8000")
    httpd.serve_forever()


