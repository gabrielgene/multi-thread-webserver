from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text-html')
        self.end_headers()
        message =  threading.currentThread().getName()
        html = """
            <html>
            <head>
            <title>Dummy HTML</title>
            </head>
            <body>
            <h1>Kode Fun is Awesome</h1>
            <h1>{message}</h1>
            </body>
            </html>
            """ 
        self.wfile.write(html.format(message=message))
        f.close()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 8080), Handler)
    print 'Starting server in port 8080, use <Ctrl-C> to stop'
    server.serve_forever()