import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def serve():
    if not os.path.exists(DIRECTORY):
        print(f"Thu muc '{DIRECTORY}' chua ton tai. Hay chay 'pytest' truoc de sinh bao cao.")
        return

    report_file = os.path.join(DIRECTORY, "report.html")
    if not os.path.exists(report_file):
        print("Canh bao: Chua tim thay 'reports/report.html'. Hay chay 'pytest' de tao bao cao.")
    
    # Tim port kha dung neu 8080 bi chiem
    port = PORT
    while port < 8090:
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                url = f"http://localhost:{port}/report.html"
                print("=" * 60)
                print(f"SERVER BAO CAO DANG CHAY TAI CONG: {port}")
                print(f"Duong dan xem truc tiep tren Web: {url}")
                print("Nhan phim Ctrl + C de dung server.")
                print("=" * 60)
                
                # Tu dong mo trinh duyet web
                webbrowser.open(url)
                httpd.serve_forever()
        except OSError:
            port += 1

if __name__ == "__main__":
    serve()
