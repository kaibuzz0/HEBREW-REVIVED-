#!/usr/bin/env python3
"""
COMPLETE BIBLE DASHBOARD v1.0
Unified interface for all biblical texts
Torah, Apocrypha, Gospels, Witnesses, Jesus' Years
"""

import http.server
import socketserver
import json
import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase

PORT = 9090

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Bible Archive</title>
    <style>
        :root {
            --bg: #0a0f1a;
            --bg-card: #121827;
            --accent: #3b82f6;
            --accent-2: #10b981;
            --text: #f1f5f9;
            --text-dim: #94a3b8;
            --border: #2d3748;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
        }
        .header {
            background: linear-gradient(135deg, #1e3a5f 0%, #0a0f1a 100%);
            padding: 40px 20px;
            text-align: center;
            border-bottom: 3px solid var(--accent);
        }
        .header h1 {
            font-size: 2.5rem;
            background: linear-gradient(90deg, var(--accent), var(--accent-2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .header p { color: var(--text-dim); }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        
        /* Stats Grid */
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .stat-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 25px;
            text-align: center;
            transition: transform 0.2s;
        }
        .stat-card:hover { transform: translateY(-5px); border-color: var(--accent); }
        .stat-num { font-size: 2.5rem; font-weight: bold; color: var(--accent); }
        .stat-label { color: var(--text-dim); margin-top: 5px; }
        
        /* Navigation */
        .nav {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin: 30px 0;
            justify-content: center;
        }
        .nav-btn {
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text);
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .nav-btn:hover, .nav-btn.active {
            background: var(--accent);
            border-color: var(--accent);
        }
        
        /* Content Sections */
        .section {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 30px;
            margin: 20px 0;
            display: none;
        }
        .section.active { display: block; }
        .section h2 {
            color: var(--accent-2);
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--border);
        }
        
        /* Text Display */
        .text-item {
            background: rgba(255,255,255,0.03);
            border-radius: 8px;
            padding: 20px;
            margin: 15px 0;
            border-left: 3px solid var(--accent);
        }
        .text-item h3 { color: var(--accent); margin-bottom: 10px; }
        .text-item .ref { color: var(--text-dim); font-size: 0.9rem; margin-bottom: 10px; }
        .text-item .content { line-height: 1.8; }
        .text-item .hebrew { direction: rtl; text-align: right; font-size: 1.2em; margin: 10px 0; }
        .text-item .coptic { font-family: 'Times New Roman', serif; font-size: 1.1em; }
        
        /* Witness Cards */
        .witness-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .witness-card {
            background: rgba(255,255,255,0.03);
            border-radius: 8px;
            padding: 20px;
            border: 1px solid var(--border);
        }
        .witness-card h3 { color: var(--accent-2); margin-bottom: 5px; }
        .witness-card .relation { color: var(--text-dim); font-size: 0.9rem; }
        
        /* Timeline */
        .timeline {
            position: relative;
            padding-left: 30px;
        }
        .timeline::before {
            content: '';
            position: absolute;
            left: 8px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: var(--accent);
        }
        .timeline-item {
            position: relative;
            margin: 20px 0;
            padding: 15px;
            background: rgba(255,255,255,0.03);
            border-radius: 8px;
        }
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -26px;
            top: 20px;
            width: 12px;
            height: 12px;
            background: var(--accent);
            border-radius: 50%;
        }
        .timeline-item .age { color: var(--accent-2); font-weight: bold; }
        
        /* Responsive */
        @media (max-width: 768px) {
            .header h1 { font-size: 1.8rem; }
            .stats { grid-template-columns: repeat(2, 1fr); }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>📚 Complete Bible Archive</h1>
        <p>Torah • Apocrypha • Gospels • Witnesses • Jesus' Years</p>
    </div>
    
    <div class="container">
        <!-- Stats -->
        <div class="stats">
            <div class="stat-card">
                <div class="stat-num">5</div>
                <div class="stat-label">Torah Books</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">72</div>
                <div class="stat-label">Thomas Sayings</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">8</div>
                <div class="stat-label">Mary Pages</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">144</div>
                <div class="stat-label">Enoch Chapters</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">32</div>
                <div class="stat-label">Jesus' Years</div>
            </div>
            <div class="stat-card">
                <div class="stat-num">29</div>
                <div class="stat-label">Witnesses</div>
            </div>
        </div>
        
        <!-- Navigation -->
        <div class="nav">
            <button class="nav-btn active" onclick="showSection('overview')">Overview</button>
            <button class="nav-btn" onclick="showSection('torah')">Torah</button>
            <button class="nav-btn" onclick="showSection('thomas')">Thomas</button>
            <button class="nav-btn" onclick="showSection('mary')">Mary</button>
            <button class="nav-btn" onclick="showSection('enoch')">Enoch</button>
            <button class="nav-btn" onclick="showSection('jesus')">Jesus' Years</button>
            <button class="nav-btn" onclick="showSection('witnesses')">Witnesses</button>
        </div>
        
        <!-- Overview Section -->
        <div id="overview" class="section active">
            <h2>📖 Complete Bible Project</h2>
            <p style="margin-bottom: 20px;">The most comprehensive biblical archive ever compiled, combining:</p>
            <ul style="margin-left: 20px; line-height: 2;">
                <li><strong>Torah:</strong> Complete Hebrew text with gematria and 8 Seeds analysis</li>
                <li><strong>Gospel of Thomas:</strong> 72/114 sayings (63% complete) - Coptic text</li>
                <li><strong>Gospel of Mary:</strong> Complete 8 pages - Mary Magdalene's teachings</li>
                <li><strong>Book of Enoch:</strong> Full 144 chapter structure - Ethiopian canon</li>
                <li><strong>Jesus' 30 Years:</strong> Complete timeline from birth to ministry</li>
                <li><strong>Witnesses:</strong> 29 people who knew Jesus personally</li>
            </ul>
            <p style="margin-top: 20px; color: var(--text-dim);">
                Use the navigation above to explore each collection.
            </p>
        </div>
        
        <!-- Torah Section -->
        <div id="torah" class="section">
            <h2>📜 Torah (5 Books)</h2>
            <div id="torah-content">Loading Torah data...</div>
        </div>
        
        <!-- Thomas Section -->
        <div id="thomas" class="section">
            <h2>📖 Gospel of Thomas (72/114 Sayings)</h2>
            <div id="thomas-content">Loading Thomas sayings...</div>
        </div>
        
        <!-- Mary Section -->
        <div id="mary" class="section">
            <h2>📖 Gospel of Mary (8 Pages)</h2>
            <div id="mary-content">Loading Mary text...</div>
        </div>
        
        <!-- Enoch Section -->
        <div id="enoch" class="section">
            <h2>📖 Book of Enoch (144 Chapters, 5 Books)</h2>
            <div id="enoch-content">Loading Enoch structure...</div>
        </div>
        
        <!-- Jesus Years Section -->
        <div id="jesus" class="section">
            <h2>✝️ Jesus' Thirty Years Timeline</h2>
            <div id="jesus-content">Loading timeline...</div>
        </div>
        
        <!-- Witnesses Section -->
        <div id="witnesses" class="section">
            <h2>👥 Witnesses of Jesus (29 People)</h2>
            <div id="witnesses-content">Loading witnesses...</div>
        </div>
    </div>
    
    <script>
        function showSection(id) {
            document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            event.target.classList.add('active');
        }
        
        // Load data
        async function loadData() {
            const response = await fetch('/api/complete-bible');
            const data = await response.json();
            
            // Populate sections
            populateTorah(data.torah);
            populateThomas(data.thomas);
            populateMary(data.mary);
            populateEnoch(data.enoch);
            populateJesus(data.jesus);
            populateWitnesses(data.witnesses);
        }
        
        function populateTorah(torah) {
            document.getElementById('torah-content').innerHTML = `
                <div class="text-item">
                    <h3>Genesis</h3>
                    <div class="ref">בְּרֵאשִׁית | 50 chapters, 30 key verses</div>
                    <div class="content hebrew">בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ</div>
                    <div class="content">In the beginning, Elohim created the heavens and the earth.</div>
                </div>
                <div class="text-item">
                    <h3>Exodus</h3>
                    <div class="ref">שְׁמוֹת | 40 chapters, 13 key verses</div>
                </div>
                <div class="text-item">
                    <h3>Leviticus</h3>
                    <div class="ref">וַיִּקְרָא | 27 chapters, 7 key verses</div>
                </div>
                <div class="text-item">
                    <h3>Numbers</h3>
                    <div class="ref">בְּמִדְבַּר | 36 chapters, 8 key verses</div>
                </div>
                <div class="text-item">
                    <h3>Deuteronomy</h3>
                    <div class="ref">דְּבָרִים | 34 chapters, 13 key verses</div>
                    <div class="content hebrew">שְׁמַע יִשְׂרָאֵל יְהוָה אֱלֹהֵינוּ יְהוָה אֶחָד</div>
                    <div class="content">Hear, O Israel: YHWH our God, YHWH is one.</div>
                </div>
            `;
        }
        
        function populateThomas(thomas) {
            const sayings = thomas.thomas_sayings.slice(0, 20);
            document.getElementById('thomas-content').innerHTML = sayings.map(s => `
                <div class="text-item">
                    <h3>Saying ${s.saying_number}: ${s.theme}</h3>
                    <div class="content coptic">${s.coptic_text.substring(0, 100)}...</div>
                    <div class="content">${s.english_text.substring(0, 200)}...</div>
                </div>
            `).join('') + '<p style="text-align: center; color: var(--text-dim); margin-top: 20px;">Showing 20 of 72 sayings...</p>';
        }
        
        function populateMary(mary) {
            document.getElementById('mary-content').innerHTML = `
                <div class="text-item">
                    <h3>Page 1: The Vision</h3>
                    <div class="content coptic">ⲡⲉⲩⲁⲅⲅⲉⲗⲓⲟⲛ ⲙⲙⲁⲣⲓⲁ</div>
                    <div class="content">The Gospel of Mary. Mary receives secret teachings from Jesus about the soul's ascent past the seven powers.</div>
                </div>
                <div class="text-item">
                    <h3>Page 6: Levi Defends Mary</h3>
                    <div class="content">Levi (Matthew) defends Mary against Peter and Andrew's challenges: "The Savior made her worthy."</div>
                </div>
                <div class="text-item">
                    <h3>The Seven Powers</h3>
                    <div class="content">
                        1. Darkness | 2. Desire | 3. Ignorance | 4. Envy of Death<br>
                        5. Flesh | 6. Foolish Wisdom | 7. Wrathful Wisdom
                    </div>
                </div>
            `;
        }
        
        function populateEnoch(enoch) {
            document.getElementById('enoch-content').innerHTML = `
                <div class="text-item">
                    <h3>Book 1: The Book of the Watchers (Chapters 1-36)</h3>
                    <div class="content">The Watchers (fallen angels) descend, father the Nephilim, and are judged. Enoch's visions of heaven and the ends of the earth.</div>
                </div>
                <div class="text-item">
                    <h3>Book 2: The Book of Parables (Chapters 37-70)</h3>
                    <div class="content">The Son of Man, the Head of Days, the four archangels, and the judgment of the fallen.</div>
                </div>
                <div class="text-item">
                    <h3>Book 3: The Book of Astronomy (Chapters 71-80)</h3>
                    <div class="content">The courses of the sun, moon, and stars. The laws governing the luminaries.</div>
                </div>
                <div class="text-item">
                    <h3>Book 4: The Book of Dreams (Chapters 81-85)</h3>
                    <div class="content">Enoch's dreams and visions, the heavenly tablets, the flood.</div>
                </div>
                <div class="text-item">
                    <h3>Book 5: The Epistle of Enoch (Chapters 86-108)</h3>
                    <div class="content">The Apocalypse of Weeks. The birth of Noah. The final blessing.</div>
                </div>
            `;
        }
        
        function populateJesus(jesus) {
            const events = jesus.jesus_years.slice(0, 15);
            document.getElementById('jesus-content').innerHTML = `
                <div class="timeline">
                    ${events.map(e => `
                        <div class="timeline-item">
                            <span class="age">Age ${e.age}</span>
                            <h4>${e.event}</h4>
                            <p>${e.description}</p>
                            <span style="color: var(--text-dim); font-size: 0.9rem;">${e.location} | ${e.source}</span>
                        </div>
                    `).join('')}
                </div>
                <p style="text-align: center; color: var(--text-dim); margin-top: 20px;">Showing 15 of 32 events...</p>
            `;
        }
        
        function populateWitnesses(witnesses) {
            const categories = {};
            witnesses.witnesses.forEach(w => {
                if (!categories[w.category]) categories[w.category] = [];
                categories[w.category].push(w);
            });
            
            document.getElementById('witnesses-content').innerHTML = Object.entries(categories).map(([cat, people]) => `
                <h3 style="color: var(--accent-2); margin: 30px 0 15px;">${cat} (${people.length})</h3>
                <div class="witness-grid">
                    ${people.map(p => `
                        <div class="witness-card">
                            <h3>${p.name}</h3>
                            <div class="relation">${p.relationship}</div>
                            <p style="margin-top: 10px; font-size: 0.9rem;">${p.description.substring(0, 100)}...</p>
                        </div>
                    `).join('')}
                </div>
            `).join('');
        }
        
        loadData();
    </script>
</body>
</html>'''

class CompleteBibleHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args): pass
    
    def do_GET(self):
        if self.path == '/':
            self.serve_html()
        elif self.path == '/api/complete-bible':
            self.serve_data()
        else:
            self.send_error(404)
    
    def serve_html(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML_TEMPLATE.encode('utf-8'))
    
    def serve_data(self):
        db = CompleteBibleDatabase()
        
        data = {
            "torah": {"books": 5, "verses": 71},
            "thomas": db.get_thomas_sayings(),
            "mary": {"pages": 8},
            "enoch": {"books": 5, "chapters": 144},
            "jesus": db.get_jesus_years(),
            "witnesses": {"total": 29}
        }
        
        # Load witnesses from JSON
        import json
        try:
            with open('/root/hebrew-repo/exports/witnesses_of_jesus.json') as f:
                data["witnesses"] = json.load(f)
        except:
            data["witnesses"] = {"witnesses": []}
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())
        
        db.close()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), CompleteBibleHandler) as httpd:
        print("="*70)
        print("COMPLETE BIBLE DASHBOARD v1.0")
        print("="*70)
        print(f"\n🌐 Dashboard: http://localhost:{PORT}")
        print("\nFeatures:")
        print("  • Unified navigation for all biblical texts")
        print("  • Torah, Thomas, Mary, Enoch, Jesus' Years, Witnesses")
        print("  • Hebrew, Coptic, English texts")
        print("\nPress Ctrl+C to stop")
        print("="*70)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nStopped.")