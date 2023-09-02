import json
from data.database import Database

db = Database('banco')

def extract_route(request):
    return request.split()[1].lstrip('/')

def read_file(file):
    with open(file, 'rb') as f:
        return f.read()
    
def load_data():
    return db.get_all()
    
    
def load_template(file):
    with open('templates/' + file, 'r', encoding='utf-8') as f:
        return str(f.read())
    
def load_params(params):
    db.add(params)
        
def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n\n" + body
    else:
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n" + headers + "\n\n" + body
    
    return str(response).encode()
