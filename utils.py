import json

def extract_route(request):
    return request.rsplit()[1].lstrip("/")

def read_file(file):
    with open(file, 'rb') as f:
        return f.read()
    
def load_data(file):
    with open('data/' + file, 'r') as f:
        return json.load(f)
    
def load_template(file):
    with open('templates/' + file, 'r', encoding='utf-8') as f:
        return str(f.read())
    
def load_params(params):
    with open('data/notes.json', 'r', encoding='utf-8') as f:
        text = f.read()
        notes = json.loads(text)
        notes.append(params)
    with open('data/notes.json', 'w') as f:
        f.write(json.dumps(notes))
        
def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n\n" + body
    else:
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n" + headers + "\n\n" + body
    
    return str(response).encode()
