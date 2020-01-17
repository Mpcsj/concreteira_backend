from src.model.models import MaterialConstrucao,TIPO_MATERIAL
'''
TIPO_MATERIAL = {'cimento':1, 'brita':2, 'areia':3, 'aditivo':4}

class MaterialConstrucao(Document):
    tipo_material =IntField()
    nome = StringField()
    marca = StringField()
    procedencia =StringField()
    qtd_rica = IntField()
    qtd_basica = IntField()
    qtd_pobre = IntField()
'''

def create_cimentos():
    return [
        MaterialConstrucao(tipo_material = TIPO_MATERIAL['cimento'],
                           nome = 'CPIII 40 RS',
                           marca = 'Holcim',
                           procedencia = 'Pedro Leopoldo',
                           qtd_rica = 368,
                           qtd_basica = 270,
                           qtd_pobre = 222
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['cimento'],
                           nome='CP V ARI RS',
                           marca='Holcim',
                           procedencia='Pedro Leopoldo',
                           qtd_rica=376,
                           qtd_basica=276,
                           qtd_pobre=226
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['cimento'],
                           nome='CPIII 40 RS',
                           marca='Holcim',
                           procedencia='Pedro Leopoldo',
                           qtd_rica=388,
                           qtd_basica=286,
                           qtd_pobre=236
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['cimento'],
                           nome='CPV ARI RS',
                           marca='Holcim',
                           procedencia='Pedro Leopoldo',
                           qtd_rica=380,
                           qtd_basica=279,
                           qtd_pobre=228
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['cimento'],
                           nome='CPIII 40 RS',
                           marca='Holcim',
                           procedencia='Pedro Leopoldo',
                           qtd_rica=372,
                           qtd_basica=274,
                           qtd_pobre=224
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['cimento'],
                           nome='CPIII 40 RS',
                           marca='Holcim',
                           procedencia='Pedro Leopoldo',
                           qtd_rica=372,
                           qtd_basica=271,
                           qtd_pobre=222
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['cimento'],
                           nome='CPIII 40 RS',
                           marca='Holcim',
                           procedencia='Sete Lagoas',
                           qtd_rica=388,
                           qtd_basica=286,
                           qtd_pobre=231
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['cimento'],
                           nome='CPII 40 RS',
                           marca='CRH',
                           procedencia='Matozinhos',
                           qtd_rica=380,
                           qtd_basica=283,
                           qtd_pobre=231
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['cimento'],
                           nome='CPII 40 RS',
                           marca='Brennand',
                           procedencia='Sete Lagoas',
                           qtd_rica=388,
                           qtd_basica=286,
                           qtd_pobre=231
                           )
    ]


def create_areias():
    return [
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia1'],
                           nome='Areia Artificial',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=546,
                           qtd_basica=610,
                           qtd_pobre=648
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia2'],
                           nome='Areia Natural',
                           marca='Areal Naque',
                           procedencia='Naque',
                           qtd_rica=234,
                           qtd_basica=261,
                           qtd_pobre=278
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia'],
                           nome='Areia Artificial',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=735,
                           qtd_basica=834,
                           qtd_pobre=886
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia1'],
                           nome='Areia Artificial',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=585,
                           qtd_basica=646,
                           qtd_pobre=679
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia2'],
                           nome='Areia Natural',
                           marca='Areal Naque',
                           procedencia='Naque',
                           qtd_rica=195,
                           qtd_basica=215,
                           qtd_pobre=226
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia1'],
                           nome='Areia Artificial',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=651,
                           qtd_basica=733,
                           qtd_pobre=772
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia2'],
                           nome='Areia Natural',
                           marca='Pedreira Um Valemix',
                           procedencia='Naque',
                           qtd_rica=115,
                           qtd_basica=129,
                           qtd_pobre=136
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia'],
                           nome='Areia Artificial',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=767,
                           qtd_basica=868,
                           qtd_pobre=904
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia1'],
                           nome='Areia Artificial',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=526,
                           qtd_basica=593,
                           qtd_pobre=625
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia2'],
                           nome='Areia Natural',
                           marca='Areal Naque',
                           procedencia='Naque',
                           qtd_rica=226,
                           qtd_basica=254,
                           qtd_pobre=268
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia1'],
                           nome='Areia Artificial',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=548,
                           qtd_basica=615,
                           qtd_pobre=641
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia2'],
                           nome='Areia Natural',
                           marca='Areal Naque',
                           procedencia='Naque',
                           qtd_rica=235,
                           qtd_basica=264,
                           qtd_pobre=275
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia1'],
                           nome='Areia Artificial',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=541,
                           qtd_basica=604,
                           qtd_pobre=630
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia2'],
                           nome='Areia Natural',
                           marca='Areal Naque',
                           procedencia='Naque',
                           qtd_rica=232,
                           qtd_basica=259,
                           qtd_pobre=270
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia1'],
                           nome='Areia Natural',
                           marca='Areal Rio Doce',
                           procedencia='Santana do Paraiso',
                           qtd_rica=490,
                           qtd_basica=555,
                           qtd_pobre=584
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia2'],
                           nome='Po de Pedra',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=264,
                           qtd_basica=299,
                           qtd_pobre=314
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia1'],
                           nome='Areia Artificial',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=523,
                           qtd_basica=588,
                           qtd_pobre=613
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia2'],
                           nome='Areia Natural',
                           marca='Areal Naque',
                           procedencia='Naque',
                           qtd_rica=224,
                           qtd_basica=252,
                           qtd_pobre=263
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia1'],
                           nome='Areia Natural',
                           marca='Areal Cachoeira do Vale',
                           procedencia='Timóteo',
                           qtd_rica=463,
                           qtd_basica=522,
                           qtd_pobre=548
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['areia2'],
                           nome='Pó de Pedra',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=309,
                           qtd_basica=348,
                           qtd_pobre=366
                           )
    ]

def create_britas():
    return [
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=591,
                           qtd_basica=568,
                           qtd_pobre=543
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=394,
                           qtd_basica=378,
                           qtd_pobre=362
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=597,
                           qtd_basica=569,
                           qtd_pobre=539
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=398,
                           qtd_basica=379,
                           qtd_pobre=360
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=596,
                           qtd_basica=572,
                           qtd_pobre=547
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=397,
                           qtd_basica=381,
                           qtd_pobre=365
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=602,
                           qtd_basica=575,
                           qtd_pobre=546
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=401,
                           qtd_basica=383,
                           qtd_pobre=364
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=596,
                           qtd_basica=570,
                           qtd_pobre=542
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=397,
                           qtd_basica=380,
                           qtd_pobre=361
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=600,
                           qtd_basica=573,
                           qtd_pobre=546
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=400,
                           qtd_basica=382,
                           qtd_pobre=364
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=603,
                           qtd_basica=571,
                           qtd_pobre=552
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=402,
                           qtd_basica=381,
                           qtd_pobre=368
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=603,
                           qtd_basica=578,
                           qtd_pobre=553
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=402,
                           qtd_basica=385,
                           qtd_pobre=369
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=596,
                           qtd_basica=566,
                           qtd_pobre=539
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=397,
                           qtd_basica=378,
                           qtd_pobre=359
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=601,
                           qtd_basica=577,
                           qtd_pobre=554
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=401,
                           qtd_basica=385,
                           qtd_pobre=369
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita1'],
                           nome='Brita 1',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=604,
                           qtd_basica=577,
                           qtd_pobre=536
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['brita2'],
                           nome='Brita 0',
                           marca='Pedreira Um Valemix',
                           procedencia='Timóteo',
                           qtd_rica=402,
                           qtd_basica=385,
                           qtd_pobre=357
                           )
    ]


def create_aditivos():
    return [
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 845',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.58,
                           qtd_basica=1.89,
                           qtd_pobre=1.56
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 845',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.52,
                           qtd_basica=1.86,
                           qtd_pobre=1.50
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 860',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.63,
                           qtd_basica=1.97,
                           qtd_pobre=1.59
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 860',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.66,
                           qtd_basica=1.96,
                           qtd_pobre=1.60
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 860',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.66,
                           qtd_basica=1.98,
                           qtd_pobre=1.62
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 845',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.13,
                           qtd_basica=1.57,
                           qtd_pobre=1.27
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 845',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.42,
                           qtd_basica=1.76,
                           qtd_pobre=1.44
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 845',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.42,
                           qtd_basica=1.78,
                           qtd_pobre=1.46
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 860',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.28,
                           qtd_basica=1.67,
                           qtd_pobre=1.37
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 845',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.13,
                           qtd_basica=1.57,
                           qtd_pobre=1.30
                           ),
        MaterialConstrucao(tipo_material=TIPO_MATERIAL['aditivo'],
                           nome='FK 860',
                           marca='Mc-Bauchemie',
                           procedencia='São Paulo',
                           qtd_rica=2.26,
                           qtd_basica=1.65,
                           qtd_pobre=1.35
                           ),
    ]
def start_db_data():
    # obs nas buscas, vou ter que tratar os acentos
    cimentos = create_cimentos()
    # se o user colocar apenas uma areia, aumentar a quantidade da mesma
    areias = create_areias()
    britas = create_britas()
    aditivos = create_aditivos()
    for lista in [cimentos,areias,britas,aditivos]:
        for el in lista:
            MaterialConstrucao.save(el)


