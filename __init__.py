__author__ = "bestblast"

from BaseHTTPServer import HTTPServer
import http_server
import time

PORT = 8000
HOST = "localhost"

serv = HTTPServer((HOST, PORT), http_server.HttpProcessor)

now = time.strftime('%Y-%m-%d %H:%M:%S')

print(now)
print "serving at port", PORT
serv.serve_forever()
