from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ("192.168.56.1", 80)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print('start server')
print(server_address)
httpd.serve_forever()
 
