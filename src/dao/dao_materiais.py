from src.model.models import MaterialConstrucao
from src.model.models import TIPO_MATERIAL

'''
TIPO_MATERIAL = {'cimento':'cimento', 'areia1':'areia1',
                 'areia2':'areia2', 'brita1':'brita1', 'brita2':'brita2',
                 'aditivo': 'aditivo','areia':'areia'}

'''
class DaoMateriais:
    def __init__(self):
        pass


    def is_areia(self,tipo_material):
        return (tipo_material == 'areia1' or tipo_material == 'areia2' or tipo_material == 'areia')

    def is_brita(self,tipo_material):
        return (tipo_material == 'brita1' or tipo_material == 'brita2')


    def tipo_els(self,els):
        for el in els:
            print(type(el))

    def get_repr(self,el):
        return el['nome']+','+el['marca']+','+el['procedencia']

    def find_all_organized_by_type(self):
        cimento= set()
        brita = set()
        aditivo=set()
        areia = set()
        for el in MaterialConstrucao.objects():
            if el['tipo_material'] == 'cimento':
                cimento.add(str(el))
            elif self.is_areia(el['tipo_material']):
                areia.add(str(el))
            elif self.is_brita(el['tipo_material']):
                brita.add(str(el))
            else:
                aditivo.add(str(el))

        print('cimentos: ',cimento)
        print('areias: ',areia)
        print('aditivo',aditivo)
        print('brita',brita)
        return {
            'cimento':list(cimento),
            'areia':list(areia),
            'brita':list(brita),
            'aditivo':list(aditivo)
        }


    def save_material(self,material):
        '''
        tipo_material =StringField()
        nome = StringField()
        marca = StringField()
        procedencia =StringField()
        qtd_basica = FloatField()
        qtd_pobre = FloatField()
        qtd_rica = FloatField()
        '''
        pass

    def get_material_by_nome_marca_tipo_e_procedencia(self,nome,marca,tipo,procedencia):
        res = MaterialConstrucao.objects(nome = nome,marca = marca,tipo_material = tipo,procedencia = procedencia)
        # caso seja mais de um, fazer uma media
        qtd_rica = 0
        qtd_basica = 0
        qtd_pobre = 0
        if len(res)>0:
            for el in res:
                qtd_rica += float(el['qtd_rica'])
                qtd_basica += float(el['qtd_basica'])
                qtd_pobre += float(el['qtd_pobre'])
            qtd_rica = round(qtd_rica/len(res))
            qtd_basica = round(qtd_basica / len(res))
            qtd_pobre = round(qtd_pobre / len(res))

        return {'qtd_rica':qtd_rica,'qtd_basica':qtd_basica,'qtd_pobre':qtd_pobre}
