# Создание Web-страниц 1
# Запуск HTTP сервера

import http.server

SERVER_ADDRESS = ('', 7999)
http = http.server.HTTPServer(SERVER_ADDRESS, http.server.CGIHTTPRequestHandler)
http.serve_forever()
