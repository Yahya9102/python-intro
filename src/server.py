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





def run_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, UserRequestHandler)

    print("servern körs på port http://localhost:8000")
    httpd.serve_forever()


