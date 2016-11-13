from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import time

PORT = 8008
HOST = "localhost"

class HttpProcessor(BaseHTTPRequestHandler):
    count = 0

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        HttpProcessor.count += 1
        message = HttpProcessor.count
        self.wfile.write(message)
        self.wfile.write('\n')
        return

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        HttpProcessor.count += 1
        message = HttpProcessor.count
        self.wfile.write(message)
        self.wfile.write('\n')
        return

serv = HTTPServer((HOST, PORT), HttpProcessor)
now = time.strftime('%Y-%m-%d %H:%M:%S')

print(now)
print "serving at port", PORT
serv.serve_forever()
