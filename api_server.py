#!/usr/bin/env python3
"""
Simple API Server (Optional)
HTTP interface for programmatic access
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class BibleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/stats':
            stats = {"texts": 317, "entries": 2046}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(stats).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        pass  # Suppress logs

def run_server(port=8080):
    print(f"Starting API server on port {port}")
    print(f"Try: http://localhost:{port}/stats")
    server = HTTPServer(('localhost', port), BibleAPI)
    server.serve_forever()

if __name__ == "__main__":
    run_server()
