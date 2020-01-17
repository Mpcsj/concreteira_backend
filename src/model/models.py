from mongoengine import *
from src.util.constants import DATABASE_NAME
connect(DATABASE_NAME)
TIPO_MATERIAL = {'cimento':'cimento', 'areia1':'areia1',
                 'areia2':'areia2', 'brita1':'brita1', 'brita2':'brita2',
                 'aditivo': 'aditivo','areia':'areia'}


class MaterialConstrucao(Document):
    tipo_material =StringField()
    nome = StringField()
    marca = StringField()
    procedencia =StringField()
    qtd_basica = FloatField()
    qtd_pobre = FloatField()
    qtd_rica = FloatField()

    def __str__(self):
        return self.nome+','+self.marca+','+self.procedencia
