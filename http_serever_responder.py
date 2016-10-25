from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from random import randint
from string import upper
import time

PORT = 8880
HOST = "host"

import requests
url = 'http://v4.ident.me'

print "My IP: "+(requests.get(url).text)

print "URL: http://" + (requests.get(url).text) + ":"  +str(PORT)

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Service is working! Use POST method!\n")

    def do_POST(self):
	headers=self.headers
        content_len = int(self.headers.getheader('content-length', 0))
        self.server_version = "Message-OS/v1-06-05"
        self.sys_version = ""
        self.send_response(200)
        self.send_header('Content-type', 'application/xml')
        self.end_headers()
        res = upper(hex(randint(268435456, 4294967295))[2:])
        timest = time.strftime(('%d.%m.%Y %H:%M:%S'))

        #resp = self.rfile.read(content_len)
        # self.wfile.write(resp)
        self.wfile.write("\n")
	print headers
        print self.rfile.read(content_len)

serv = HTTPServer((HOST, PORT), HttpProcessor)

now = time.strftime('%Y-%m-%d %H:%M:%S')

print(now)
print "serving at port", PORT
serv.serve_forever()

