from http.server import BaseHTTPRequestHandler,HTTPServer

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('localhost', 8000)
  httpd = server_class(server_address, handler_class)
  httpd.serve_forever()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        message = "hello"
        self.wfile.write(message.encode())

    def do_POST(self):
        print(self.rfile.read())

run(handler_class=Handler)
