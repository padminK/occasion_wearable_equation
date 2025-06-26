#!/usr/bin/env python3
import http.server
import socketserver
import os

# Change to the directory containing the HTML files
os.chdir('.')

PORT = 5000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/Women_in_Tech_Platform_Code.html'
        super().do_GET()

try:
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🌐 Web Server Started Successfully!")
        print(f"📍 Server running at: http://0.0.0.0:{PORT}")
        print("\n📄 Available HTML Files:")
        print(f"• Full Documentation: http://0.0.0.0:{PORT}/Women_in_Tech_Platform_Code.html")
        print(f"• Code Only: http://0.0.0.0:{PORT}/code_export.html")
        print(f"• Default (redirects to full docs): http://0.0.0.0:{PORT}/")
        print("\n✨ Click the URL above or open the Webview to see your project documentation!")
        httpd.serve_forever()
except Exception as e:
    print(f"❌ Server error: {e}")