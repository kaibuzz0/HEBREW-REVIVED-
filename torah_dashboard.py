#!/usr/bin/env python3
"""
TORAH DASHBOARD - Interactive Web Interface
Simple HTTP server with clean HTML
"""

import http.server
import socketserver
import json
import sys
sys.path.insert(0, '/root/hebrew-repo')

from import_torah_complete_v2 import TORAH_COMPLETE
from gematria_calculator import GematriaCalculator

PORT = 8080

class DashboardHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        if self.path == '/':
            self.serve_html()
        elif self.path == '/api/torah':
            self.serve_data()
        else:
            self.send_error(404)
    
    def serve_html(self):
        html = '''<!DOCTYPE html>
<html>
<head>
    <title>Torah Analyzer</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }
        .header { background: #1e293b; padding: 20px; margin: -20px -20px 20px -20px; }
        h1 { color: #3b82f6; margin: 0; }
        .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 20px 0; }
        .stat-box { background: #1e293b; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #334155; }
        .stat-num { font-size: 2.5em; color: #3b82f6; font-weight: bold; }
        .books { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .book { background: #1e293b; padding: 20px; border-radius: 8px; border: 1px solid #334155; }
        .book:hover { border-color: #10b981; }
        .book-name { font-size: 1.3em; color: #10b981; margin-bottom: 10px; }
        .hebrew { color: #3b82f6; font-size: 1.1em; }
        .loading { text-align: center; padding: 50px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Torah Analyzer Dashboard</h1>
    </div>
    
    <div class="stats">
        <div class="stat-box"><div class="stat-num">5</div><div>Books</div></div>
        <div class="stat-box"><div class="stat-num">71</div><div>Key Verses</div></div>
        <div class="stat-box"><div class="stat-num">428</div><div>Words</div></div>
        <div class="stat-box"><div class="stat-num">92K</div><div>Gematria</div></div>
    </div>
    
    <div id="books" class="books">
        <div class="loading">Loading Torah data...</div>
    </div>
    
    <script>
        fetch('/api/torah')
            .then(r => r.json())
            .then(data => {
                let html = '';
                for (const [name, book] of Object.entries(data)) {
                    const verses = Object.keys(book.key_verses).length;
                    html += '<div class="book">' +
                        '<div class="book-name">' + name + '</div>' +
                        '<div class="hebrew">' + book.hebrew_name + '</div>' +
                        '<div>' + book.chapters + ' chapters | ' + verses + ' key verses</div>' +
                        '</div>';
                }
                document.getElementById('books').innerHTML = html;
            });
    </script>
</body>
</html>'''
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def serve_data(self):
        data = {}
        for book_name, book_data in TORAH_COMPLETE.items():
            data[book_name] = {
                "hebrew_name": book_data["hebrew_name"],
                "chapters": book_data["chapters"],
                "key_verses": {k: {"hebrew": v} for k, v in book_data["key_verses"].items()}
            }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        print("="*70)
        print("TORAH ANALYZER DASHBOARD")
        print("="*70)
        print(f"\nDashboard: http://localhost:{PORT}")
        print("\nFeatures:")
        print("  - 5 Books of Torah overview")
        print("  - 71 key verses")
        print("  - Real-time statistics")
        print("\nPress Ctrl+C to stop")
        print("="*70)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nStopped.")