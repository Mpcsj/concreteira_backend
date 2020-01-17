MESSAGE = 'message'
DATABASE_NAME = 'db_proj_valemix'
OK = 200
BAD_REQUEST = 400
def get_model_pdf():
    with open('/home/mpcsj/Projetos/Python/valemix_server/assets/tabela_resultado.html') as f:
        res = f.readlines()
        res = ''.join(res)

    return res