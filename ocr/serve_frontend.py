"""
Simple HTTP server to serve frontend files (HTML, CSS, JS)
Run this in a separate terminal while main.py API server runs on port 8000

Usage:
    python serve_frontend.py
    
Then open: http://localhost:8080
"""
import http.server
import socketserver
import os
from pathlib import Path

PORT = 8080
FRONTEND_DIR = os.path.dirname(os.path.abspath(__file__))

class FrontendHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FRONTEND_DIR, **kwargs)
    
    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        
        # Try to find the file
        file_path = os.path.join(FRONTEND_DIR, self.path.lstrip('/'))
        
        if os.path.isfile(file_path):
            return super().do_GET()
        
        # If file doesn't exist and it's not index.html, try index.html
        if not self.path.startswith('/api'):
            self.path = '/index.html'
            file_path = os.path.join(FRONTEND_DIR, self.path.lstrip('/'))
            if os.path.isfile(file_path):
                return super().do_GET()
        
        self.send_error(404, "File not found")
    
    def log_message(self, format, *args):
        # Custom logging
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), FrontendHandler) as httpd:
        print(f"""
╔════════════════════════════════════════════════════════════════╗
║           🌐 Frontend Server Started                           ║
╠════════════════════════════════════════════════════════════════╣
║  URL: http://localhost:{PORT}                                  ║
║  Directory: {FRONTEND_DIR}                            ║
║                                                                ║
║  Files being served:                                           ║
║    • index.html (Frontend UI)                                  ║
║    • styles.css (Styling)                                      ║
║    • app.js (JavaScript logic)                                 ║
║                                                                ║
║  API Server: http://localhost:8000                             ║
║  (Make sure main.py is also running!)                          ║
║                                                                ║
║  Press Ctrl+C to stop                                          ║
╚════════════════════════════════════════════════════════════════╝
        """)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✓ Server stopped")
