def get_email_credentials():
    with open('/home/mpcsj/Documentos/dados_email') as f:
        res = f.readlines()

    res = [el.replace('\n','') for el in res]
    print('credenciais::',res)
    return {'email':res[0],'password':res[1]}