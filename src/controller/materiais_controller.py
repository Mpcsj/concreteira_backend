from src.dao.dao_materiais import DaoMateriais
from src.model.models import TIPO_MATERIAL
from src.util.constants import get_model_pdf
import jinja2
from src.util.util_files import get_email_credentials
class MateriaisController:
    def __init__(self):
        self.dao_materiais = DaoMateriais()
        pass

    def get_all_materiais(self):
        res = self.dao_materiais.find_all_organized_by_type()
        print('chegou aqui: ',type(res['areia'][0]))
        return res

    def get_tipos_e_descricoes(self):
        '''
        {'cimento':'cimento', 'areia1':'areia1',
                 'areia2':'areia2', 'brita1':'brita1', 'brita2':'brita2',
                 'aditivo': 'aditivo','areia':'areia'}
        :return: todos os tipos de materiais cadastrados e suas descricoes
        '''
        return {
            TIPO_MATERIAL['cimento']:'Cimento usado na composicao',
            TIPO_MATERIAL['areia']:'Areia usada sem uma auxiliar',
            TIPO_MATERIAL['areia1']:'Areia principal quando combinada com outra areia',
            TIPO_MATERIAL['areia2']: 'Areia auxiliar quando combinada com outra areia',
            TIPO_MATERIAL['brita1']:'Brita principal quando combinada com outro tipo de brita',
            TIPO_MATERIAL['brita2']: 'Brita auxiliar quando combinada com outro tipo de brita',
            TIPO_MATERIAL['aditivo']: 'Aditivo usado na composição do concreto'
        }

    def processa_escolha(self,dict_elements):
        res,rico,basico,pobre = {},{},{},{}
        # cimento
        for el in ['cimento','brita1','brita2','aditivo']:
            material = dict_elements[el].split(',')
            aux = self.dao_materiais.get_material_by_nome_marca_tipo_e_procedencia(material[0], material[1], el,
                                                                                   material[2])
            rico[el] = aux['qtd_rica']
            basico[el] = aux['qtd_basica']
            pobre[el] = aux['qtd_pobre']
        if 'areia2' not in dict_elements or dict_elements['areia2'] == '':
            # modelo com uma areia apenas
            material = dict_elements['areia1'] = dict_elements['areia1'].split(',')
            aux = self.dao_materiais.get_material_by_nome_marca_tipo_e_procedencia(material[0], material[1], 'areia',
                                                                                   material[2])
            rico['areia1'] = aux['qtd_rica']
            basico['areia1'] = aux['qtd_basica']
            pobre['areia1'] = aux['qtd_pobre']
            rico['areia2'] = '0'
            basico['areia2'] = '0'
            pobre['areia2'] = '0'
        else:
            # modelo com duas areias
            for el in ['areia1','areia2']:
                material = dict_elements[el].split(',')
                aux = self.dao_materiais.get_material_by_nome_marca_tipo_e_procedencia(material[0], material[1], el,
                                                                                       material[2])
                rico[el] = aux['qtd_rica']
                basico[el] = aux['qtd_basica']
                pobre[el] = aux['qtd_pobre']

        res['rico'] = rico
        res['basico'] = basico
        res['pobre'] = pobre
        return res

    def generate_pdf(self,body):
        model_pdf = get_model_pdf()#template
        # print(model_pdf)
        materiais = body['materiais']
        values = body['values']
        rendered = jinja2.Template(model_pdf).render(
            cimento_rico = values[0][0],
            cimento_basico=values[0][0],
            cimento_pobre=values[0][0],
            areia1_rico = values[1][0],
            areia1_basico=values[1][1],
            areia1_pobre=values[1][2],
            areia2_rico=values[2][0],
            areia2_basico=values[2][1],
            areia2_pobre=values[2][2],
            brita1_rico=values[3][0],
            brita1_basico=values[3][1],
            brita1_pobre=values[3][2],
            brita2_rico=values[4][0],
            brita2_basico=values[4][1],
            brita2_pobre=values[4][2],
            aditivo_rico=values[5][0],
            aditivo_basico=values[5][1],
            aditivo_pobre=values[5][2],
            cimento = materiais['cimento'],
            areia1 = materiais['areia1'],
            areia2 = materiais['areia2'],
            brita1 = materiais['brita1'],
            brita2 = materiais['brita2'],
            aditivo = materiais['aditivo']
        )
        return{
            'result':rendered
        }

    def send_email(self, html_data, email):
        credentials = get_email_credentials()
        '''import smtplib
        
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 465)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(credentials['email'], credentials['password'])

        # message to be sent
        message = html_data

        # sending the mail
        s.sendmail(credentials['email'], email, message)

        # terminating the session
        s.quit()'''
        try:
            print('email para ser enviado::',email)
            from flask_mail import Message
            from src.app import mail
            print('processando1')
            msg = Message("Dados processados",
                          sender=credentials['email'],
                          recipients=[email])
            msg.html = html_data
            print('processando2')
            msg.body = ''
            #msg.body = "%s %s" % (body, msg.sender)
            if html_data is not None:
                msg.html = str(html_data)
            print('processando3')
            #mail.connect()
            print('processando4')
            mail.send(msg)
            print('processando5')
        except Exception as e:
            msg = 'Erro ao enviar email::'+str(e)
            print(msg)
            return msg
        return 'Email enviado!!!'