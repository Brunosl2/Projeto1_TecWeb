from utils import extract_route, build_response, load_data, load_params, load_template
from urllib.parse import unquote_plus
from data.database import Database, Note

db = Database('banco')

def index(request):
    route = extract_route(request)
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            separado = chave_valor.split("=")
            params[unquote_plus(separado[0])] = unquote_plus(separado[1])
        
        if route.startswith('edit'):
            id = int(route.split('/')[-1])
            db.update(Note(
                id = id,
                title=params['titulo'],
                content=params['detalhes']
            ))

        else:
            load_params(params)
        return build_response(code=303, reason='See Other', headers='Location: /')
    
    elif route.startswith('delete'):
        id = int(route.split('/')[-1])
        db.delete(id)
        return build_response(code=303, reason='See Other', headers='Location:/')
    
    elif route.startswith('edit'):
        id = int(route.split('/')[-1])
        note = db.get(id)
        body = load_template('edit.html').format(
            id=id,
            title=note.title,
            details=note.content
        )
        return build_response(body=body)
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content, id = dados.id)
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)

    return build_response(body=body)
