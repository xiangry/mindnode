#
# from http.server import HTTPServer, CGIHTTPRequestHandler
#
# port = 8875
#
# httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
# print("Starting simple_httpd on port: " + str(httpd.server_port))
# httpd.serve_forever()



import SimpleHTTPServer
import SocketServer

PORT = 8875

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler


httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()