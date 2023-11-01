# server
from wsgiref.simple_server import make_server
from hello import gdhttpapp

httpd = make_server('', 8000, gdhttpapp)
print('Serving HTTP on port 8000...')
httpd.serve_forever()