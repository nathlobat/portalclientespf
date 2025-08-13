"""Servidor HTTP simples para o portal."""
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000
DIRECTORY = "templates"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


if __name__ == "__main__":
    with TCPServer(("", PORT), Handler) as httpd:
        print(f"Servidor iniciado em http://localhost:{PORT}")
        httpd.serve_forever()
