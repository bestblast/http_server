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
        res = upper(hex(randint(268435456, 4294967295))[2:])
        timest = time.strftime(('%d.%m.%Y %H:%M:%S'))
        resp = '<?xml version="1.0" encoding="utf-8"?>\n\
<message>\n\
   <state code="ACCEPT" date="%s">The message has been successfully processed and added to the queue for delivery.</state>\n\
   <reference>%s</reference>\n\
</message>\
' % (timest, res)
        self.wfile.write(resp)
        self.wfile.write("\n")

serv = HTTPServer((HOST, PORT), HttpProcessor)

now = time.strftime('%Y-%m-%d %H:%M:%S')

print(now)
print "serving at port", PORT
serv.serve_forever()
