#!/usr/bin/env python3
"""
CLI Web Server for Hebrew Bible Analysis
Simple HTTP server with JSON API
"""

import http.server
import socketserver
import json
import sys
sys.path.insert(0, '/root/hebrew-repo')

from biblical_database import BiblicalDatabase
from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine

# Initialize
print("Loading Hebrew Bible Analyzer...")
db = BiblicalDatabase()
gem = GematriaCalculator()
res = ResonanceEngine()

# Read the HTML from a file to avoid encoding issues
HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <title>Hebrew Bible Analyzer</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: monospace; max-width: 900px; margin: 20px auto; padding: 20px; background: #0d1117; color: #c9d1d9; }
        h1 { color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 10px; }
        .box { background: #161b22; border: 1px solid #30363d; padding: 20px; margin: 15px 0; border-radius: 6px; }
        textarea, input { width: 100%; background: #0d1117; color: #c9d1d9; border: 1px solid #30363d; padding: 12px; font-family: monospace; font-size: 16px; }
        button { background: #238636; color: white; border: none; padding: 10px 20px; cursor: pointer; margin-top: 10px; font-size: 14px; }
        button:hover { background: #2ea043; }
        .hebrew { font-size: 28px; direction: rtl; text-align: center; padding: 15px; background: #0d1117; margin: 10px 0; border-radius: 4px; }
        .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0; }
        .stat-card { background: #161b22; padding: 20px; text-align: center; border: 1px solid #30363d; border-radius: 6px; }
        .stat-number { font-size: 2em; color: #58a6ff; font-weight: bold; }
        pre { background: #0d1117; padding: 15px; overflow-x: auto; border: 1px solid #30363d; }
        .word-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; margin-top: 15px; }
        .word-card { background: #21262d; padding: 15px; border-radius: 4px; border: 1px solid #30363d; }
        .seed-tag { background: #238636; color: white; padding: 2px 8px; border-radius: 12px; font-size: 12px; display: inline-block; margin: 2px; }
    </style>
</head>
<body>
    <h1>Hebrew Bible Analyzer</h1>
    
    <div class="stats" id="stats">Loading...</div>
    
    <div class="box">
        <h3>Analyze Hebrew Text</h3>
        <textarea id="input" rows="3">Genesis 1:1 Sample</textarea>
        <button onclick="analyze()">Analyze</button>
        <div id="result"></div>
    </div>
    
    <div class="box">
        <h3>8 Seeds Reference</h3>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
            <div class="word-card"><strong>NA</strong> - Sacred Stillness</div>
            <div class="word-card"><strong>HA</strong> - Living Breath</div>
            <div class="word-card"><strong>GE</strong> - Sacred Form</div>
            <div class="word-card"><strong>OR</strong> - Unveiling Light</div>
            <div class="word-card"><strong>RI</strong> - Turning Alignment</div>
            <div class="word-card"><strong>VO</strong> - Sounded Truth</div>
            <div class="word-card"><strong>EL</strong> - Seal/Witness</div>
            <div class="word-card"><strong>AM</strong> - Embodiment</div>
        </div>
    </div>
    
    <script>
        // Load stats
        fetch('/api/stats').then(r=>r.json()).then(d=>{
            document.getElementById('stats').innerHTML = `
                <div class="stat-card"><div class="stat-number">${d.total_verses}</div><div>Total Verses</div></div>
                <div class="stat-card"><div class="stat-number">${d.avg_gematria}</div><div>Avg Gematria</div></div>
                <div class="stat-card"><div class="stat-number">${d.max_gematria}</div><div>Max Gematria</div></div>`;
        });
        
        function analyze() {
            const text = document.getElementById('input').value;
            fetch('/api/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: text})
            })
            .then(r=>r.json())
            .then(d=>{
                let html = '<pre>Total Gematria: ' + d.total_gematria + ' | Katan: ' + d.total_katan + '</pre>';
                html += '<div class="word-grid">';
                d.words.forEach(w=>{
                    html += '<div class="word-card">';
                    html += '<div>Gematria: ' + w.gematria + '</div>';
                    html += '<div><span class="seed-tag">' + w.seeds + '</span></div>';
                    html += '<div style="font-size: 12px; color: #8b949e;">' + w.pattern + '</div>';
                    html += '</div>';
                });
                html += '</div>';
                document.getElementById('result').innerHTML = html;
            });
        }
    </script>
</body>
</html>
"""

class HebrewHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode('utf-8'))
        elif self.path == '/api/stats':
            stats = db.get_verse_stats()
            data = json.dumps({
                "total_verses": stats[0] or 0,
                "avg_gematria": round(stats[1], 1) if stats[1] else 0,
                "max_gematria": stats[2] or 0
            })
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(data.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/api/analyze':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())
            
            text = data.get('text', '')
            words = text.split()
            
            result = {
                "words": [],
                "total_gematria": gem.calculate(text),
                "total_katan": gem.calculate(text, "katan")
            }
            
            for word in words:
                decoded = res.decode_word(word)
                result["words"].append({
                    "hebrew": word,
                    "gematria": gem.calculate(word),
                    "katan": gem.calculate(word, "katan"),
                    "seeds": decoded.seed_sequence,
                    "pattern": decoded.resonance_pattern
                })
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), HebrewHandler) as httpd:
        print("="*60)
        print(f"Hebrew Bible Analyzer - Web Interface")
        print("="*60)
        print(f"\nServer running at: http://localhost:{PORT}")
        print("\nFeatures:")
        print("  - Hebrew text analysis (Gematria + 8 Seeds)")
        print("  - Database statistics")
        print("  - Dark theme interface")
        print("\nPress Ctrl+C to stop")
        print("="*60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")