#!/usr/bin/env python3
"""
Web Interface for Hebrew Bible Analysis
Flask-based web application
"""

from flask import Flask, render_template, jsonify, request
import json
import sys
sys.path.insert(0, '/root/hebrew-repo')

from biblical_database import BiblicalDatabase
from gematria_calculator import GematriaCalculator
from resonance_decoder import ResonanceEngine

app = Flask(__name__)

# Initialize components
db = BiblicalDatabase()
gem = GematriaCalculator()
res = ResonanceEngine()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/books')
def get_books():
    """Get list of biblical books"""
    conn = db.conn
    cursor = conn.cursor()
    cursor.execute("SELECT name, hebrew_name, chapters FROM books")
    books = [{"name": r[0], "hebrew": r[1], "chapters": r[2]} for r in cursor.fetchall()]
    return jsonify(books)

@app.route('/api/verse/<book>/<int:chapter>/<int:verse>')
def get_verse(book, chapter, verse):
    """Get specific verse with analysis"""
    conn = db.conn
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT v.hebrew_text, v.transliteration, v.translation,
               v.gematria_standard, v.gematria_katan
        FROM verses v
        JOIN books b ON v.book_id = b.id
        WHERE b.name=? AND v.chapter=? AND v.verse=?
    """, (book, chapter, verse))
    
    result = cursor.fetchone()
    if result:
        return jsonify({
            "hebrew": result[0],
            "translit": result[1],
            "translation": result[2],
            "gematria_standard": result[3],
            "gematria_katan": result[4]
        })
    return jsonify({"error": "Verse not found"}), 404

@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """Analyze Hebrew text"""
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Perform analysis
    words = text.split()
    analysis = {
        "words": [],
        "total_gematria": gem.calculate(text),
        "total_katan": gem.calculate(text, "katan")
    }
    
    for word in words:
        decoded = res.decode_word(word)
        analysis["words"].append({
            "hebrew": word,
            "gematria": gem.calculate(word),
            "katan": gem.calculate(word, "katan"),
            "seeds": decoded.seed_sequence,
            "pattern": decoded.resonance_pattern
        })
    
    return jsonify(analysis)

@app.route('/api/search/gematria/<int:value>')
def search_gematria(value):
    """Search by gematria value"""
    results = db.search_by_gematria(value)
    return jsonify([{
        "book": r[3],
        "chapter": r[1],
        "verse": r[2],
        "text": r[0][:50] + "..." if len(r[0]) > 50 else r[0]
    } for r in results])

@app.route('/api/stats')
def get_stats():
    """Get database statistics"""
    stats = db.get_verse_stats()
    return jsonify({
        "total_verses": stats[0],
        "avg_gematria": round(stats[1], 2) if stats[1] else 0,
        "max_gematria": stats[2]
    })

# Create minimal HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hebrew Bible Analyzer</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: #1a1a2e; color: #eee; }
        h1 { color: #e94560; border-bottom: 2px solid #e94560; padding-bottom: 10px; }
        .container { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .box { background: #16213e; padding: 20px; border-radius: 8px; }
        textarea { width: 100%; height: 100px; background: #0f3460; color: #fff; border: none; padding: 10px; font-size: 18px; }
        button { background: #e94560; color: white; border: none; padding: 10px 20px; cursor: pointer; margin-top: 10px; }
        button:hover { background: #ff6b6b; }
        .result { background: #0f3460; padding: 15px; margin-top: 10px; border-radius: 4px; }
        .word-box { display: inline-block; background: #1a1a2e; padding: 10px; margin: 5px; border-radius: 4px; border: 1px solid #e94560; }
        .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0; }
        .stat-card { background: #16213e; padding: 15px; text-align: center; border-radius: 8px; }
        .stat-number { font-size: 2em; color: #e94560; }
        .hebrew { font-size: 24px; direction: rtl; }
    </style>
</head>
<body>
    <h1>🔯 Hebrew Bible Analyzer</h1>
    
    <div class="stats">
        <div class="stat-card">
            <div class="stat-number" id="total-verses">-</div>
            <div>Total Verses</div>
        </div>
        <div class="stat-card">
            <div class="stat-number" id="avg-gematria">-</div>
            <div>Avg Gematria</div>
        </div>
        <div class="stat-card">
            <div class="stat-number" id="max-gematria">-</div>
            <div>Max Gematria</div>
        </div>
    </div>
    
    <div class="container">
        <div class="box">
            <h2>Analyze Hebrew Text</h2>
            <textarea id="hebrew-input" placeholder="Enter Hebrew text...">בְּרֵאשִׁית בָּרָא אֱלֹהִים</textarea>
            <button onclick="analyze()">Analyze</button>
            <div id="analysis-result"></div>
        </div>
        
        <div class="box">
            <h2>Search by Gematria</h2>
            <input type="number" id="gematria-search" placeholder="Enter value..." style="width: 100%; padding: 10px; font-size: 16px;">
            <button onclick="searchGematria()">Search</button>
            <div id="search-result"></div>
        </div>
    </div>
    
    <script>
        // Load stats on page load
        fetch('/api/stats')
            .then(r => r.json())
            .then(data => {
                document.getElementById('total-verses').textContent = data.total_verses;
                document.getElementById('avg-gematria').textContent = data.avg_gematria;
                document.getElementById('max-gematria').textContent = data.max_gematria;
            });
        
        function analyze() {
            const text = document.getElementById('hebrew-input').value;
            fetch('/api/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: text})
            })
            .then(r => r.json())
            .then(data => {
                let html = `<div class="result">
                    <h3>Total Gematria: ${data.total_gematria} (Katan: ${data.total_katan})</h3>
                    <div style="margin-top: 10px;">`;
                
                data.words.forEach(w => {
                    html += `<div class="word-box">
                        <div class="hebrew">${w.hebrew}</div>
                        <div>Gematria: ${w.gematria}</div>
                        <div>Seeds: ${w.seeds}</div>
                    </div>`;
                });
                
                html += '</div></div>';
                document.getElementById('analysis-result').innerHTML = html;
            });
        }
        
        function searchGematria() {
            const value = document.getElementById('gematria-search').value;
            fetch(`/api/search/gematria/${value}`)
                .then(r => r.json())
                .then(data => {
                    let html = '<div class="result">';
                    if (data.length === 0) {
                        html += '<p>No verses found with this gematria value.</p>';
                    } else {
                        data.forEach(v => {
                            html += `<p><strong>${v.book} ${v.chapter}:${v.verse}</strong> - ${v.text}</p>`;
                        });
                    }
                    html += '</div>';
                    document.getElementById('search-result').innerHTML = html;
                });
        }
    </script>
</body>
</html>
"""

@app.route('/templates/index.html')
def template():
    return HTML_TEMPLATE

# Write template to file
import os
os.makedirs('/root/hebrew-repo/templates', exist_ok=True)
with open('/root/hebrew-repo/templates/index.html', 'w') as f:
    f.write(HTML_TEMPLATE)

if __name__ == "__main__":
    print("="*60)
    print("Hebrew Bible Analyzer - Web Interface")
    print("="*60)
    print("\nStarting server on http://localhost:5000")
    print("\nFeatures:")
    print("  - Hebrew text analysis (Gematria + Seeds)")
    print("  - Search by gematria value")
    print("  - Database statistics")
    print("\nPress Ctrl+C to stop")
    print("="*60)
    app.run(host='0.0.0.0', port=5000, debug=False)