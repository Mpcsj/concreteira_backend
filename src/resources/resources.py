from flask import Blueprint, jsonify,request
from src.util.constants import MESSAGE,OK,BAD_REQUEST
from src.controller.materiais_controller import MateriaisController
endpoint1 = 'APP'

app_resources = Blueprint('app_resources',__name__)

__materiais_controller = MateriaisController()

@app_resources.route('/',methods=['GET'])
def test():
    return jsonify({MESSAGE: 'Endpoint base'})


@app_resources.route('/MATERIAL', methods=['POST'])
def cadastra_material():
    # cadastra um novo material no banco de dados
    print('material cadastrado: ',request.json)
    return jsonify(''), OK

@app_resources.route('/MATERIAL',methods=['GET'])
def obtem_materiais():
    # obtem todos os materiais disponiveis
    return jsonify(__materiais_controller.get_all_materiais()),OK


@app_resources.route('/MATERIAL/tipos',methods=['GET'])
def obtem_tipos_e_descricoes():
    print('obtem tipos e descricoes')
    return jsonify(__materiais_controller.get_tipos_e_descricoes()),OK



@app_resources.route('/MATERIAL/result',methods=['POST'])
def processa_escolha():
    # funcao que recebe a escolha de materiais e retorna a quantidade para cada modelo
    dados = request.json
    print('materiais recebidos: ',dados)
    return jsonify(__materiais_controller.processa_escolha(dados)), OK

@app_resources.route('/MATERIAL/gen_pdf',methods=['POST'])
def generate_pdf():
    body = request.json
    print('funcao gera pdf')
    return jsonify(__materiais_controller.generate_pdf(body)), OK

@app_resources.route('/MATERIAL/send_email',methods = ['POST'])
def send_email():
    body = request.json
    if 'data' not in body or 'email' not in body:
        return jsonify(''), BAD_REQUEST
    else:
        res = __materiais_controller.send_email(body['data'], body['email'])
        return jsonify({'MESSAGE': res}), OK