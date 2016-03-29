"""
<?xml version="1.0" encoding="utf-8"?>
<message>
   <state code="ACCEPT" date="29.10.2015 21:46:02">The message has been successfully processed and added to the queue for delivery.</state>
   <reference>1AB5C00E</reference>
</message>
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from random import randint
from string import upper
import time

PORT = 8000
HOST = "localhost"

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Service is working! Use POST method!\n")

    def do_POST(self):
        self.server_version = "Message-OS/v1-06-05"
        self.sys_version = ""
        self.send_response(200)
        self.send_header('content-type', 'application/xml')
        self.end_headers()
        req_path = self.path

        if req_path == '/0-0-1':
            print('You have ask 0-0-1')
            resp1 = 'You have ask 0-0-1'
        elif req_path == '/0-0-2':
            print('You have ask 0-0-2')
            resp1 = 'You have ask 0-0-2'
        else:
            print('Invalid path. Try')
            resp1 = 'Invalid path. Try'

        # res = upper(hex(randint(268435456, 4294967295))[2:])
        timest = time.strftime(('%d.%m.%Y %H:%M:%S'))
        resp1 = resp1 + " Time is: " + timest
        self.wfile.write(resp1)
        self.wfile.write("\n")

serv = HTTPServer((HOST, PORT), HttpProcessor)
now = time.strftime('%Y-%m-%d %H:%M:%S')

print(now)
print "serving at port", PORT
serv.serve_forever()
