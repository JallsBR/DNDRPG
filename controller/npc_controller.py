from database.database import db
from model.user_model import User
from model.personagens_model import Personagem
from controller.rpgcontroller import RPGController
from random import randint
from controller.constante import nd_livro
import re
from math import floor
from flask_login import logout_user, current_user

class NPCController:
    
    @staticmethod
    def criar_npc(data):
        # Acessando os dados do JSON
        print('________________________________________________________')
        print('DATA',data)
        
        
        tipo_personagem = data.get('tipo_personagem')
        if tipo_personagem == None:
            tipo_personagem = 'NPC'
        
        raca = data.get('raca')
        if raca != None:
            raca = raca.strip().title()
        if raca == None:
            raca = RPGController.raça_aleatoria()
        
        genero = data.get('genero')
        if genero == None:
            genero = RPGController.genero_aleatorio()
        
        npc_nome = data.get('npc_nome')     
        if npc_nome == '':
            npc_nome = RPGController.nome_aleatorio(raca=raca, sexo = genero)
 
             
        tendencia = data.get('tendencia')
        if tendencia == None:
            tendencia = RPGController.tendencia_aleatoria()
                # Atributos do NPC
        atributos = {}

        # Atributo Força
        if data.get('forca'):
            atributos['forca'] = int(data.get('forca'))
        else:
            atributos['forca'] = RPGController.gerar_atributo()
        atributos['bforca'] = (atributos['forca'] - 10) // 2
        atributos['save_forca'] = atributos['bforca']

        # Atributo Destreza
        if data.get('destreza'):
            atributos['destreza'] = int(data.get('destreza'))
        else:
            atributos['destreza'] = RPGController.gerar_atributo()
        atributos['bdestreza'] = (atributos['destreza'] - 10) // 2
        atributos['save_destreza'] = atributos['bdestreza']

        # Atributo Constituição
        if data.get('constituição'):
             atributos['constituição'] = int(data.get('constituição'))
        else:
            atributos['constituição'] = RPGController.gerar_atributo()
        atributos['bconstituição'] = (atributos['constituição'] - 10) // 2
        atributos['save_constituicao'] = atributos['bconstituição']

        # Atributo Sabedoria
        if data.get('sabedoria'):
            atributos['sabedoria'] = int(data.get('sabedoria'))
        else:
            atributos['sabedoria'] = RPGController.gerar_atributo()
        atributos['bsabedoria'] = (atributos['sabedoria'] - 10) // 2
        atributos['save_sabedoria'] = atributos['bsabedoria']

        # Atributo Inteligência
        if data.get('inteligência'):
            atributos['inteligência'] = int(data.get('inteligência'))
        else:
            atributos['inteligência'] = RPGController.gerar_atributo()
        atributos['binteligência'] = (atributos['inteligência'] - 10) // 2
        atributos['save_inteligencia'] = atributos['binteligência']

        # Atributo Carisma
        if data.get('carisma'):
            atributos['carisma'] = int(data.get('carisma'))
        else:
            atributos['carisma'] = RPGController.gerar_atributo()
        atributos['bcarisma'] = (atributos['carisma'] - 10) // 2
        atributos['save_carisma'] = atributos['bcarisma']
        
        percepção_passiva = atributos['bsabedoria'] + 10

        proef= 0
        nd = data.get('nd')
        if not nd or nd == '':
            nd = RPGController.gera_nd()
            
        else:
            try:
                # Tenta converter 'nd' para inteiro, se não for possível, trata como string
                nd = int(nd)
            except ValueError:
                pass

        if isinstance(nd, int):
            if nd <= 4:
                proef = 2
            elif nd <= 8:
                proef = 3
            elif nd <= 12:
                proef = 4
            elif nd <= 16:
                proef = 5
            elif nd <= 20:
                proef = 6
            elif nd <= 24:
                proef = 7
            elif nd <= 28:
                proef = 8
            elif nd <= 30:
                proef = 9
        
        nd_pretendido = nd
        
        if nd_pretendido == 0:
            nd_pretendido = nd_livro[0]
        elif nd_pretendido == '1/8':
            nd_pretendido = nd_livro[1]
        elif nd_pretendido == '1/4':
            nd_pretendido = nd_livro[2]
        elif nd_pretendido == '1/2':
            nd_pretendido = nd_livro[3]
        elif isinstance(nd_pretendido, int) and 1 <= nd_pretendido <= 30:
            # Ajusta o índice para valores inteiros entre 1 e 30
              nd_pretendido = nd_livro[nd_pretendido + 3]
        else:
            # Caso nd_pretendido não esteja nos valores esperados, escolhe um valor aleatório
            nd_pretendido = nd_livro[randint(4, 30)]
        
        dadosvida = data.get('dadosvida')
        pv = data.get('pv', 0)

        if not pv and dadosvida:
            pv = RPGController.processar_rolagem(dadosvida)

        if not pv and not dadosvida:
            pv = nd_pretendido['PV']       
            
        if not dadosvida:
            dadosvida = RPGController.deduzir_dvs(pv, atributos['bconstituição'])    
                
        armadurausada = data.get('armadurausada')
        ca = data.get('ca')
        if not ca and armadurausada:
            ca = RPGController.ca_armor(armadurausada, atributos['bdestreza'])        
        
        if not ca and not armadurausada:
            ca = nd_pretendido["CA"]
            armadurausada = RPGController.descobrir_armadura(ca, atributos['bdestreza'])
            

        cd= data.get('cd')
        if not cd:
            cd = nd_pretendido['CD']        
  
        xp = nd_pretendido['XP']
        
        speed = data.get('speed', '30')
        voo = data.get('voo')
        natacao = data.get('natacao')
        darkvision = data.get('darkvision')
        if raca in ["Aasimar", "Draconato", "Alto Elfo", 
                    "Elfo da Floresta", "Gnomo", "Tiefling", "Morto-Vivo",  
                    "Celestial", "Constructo", "Corruptor", "Dragão", "Elemental", 
                    "Fada", "Monstruosidade"] and not darkvision:
            darkvision = '60'
        elif raca in ["Anão","Drow", "Orc" ]  and not darkvision:
            darkvision = '120'
        
        
        resistencias = data.get('resistencias', [])
        resistencia = data.get('resistencia')
        if resistencia == True:
            resistencias = RPGController.resistencias_aleatorio(resistencias)    
        
               
        imunidades = data.get('imunidades', [])
        imunidade = True if data.get('imunidade') else False
        if imunidade == True:
            imunidades = RPGController.imunidades_aleatorio(imunidades)   
            
        # Pericias
        pericias_atuais = data.get('pericias_atuais', [])
        pericias = True if data.get('pericias') else False
        if pericias == True:
            pericias_atuais = RPGController.pericias_aleatorio(pericias_atuais)

       
        
        nmagias = data.get('nmagias')  
        # Habilidades e ações
        habilidades = data.get('habilidades')
        habilidades_atuais = data.get('habilidades_atuais', [])
        
        
        
        #Ações
        acoes= data.get('acoes')
        acoes_atuais = data.get('acoes_atuais', [])
        
        
        
        reacao = data.get('reacão')
        reacoes_atuais = data.get('reacoes_atuais', [])

        # Lendárias
        lendarias = data.get('lendarias')
        desclendaria = data.get('desclendaria', [])
        acoes_lendarias_atuais = data.get('acoes_lendarias_atuais', [])

        
        proefsaves = []
        
        saveforca = True if data.get('saveforca') else False
        if saveforca == True:
            proefsaves.append('saveforca')            
        savedestreza = True if data.get('savedestreza') else False
        if savedestreza == True:
             proefsaves.append('savedestreza')
        saveconstituicao = True if data.get('saveconstituicao') else False
        if saveconstituicao == True:
             proefsaves.append('saveconstituicao')
        savesabedoria = True if data.get('savesabedoria') else False
        if savesabedoria == True:
             proefsaves.append('savesabedoria')
        saveinteligencia = True if data.get('saveinteligencia') else False
        if saveinteligencia == True:
            proefsaves.append('saveinteligencia')
        savecarisma = True if data.get('savecarisma') else False
        if savecarisma == True:
            proefsaves.append('savecarisma')
            
        saves = True if data.get('saves') else False
        if saves == True:
            proefsaves =RPGController.saves_aleatorios(proefsaves)
        if 'saveforca' in proefsaves:
            atributos['save_forca'] += proef
        if 'savedestreza' in proefsaves:
            atributos['save_destreza'] += proef
        if 'saveconstituicao' in proefsaves:
            atributos['save_constituicao'] += proef
        if 'savesabedoria' in proefsaves:
            atributos['save_sabedoria'] += proef
        if 'saveinteligencia' in proefsaves:
            atributos['save_inteligencia'] += proef
        if 'savecarisma' in proefsaves:
            atributos['save_carisma'] += proef
            
        iniciativa = atributos['bdestreza']
        
        
        linguas = ['Comum']
            
            
        if 'Percepção' in pericias_atuais:
            percepção_passiva = atributos['bsabedoria'] + proef + 10                     
            
        pericias_atuais = RPGController.transformar_pericias(bdes = atributos['bdestreza'], bfor= atributos['bforca'], bcon =  atributos['bconstituição'], 
                                                             bint= atributos['binteligência'], bsab= atributos['bsabedoria'], bcar= atributos['bcarisma'], 
                                                             proef= proef, pericias_atuais=pericias_atuais)
        
        
        nataques = data.get('nataques')
        ataques_atuais = data.get('ataques_atuais', [])
        ataques_atuais = RPGController.calcular_ataques_atuais(ataques_atuais = ataques_atuais, nataques = nataques, bdes = atributos['bdestreza'], bfor= atributos['bforca'], 
                                                      bcon =  atributos['bconstituição'], bint= atributos['binteligência'], bsab= atributos['bsabedoria'], 
                                                      bcar= atributos['bcarisma'], proef= proef)
        
        ataques_atuais = [item for sublist in ataques_atuais for item in (sublist if isinstance(sublist, list) else [sublist])]
        
        # Ataques e Reaçoes
        ataques = data.get('ataques')
        print('ATAQUES', ataques)
        if ataques or not ataques_atuais:
            arma1, arma2 = RPGController.ataques_aleatorio(
                nataques=nataques,
                bdes=atributos['bdestreza'],
                bfor=atributos['bforca'],
                proef=proef
            )
            ataques_atuais.append(arma1)
            ataques_atuais.append(arma2)
            
            

        
        npc_data = {
            'nome': npc_nome,
            'tamanho': 'Médio',
            'raca': raca,
            'tendencia': tendencia,
            'genero': genero,
            'proef': proef,
            'atributos': atributos,
            'ca': ca,
            'armadurausada': armadurausada,
            'iniciativa': iniciativa,
            'pv': pv,
            'dadosvida': dadosvida,
            'linguas': linguas,
            'speed': speed,
            'voo': voo,
            'natacao': natacao,
            'darkvision': darkvision,
            'Percepcão_passiva': percepção_passiva,
            'nd': nd,
            'xp': xp,
            'resistencia': resistencia,
            'resistencias': resistencias,
            'imunidade': imunidade,
            'imunidades': imunidades,
            'nataques': nataques,
            'nmagias': nmagias,
            'cd': cd,
            'atributos': atributos,
            'pericias': pericias,
            'pericias_atuais': pericias_atuais,
            'habilidades': habilidades,
            'habilidades_atuais': habilidades_atuais,
            'acoes': acoes,
            'acoes_atuais': acoes_atuais,
            'ataques': ataques,
            'ataques_atuais': ataques_atuais,
            'reacao': reacao,
            'reacoes_atuais': reacoes_atuais,
            'lendarias': lendarias,
            'desclendaria': desclendaria,
            'acoes_lendarias_atuais': acoes_lendarias_atuais
        }
        print ('_____________________________________________________________________________')
        print ('Npc: ', npc_data)
        
        
        
        try:
            personagem = Personagem(id_user=current_user.id, ficha=npc_data, nome=npc_data['nome'], tipo= tipo_personagem)
            db.session.add(personagem)
            db.session.commit()
            print("NPC inserido com sucesso no banco de dados.")
        except Exception as e:
            db.session.rollback()  # Desfaz qualquer mudança no banco de dados no caso de erro
            print(f"Erro ao inserir NPC no banco de dados: {str(e)}")
                       
        return npc_data
