#!/usr/bin/env python
#--coding:utf-8--

from http.server import BaseHTTPRequestHandler, HTTPServer
import io,shutil
from urllib.parse import urlparse
import json
import os, sys

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        mpath=urlparse(self.path) # ?分割

        self.do_action(mpath)

    def do_POST(self):
        mpath=urlparse(self.path)
        path = mpath.path
        datas = self.rfile.read(int(self.headers['content-length']))
        args_json = bytes.decode(datas)
        args_dict = json.loads(args_json)
        self.do_action(path, args_dict)

    def do_action(self, path, args_dict):
        response_dict = {}
        response_dict['code'] = '1'

        if path == '/chatbot':
            response_dict['code'] = '0'
            if args_dict.get('type') == 'medical_chat':
                response_dict['answer'] ='medical'
            elif args_dict.get('type') == 'normal_chat':
                response_dict['answer'] = 'normal'
            elif args_dict.get('type') == 'mix_chat':
                response_dict['answer'] = 'mix'
            else:
                response_dict['code'] = '1'
        else:
            response_dict['code'] = '1'
        response_json = json.dumps(response_dict)
        self.outputtxt(response_json)

    def outputtxt(self, content):
        #指定返回编码
        enc = "UTF-8"
        content = content.encode(enc)
        f = io.BytesIO()
        f.write(content)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        shutil.copyfileobj(f,self.wfile)
def run():
    port = 8000
    print('starting server, port', port)

    # Server settings
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('running server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()