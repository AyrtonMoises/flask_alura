import os
from jogoteca import app


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_{id}' in nome_arquivo:
            return nome_arquivo
    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    try:
        arquivo = recupera_imagem(id)
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
    except OSError:
        ...