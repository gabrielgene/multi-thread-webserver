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
            <link rel="shortcut icon" href="data:image/x-icon;," type="image/x-icon"> 
            <title>Multi-Thread WebServer</title>
            </head>
            <body style="
                background: #2d2d2d;
            ">
            <h1 style="
                color: #00d8ea;
                position: relative;
                text-align: center;
                font-size: 45px;
                top: 20px;
            ">Multi-Thread WebServer</h1>
            <h1 style="
                color: #00d8ea;
                position: relative;
                text-align: center;
                font-size: 45px;
                top: 20px;
            ">{message}</h1>
            </body>
            </html>
            """ 
        self.wfile.write(html.format(message=message))

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 8080), Handler)
    print 'Starting server in port 8080, use <Ctrl-C> to stop'
    server.serve_forever()