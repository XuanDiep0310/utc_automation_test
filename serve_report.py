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
        print(f"Thư mục '{DIRECTORY}' chưa tồn tại. Hãy chạy 'pytest' trước để sinh báo cáo.")
        return

    report_file = os.path.join(DIRECTORY, "report.html")
    if not os.path.exists(report_file):
        print(f"Cảnh báo: Chưa tìm thấy 'reports/report.html'. Hãy chạy 'pytest' để tạo báo cáo.")
    
    # Tìm port khả dụng nếu 8080 bị chiếm
    port = PORT
    while port < 8090:
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                url = f"http://localhost:{port}/report.html"
                print("=" * 60)
                print(f"🚀 SERVER BÁO CÁO ĐANG CHẠY TẠI CỔNG: {port}")
                print(f"👉 Đường dẫn xem trực tiếp trên Web: {url}")
                print("💡 Nhấn phím Ctrl + C để dừng server.")
                print("=" * 60)
                
                # Tự động mở trình duyệt web
                webbrowser.open(url)
                httpd.serve_forever()
        except OSError:
            port += 1

if __name__ == "__main__":
    serve()
