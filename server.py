from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import urllib.request

API_KEY = "30026843"
BASE_URL = "https://api.openmetrolinx.com/OpenDataAPI/api/V1"

class ProxyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/trains':
            # Proxy the API request
            url = f"{BASE_URL}/ServiceataGlance/Trains/All?key={API_KEY}"
            try:
                req = urllib.request.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0')
                response = urllib.request.urlopen(req, timeout=30)
                data = response.read()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(data)
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            # Serve static files
            super().do_GET()

print("Starting server with API proxy on port 3030...")
server = HTTPServer(('0.0.0.0', 3030), ProxyHandler)
server.serve_forever()
