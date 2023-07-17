from http.server import BaseHTTPRequestHandler, HTTPServer
# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# import SocketServer
# import time
import json
from gpt import apiCall

# hostName = '192.168.134.53'
hostName = 'localhost'
serverPort = 12345

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('Ciao a tutti'))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content_len = int(self.headers.get('content-length'))
        post_body = self.rfile.read(content_len)
        print(post_body)
        question = eval(post_body)['question']
        ans = apiCall(question)
        self.wfile.write(ans.encode())
        

if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    webServer.serve_forever()
        

