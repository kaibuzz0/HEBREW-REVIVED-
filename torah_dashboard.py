#!/usr/bin/env python3
"""
TORAH DASHBOARD v3.0 - Enhanced Visual Interface
Modern dark theme with animations and gradients
"""

import http.server
import socketserver
import json
import sys
sys.path.insert(0, '/root/hebrew-repo')

from import_torah_complete_v2 import TORAH_COMPLETE
from gematria_calculator import GematriaCalculator

PORT = 8080

DASHBOARD_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Torah Analyzer v3.0</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0a0f1a;
            --bg-secondary: #121827;
            --bg-card: #1a2235;
            --accent-blue: #3b82f6;
            --accent-green: #10b981;
            --accent-purple: #8b5cf6;
            --accent-gold: #f59e0b;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --border: #2d3748;
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Inter', -apple-system, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
        }
        
        .bg-anim {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 0;
            opacity: 0.03;
            background: 
                radial-gradient(circle at 20% 80%, #3b82f6 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, #8b5cf6 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, #10b981 0%, transparent 30%);
        }
        
        .wrap { position: relative; z-index: 1; max-width: 1400px; margin: 0 auto; padding: 20px; }
        
        header {
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
        }
        
        header::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 3px;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        }
        
        .logo {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .subtitle { color: var(--text-secondary); margin-top: 8px; font-size: 1.1rem; }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 25px;
            position: relative;
            overflow: hidden;
            transition: transform 0.3s, border-color 0.3s;
        }
        
        .stat-card:hover { transform: translateY(-5px); border-color: var(--accent-blue); }
        
        .stat-card::after {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 3px;
        }
        
        .stat-card:nth-child(1)::after { background: linear-gradient(90deg, #3b82f6, #8b5cf6); }
        .stat-card:nth-child(2)::after { background: linear-gradient(90deg, #10b981, #3b82f6); }
        .stat-card:nth-child(3)::after { background: linear-gradient(90deg, #8b5cf6, #ec4899); }
        .stat-card:nth-child(4)::after { background: linear-gradient(90deg, #f59e0b, #ef4444); }
        
        .stat-icon { font-size: 2rem; margin-bottom: 10px; }
        .stat-val { font-size: 3rem; font-weight: 700; color: var(--text-primary); }
        .stat-lbl { color: var(--text-secondary); font-size: 0.95rem; margin-top: 5px; }
        
        .section-title {
            font-size: 1.5rem;
            margin: 40px 0 20px;
            padding-left: 15px;
            border-left: 4px solid var(--accent-blue);
        }
        
        .books {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 20px;
        }
        
        .book-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
        }
        
        .book-card:hover {
            border-color: var(--accent-green);
            box-shadow: 0 0 30px rgba(16, 185, 129, 0.15);
            transform: translateY(-3px);
        }
        
        .book-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 4px; height: 100%;
            background: var(--accent-green);
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        .book-card:hover::before { opacity: 1; }
        
        .book-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 15px; }
        .book-title { font-size: 1.3rem; font-weight: 600; color: var(--text-primary); }
        .book-hebrew { font-size: 1.5rem; color: var(--accent-blue); direction: rtl; }
        
        .book-stats { display: flex; gap: 20px; margin-top: 15px; padding-top: 15px; border-top: 1px solid var(--border); }
        .book-stat { display: flex; flex-direction: column; }
        .book-stat-val { font-size: 1.5rem; font-weight: 600; color: var(--accent-gold); }
        .book-stat-lbl { font-size: 0.85rem; color: var(--text-secondary); }
        
        .loading { text-align: center; padding: 60px; }
        .spinner {
            width: 50px; height: 50px;
            border: 3px solid var(--border);
            border-top-color: var(--accent-blue);
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
        
        footer {
            margin-top: 60px;
            padding: 30px;
            text-align: center;
            border-top: 1px solid var(--border);
            color: var(--text-secondary);
        }
        footer a { color: var(--accent-blue); text-decoration: none; }
        
        @media (max-width: 768px) {
            .logo { font-size: 1.8rem; }
            .stat-val { font-size: 2.2rem; }
            .books { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="bg-anim"></div>
    <div class="wrap">
        <header>
            <div class="logo">Torah Analyzer</div>
            <div class="subtitle">Complete Hebrew Bible Study System v3.0</div>
        </header>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-icon">📚</div>
                <div class="stat-val">5</div>
                <div class="stat-lbl">Books of Torah</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">📖</div>
                <div class="stat-val" id="vc">-</div>
                <div class="stat-lbl">Key Verses Analyzed</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">✍️</div>
                <div class="stat-val" id="cc">-</div>
                <div class="stat-lbl">Total Chapters</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🔢</div>
                <div class="stat-val" id="gt">92K</div>
                <div class="stat-lbl">Total Gematria</div>
            </div>
        </div>
        
        <h2 class="section-title">Torah Books</h2>
        <div id="books" class="books">
            <div class="loading"><div class="spinner"></div><p>Loading Torah data...</p></div>
        </div>
        
        <footer>
            <p>Hebrew Bible Analyzer | <a href="https://github.com/kaibuzz0/HEBREW-REVIVED-" target="_blank">GitHub</a></p>
            <p style="margin-top: 10px; font-size: 0.9rem;">8 Seeds • 4 Gematria Methods • AI Insights</p>
        </footer>
    </div>
    
    <script>
        async function load() {
            try {
                const r = await fetch('/api/torah');
                const d = await r.json();
                let tv = 0, tc = 0;
                const bh = Object.entries(d).map(([n, b]) => {
                    const v = Object.keys(b.key_verses).length;
                    tv += v; tc += b.chapters;
                    return `<div class="book-card">
                        <div class="book-header">
                            <div><div class="book-title">${n}</div></div>
                            <div class="book-hebrew">${b.hebrew_name}</div>
                        </div>
                        <div class="book-stats">
                            <div class="book-stat"><span class="book-stat-val">${b.chapters}</span><span class="book-stat-lbl">Chapters</span></div>
                            <div class="book-stat"><span class="book-stat-val">${v}</span><span class="book-stat-lbl">Verses</span></div>
                        </div>
                    </div>`;
                }).join('');
                document.getElementById('books').innerHTML = bh;
                document.getElementById('vc').textContent = tv;
                document.getElementById('cc').textContent = tc;
            } catch (e) { document.getElementById('books').innerHTML = '<div class="loading"><p>Error loading data</p></div>'; }
        }
        load();
    </script>
</body>
</html>'''

class DashboardHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args): pass
    
    def do_GET(self):
        if self.path == '/': self.serve_html()
        elif self.path == '/api/torah': self.serve_data()
        else: self.send_error(404)
    
    def serve_html(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(DASHBOARD_HTML.encode('utf-8'))
    
    def serve_data(self):
        data = {n: {"hebrew_name": b["hebrew_name"], "chapters": b["chapters"],
                    "key_verses": {k: {"hebrew": v} for k, v in b["key_verses"].items()}}
                for n, b in TORAH_COMPLETE.items()}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        print("="*70)
        print("TORAH DASHBOARD v3.0")
        print("="*70)
        print(f"\nDashboard: http://localhost:{PORT}")
        print("Features: Enhanced visuals, animations, gradients")
        print("\nPress Ctrl+C to stop")
        print("="*70)
        try: httpd.serve_forever()
        except KeyboardInterrupt: print("\n\nStopped.")