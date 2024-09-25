from database.database import db
from model.nomes_model import Nome
from random import choice, sample, randint, choices,random
from math import floor, ceil
import re



class RPGController:
    
    @staticmethod
    def rolagem_de_dados(rolagens=1, lados=6, bonus=0):
        try:        
            if not isinstance(rolagens, int) or not isinstance(lados, int) or not isinstance(bonus, int):
                raise ValueError("Os parâmetros 'rolagens', 'lados' e 'bonus' devem ser inteiros.")        
        
            if rolagens <= 0 or lados <= 0:
                raise ValueError("'rolagens' e 'lados' devem ser maiores que 0.")        
        
            total = sum(randint(1, lados) for _ in range(rolagens)) + bonus
            return total

        except ValueError as ve:
            print(f"Erro de valor: {ve}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None


    @staticmethod
    def nome_aleatorio(raca, sexo, quantidade=2):  
        try:
            # Normalização de raças
            if raca in ['Alto Elfo', 'Elfo da Floresta', 'Dríade', 'Planta', 'Fada', 'Centauro', 'Sátiro']:
                raca = 'Elfo'
            elif raca == "Celestial":
                raca = 'Aasimar'
            elif raca == "Gigante":
                raca = 'Goliath'
            elif raca == 'Dragão':
                raca = 'Draconato'
            elif raca == 'Bugbear':
                raca = 'Orc'
            elif raca in ['Corruptor', 'Yuan-ti', 'Drow', 'Medusa']:
                raca = 'Tiefling'
            elif raca in ['Genasi', 'Licantropo', 'Morto-Vivo']:
                raca = 'Humano'


            nome = Nome.query.filter_by(raca=raca, sexo=sexo).all()
            
            # Caso não encontre nomes para a combinação raça/sexo, tenta outras combinações
            if not nome:
                nome = Nome.query.filter_by(sexo=sexo).all()
            if not nome or sexo == 'Outros' or sexo is None:
                nome = Nome.query.filter_by(raca=raca).all()
            if not nome:
                nome = Nome.query.all()

            # Seleciona uma quantidade aleatória de nomes
            nomes_aleatorios = sample(nome, k=min(quantidade, len(nome)))
            nomes_aleatorios = [obj.nome for obj in nomes_aleatorios]
            
            return nomes_aleatorios

        except ValueError as ve:
            print(f"Erro de valor: {ve}")
            return []
        
        except AttributeError as ae:
            print(f"Erro de atributo: {ae}")
            return []

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return []
    
   
   
    @staticmethod
    def raça_aleatoria():
        try:
            raças = [
                "Aasimar", "Draconato", "Anão", "Alto Elfo", "Elfo da Floresta", "Gnomo", 
                "Goliath", "Halfling", "Orc", "Tiefling", "Drow", "Morto Vivo", "Goblin", 
                "Bugbear", "Centauro", "Dríade", "Celestial", "Constructo", "Corruptor", 
                "Genasi", "Fada", "Gigante", "Licantropo", "Medusa", "Yuan-ti", 
                "Sátiro", "Humano" ]

            pesos = [1, 1, 15, 10, 10, 1, 1, 5, 15, 1, 1, 1, 10, 
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 35]        
            
            # Verifica se as listas raças e pesos têm o mesmo tamanho
            if len(raças) != len(pesos):
                raise ValueError("O número de raças e pesos deve ser igual.")
            
            # Escolhendo uma raça com base nos pesos
            escolhe_raça = choices(raças, weights=pesos, k=1)[0]
            return escolhe_raça

        except ValueError as ve:
            print(f"Erro de valor: {ve}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None
    

    @staticmethod
    def genero_aleatorio():
        try:
            genero = ["Masculino", "Feminino", "Outro"]
            # Pesos correspondentes ao gênero
            pesos = [49, 49, 2]            
            # Verifica se as listas genero e pesos têm o mesmo tamanho
            if len(genero) != len(pesos):
                raise ValueError("O número de gêneros e pesos deve ser igual.")            
            # Escolhendo um gênero com base nos pesos
            escolhe_genero = choices(genero, weights=pesos, k=1)[0]
            return escolhe_genero

        except ValueError as ve:
            print(f"Erro de valor: {ve}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None

    @staticmethod
    def tendencia_aleatoria():
        try:
            tendências = [
                "Leal e Bom", "Neutro e Bom", "Caótico e Bom", 
                "Leal e Neutro", "Neutro", "Caótico e Neutro", 
                "Leal e Mau", "Neutro e Mau", "Caótico e Mau"
            ]
            
            # Escolhendo uma tendência aleatoriamente
            return choice(tendências)

        except IndexError as ie:
            print(f"Erro de índice: {ie}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None
    
    @staticmethod
    def gera_nd():
        try:
            numeros = []            
            # Adiciona números menores mais vezes para aumentar a probabilidade
            for i in range(1, 30):  # Supondo que a ND varia de 1 a 30
                numeros.extend([i] * (30 - i))  # Quanto maior o número, menos ele aparece na lista            
            # Retorna um número aleatório da lista ponderada
            return choice(numeros)
        
        except Exception as e:
            print(f"Ocorreu um erro ao gerar o número: {e}")
            return None  # Retorna None em caso de erro


            
    @staticmethod
    def saves_aleatorios(proefsaves):
        try:
            # Lista de possíveis saves
            todos_saves = [ 'saveforca', 'savedestreza', 'saveconstituicao',
                'savesabedoria', 'saveinteligencia', 'savecarisma']             
            # Cria um conjunto para evitar duplicatas
            saves_set = set(proefsaves)
            
            while len(saves_set) < len(proefsaves) + 2:
                novo_save = choice(todos_saves)
                if novo_save not in saves_set:
                    saves_set.add(novo_save)
                                    
                # Verifica se já temos todos os saves
                if len(saves_set) == len(todos_saves):
                    break  # Interrompe o loop se todos os saves foram adicionados
                
            return list(saves_set)
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None
        
        
    @staticmethod
    def resistencias_aleatorio(resistencias):
        try:
            resist = [
                "Ácido", "Concussão", "Cortante", "Elétrico", "Energia", "Fogo",
                "Frio", "Necrótico", "Perfurante", "Psíquico", "Radiante",
                "Trovejante", "Veneno", "Ataques Não-mágicos", "Magia" ]
            
            # Conjunto para evitar resistências duplicadas
            resistencias_set = set(resistencias)
            
            # Adiciona novas resistências até que tenha duas a mais
            while len(resistencias_set) < len(resistencias) + 2:
                nova_resistencia = choice(resist)
                if nova_resistencia not in resistencias_set:
                    resistencias_set.add(nova_resistencia)
                if len(resistencias_set) == len(resist):
                    break
            
            # Converte o conjunto de volta para uma lista e retorna
            return list(resistencias_set)

        except TypeError as te:
            print(f"Erro de tipo: {te}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None
    
    
    
    @staticmethod
    def imunidades_aleatorio(imunidades):
        try:
            resist = [
            "Agarrado", "Amedrontado", "Atordoado", "Caído", "Cego", 
            "Enfeitiçado", "Envenenado", "Impedido", "Incapacitado", 
            "Inconsciente", "Invisível", "Paralisado", "Petrificado", 
            "Surdo", "Ácido", "Concussão", "Cortante", "Elétrico", 
            "Energia", "Fogo", "Frio", "Necrótico", "Perfurante", 
            "Psíquico", "Radiante", "Trovejante", "Veneno", 
            "Ataques Não-mágicos", "Magia"
            ]
            
            # Conjunto para evitar imunidades duplicadas
            imunidades_set = set(imunidades)
            
            # Adiciona novas imunidades até que tenha duas a mais
            while len(imunidades_set) < len(imunidades) + 2:
                nova_imunidade = choice(resist)
                if nova_imunidade not in imunidades_set:
                    imunidades_set.add(nova_imunidade)
                
                # Interrompe o loop se todas as imunidades possíveis já foram adicionadas
                if len(imunidades_set) == len(resist):
                    break
            
            # Converte o conjunto de volta para uma lista e retorna
            return list(imunidades_set)

        except TypeError as te:
            print(f"Erro de tipo: {te}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None
    
    
    @staticmethod
    def pericias_aleatorio(pericias_atuais):
        try:
            # Lista completa de possíveis perícias
            pericias_lista = [
                'Acrobacia', 'Adestrar Animais', 'Arcanismo', 'Atletismo', 'Atuação',
                'Enganação', 'Furtividade', 'História', 'Intimidação', 'Intuição',
                'Investigação', 'Medicina', 'Natureza', 'Percepção', 'Persuasão',
                'Prestidigitação', 'Religião', 'Sobrevivência'
            ]
            
            # Conjunto para evitar perícias duplicadas
            pericias_set = set(pericias_atuais)
            
            # Adiciona novas perícias até que tenha duas a mais
            while len(pericias_set) < len(pericias_atuais) + 2:
                nova_pericia = choice(pericias_lista)
                if nova_pericia not in pericias_set:
                    pericias_set.add(nova_pericia)
                
                # Interrompe o loop se todas as perícias possíveis já foram adicionadas
                if len(pericias_set) == len(pericias_lista):
                    break
            
            # Converte o conjunto de volta para uma lista e retorna
            return list(pericias_set)

        except TypeError as te:
            print(f"Erro de tipo: {te}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None
    
    
    
    @staticmethod
    def transformar_pericias(bdes, bfor, bcon, bint, bsab, bcar, proef, pericias_atuais):
        try:
            # Mapeia as perícias aos seus respectivos atributos
            atributos = {
                'Acrobacia': bdes + proef,
                'Adestrar Animais': bsab + proef,
                'Arcanismo': bint + proef,
                'Atletismo': bfor + proef,
                'Atuação': bcar + proef,
                'Enganação': bcar + proef,
                'Furtividade': bdes + proef,
                'História': bint + proef,
                'Intimidação': bcar + proef,
                'Intuição': bsab + proef,
                'Investigação': bint + proef,
                'Medicina': bsab + proef,
                'Natureza': bint + proef,
                'Percepção': bsab + proef,
                'Persuasão': bcar + proef,
                'Prestidigitação': bdes + proef,
                'Religião': bsab + proef,
                'Sobrevivência': bsab + proef
            }
            pericias_dict = []

            for pericia in pericias_atuais:
                if pericia in atributos:
                    # Obtém o valor diretamente do dicionário
                    valor = atributos[pericia]
                    # Adiciona o dicionário à lista
                    pericias_dict.append({'nome': pericia, 'valor': valor})

            return pericias_dict

        except TypeError as te:
            print(f"Erro de tipo: {te}")
            return None

        except KeyError as ke:
            print(f"Erro de chave: {ke}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None



    @staticmethod
    def gerar_atributo():
        try:
            # Gera 4 números aleatórios entre 1 e 6
            dados = [randint(1, 6) for _ in range(4)]
            # Soma os dados e subtrai o menor valor
            atributo_total = sum(dados) - min(dados)
            return atributo_total

        except ValueError as ve:
            print(f"Erro de valor: {ve}")
            return None

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None
    

    
    @staticmethod
    def processar_rolagem_dv(dadosvida):
        # Separar as rolagens por " + "
        partes = dadosvida.split(" + ")

        total_pv = 0
        try:
            for parte in partes:
                # Expressão regular para capturar a rolagem no formato `NdX+Y`
                padrao = re.match(r'(\d+)d(\d+)(\+(\d+))?', parte)

                if padrao:
                    rolagens = int(padrao.group(1))  # O número antes do 'd'
                    lados = int(padrao.group(2))     # O número depois do 'd'
                    bonus = int(padrao.group(4)) if padrao.group(4) else 0  # O número após o '+', ou 0 se não houver

                    # Chamar a função de rolagem de dados
                    pv = RPGController.rolagem_de_dados(rolagens=rolagens, lados=lados, bonus=bonus)
                    total_pv += pv
                else:
                    raise ValueError(f"Formato de dados de vida inválido: {parte}")

        except ValueError as e:
            print(f"Erro: {e}")
            # Retorna 0 no caso de erro
            return 0

        return total_pv
    
    
    @staticmethod    
    def deduzir_dvs(pv, bcons):
        try:
            # Verifica se pv e bcons são números
            if not isinstance(pv, (int, float)) or not isinstance(bcons, (int, float)):
                raise ValueError("PV e bcons devem ser números.")

            # Calcula a média de vida por dado
            media_por_dado = 5 + bcons
            
            # Calcula o número de dados necessários
            numero_de_dados = ceil(pv / media_por_dado)
            
            # Verifica se o número de dados é menor que 0
            if numero_de_dados < 0:
                raise ValueError("O número de dados não pode ser negativo.")
            
            # Formata a saída
            if bcons > 0:
                resultado = f"{numero_de_dados}d8 + {numero_de_dados*bcons}"
            
            elif bcons == 0:
                resultado = f"{numero_de_dados}d8"
            else:
                resultado = f"{numero_de_dados}d8 - {numero_de_dados*bcons}"  
            
            return resultado
        
        except Exception as e:
            return str(e)




#_______________________________________________________________________________________________________________________________






    @staticmethod
    def aptidão_mágica(magia=False, classe=''):
        """
            Randomiza a possibilidade de um personagem conter magia
        :param magia: Pro padrão está em False, se modificado para True o personagem possui magias
        :param classe: Especifica uma determinada classe

        """


        aptidão_magica = randint(1, 15)
        magias1 = magias2 = magias3 = magias4= magias5 =0
        if magia:
            aptidão_magica = 15
        if aptidão_magica == 15:
            truques = randint(1, 3)
            magias1 = randint(0, 3)
            if magias1 > 1:
                magias2 = (randint(0, 3))
                if magias2 > 1:
                    magias3 = randint(0, 3)
                    if magias3 > 1:
                        magias4 = randint(0, 3)
                        if magias4 > 1:
                            magias5 = randint(0, 3)
            caster = randint(1, 7)
            tipomagico = None
            if classe != '':
                tipomagico = classe
            else:
                if caster == 1:
                    tipomagico = 'Clérigo'
                if caster == 2:
                    tipomagico = 'Mago'
                if caster == 3:
                    tipomagico = 'Druida'
                if caster == 4:
                    tipomagico = 'Bardo'
                if caster == 5:
                    tipomagico = 'Paladino'
                if caster == 6:
                    tipomagico = 'Bruxo'
                if caster == 7:
                    tipomagico = 'Feiticeiro'

        if aptidão_magica == 15:
            feitiços = {'Aptidão Mágica': aptidão_magica,'Classe': tipomagico, 'Truques': truques }
            feitiços['Magias1'] = 0
            feitiços['Magias2'] = 0
            feitiços['Magias3'] = 0
            feitiços['Magias4'] = 0
            feitiços['Magias5'] = 0
            if magias1 > 0:
                feitiços['Magias1']=1
                feitiços['1Círculo'] = magias1
                if magias2 > 0:
                    feitiços['Magias2'] = 1
                    feitiços['2Círculo'] = magias2
                    if magias3 > 0:
                        feitiços['Magias3'] = 1
                        feitiços['3Círculo'] = magias3
                        if magias4 > 0:
                            feitiços['Magias4'] = 1
                            feitiços['4Círculo'] = magias4
                            if magias5 > 0:
                                feitiços['Magias5'] = 1
                                feitiços['5Círculo'] = magias5
        if aptidão_magica == 15:
            return feitiços
        else:
            return {'Aptidão Mágica': 0}

    

    @staticmethod
    def ataques_aleatorios(proef=2, bfor=0, bdes=0, bônusataque=0, bonusdano = 0):
        """
            Randomiza 2 armas e seus ataques
        :param proef: Bônus de proeficiência
        :param bfor: Bônus de Força
        :param bdes: Bônus de Destreza
        :param bônusataque: Bônus de ataque
        :param bonusdano: Bônus de dano
        :return:
        """

        armaslista = [
            f'Adaga. Ataque Corpo-a-Corpo ou a distância com Arma: +{proef + bdes + bônusataque} para atingir, alcance 6/18 m, um alvo.Acerto: {bdes + bonusdano + 3}(1d4 + {bdes + bonusdano}) de dano perfurante.',
            f'Lança. Ataque Corpo-a-Corpo ou a distância com Arma: +{proef + bdes + bônusataque} para atingir, alcance 6/18 m, um alvo.Acerto: {bdes + bonusdano + 5}(1d8 + {bdes + bonusdano}) de dano perfurante.',
            f'Espada Curta. Ataque Corpo-a-Corpo com Arma: +{proef + bfor+ bônusataque} para atingir, alcance 1,5m, um alvo.Acerto: {bfor + bonusdano + 4}(1d6 + {bfor + bonusdano}) de dano perfurante.',
            f'Maça. Ataque Corpo-a-Corpo com Arma: +{proef + bfor + bônusataque} para atingir, alcance 1,5m, um alvo.Acerto: {bfor+ bonusdano + 4}(1d6 + {bfor + bonusdano}) de dano contundente.',
            f'Espada Longa. Ataque Corpo-a-Corpo com Arma: +{proef + bfor+ bônusataque} para atingir, alcance 1,5m, um alvo.Acerto: {bfor + bonusdano + 5}(1d8 + {bfor + bonusdano}) de dano perfurante.',
            f'Arco Longo.Ataque à Distância com Arma: +{proef + bdes + bônusataque} para atingir, distância 45 / 180m, um alvo.Acerto: {5 + bdes + bonusdano}(1d8 + {bdes + bonusdano}) de dano perfurante.']
        ataques = sample(armaslista, k=len(armaslista))
        return {'Ataque1': ataques[0:1], 'Ataque2': ataques[2:3]}

    @staticmethod
    def livro_nd (nd_pretendido = 0):
        """
            Consulta de um ND segundo o livro do mestre
        :param nd_pretendido: nd a ser retornado

        """

        nd_livro = [{'ND': 0, 'Proef': 2, "CA": 13, 'PV': randint(1, 6), 'Pvmin': 1, 'Pvmax': 6, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(0, 1), 'Danomin': 0, 'Danomax': 1, 'CD': 13},
                    {'ND': 1 / 8, 'Proef': 2, "CA": 13, 'PV': randint(7, 35), 'Pvmin': 7, 'Pvmax': 35, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(2, 3), 'Danomin': 2, 'Danomax': 3, 'CD': 13},
                    {'ND': 1 / 4, 'Proef': 2, "CA": 13, 'PV': randint(36, 49), 'Pvmin': 36, 'Pvmax': 49, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(4, 5), 'Danomin': 4, 'Danomax': 5, 'CD': 13},
                    {'ND': 1 / 2, 'Proef': 2, "CA": 13, 'PV': randint(50, 70), 'Pvmin': 50, 'Pvmax': 70, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(6, 8), 'Danomin': 6, 'Danomax': 8, 'CD': 13},
                    {'ND': 1, 'Proef': 2, "CA": 13, 'PV': randint(71, 85), 'Pvmin': 71, 'Pvmax': 85, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(9, 14), 'Danomin': 9, 'Danomax': 14, 'CD': 13},
                    {'ND': 2, 'Proef': 2, "CA": 13, 'PV': randint(86, 100), 'Pvmin': 86, 'Pvmax': 100, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(15, 20), 'Danomin': 15, 'Danomax': 20, 'CD': 13},
                    {'ND': 3, 'Proef': 2, "CA": 13, 'PV': randint(101, 115), 'Pvmin': 101, 'Pvmax': 115, 'Bônus Ataque': 4,
                    'Dano Rodada': randint(21, 26), 'Danomin': 21, 'Danomax': 26, 'CD': 13},
                    {'ND': 4, 'Proef': 2, "CA": 14, 'PV': randint(116, 130), 'Pvmin': 116, 'Pvmax': 130, 'Bônus Ataque': 5,
                    'Dano Rodada': randint(27, 32), 'Danomin': 27, 'Danomax': 32, 'CD': 14},
                    {'ND': 5, 'Proef': 3, "CA": 15, 'PV': randint(131, 145), 'Pvmin': 131, 'Pvmax': 145, 'Bônus Ataque': 6,
                    'Dano Rodada': randint(33, 38), 'Danomin': 33, 'Danomax': 38, 'CD': 15},
                    {'ND': 6, 'Proef': 3, "CA": 15, 'PV': randint(146, 160), 'Pvmin': 146, 'Pvmax': 160, 'Bônus Ataque': 6,
                    'Dano Rodada': randint(39, 44), 'Danomin': 39, 'Danomax': 44, 'CD': 15},
                    {'ND': 7, 'Proef': 3, "CA": 15, 'PV': randint(161, 175), 'Pvmin': 161, 'Pvmax': 175, 'Bônus Ataque': 6,
                    'Dano Rodada': randint(45, 50), 'Danomin': 45, 'Danomax': 50, 'CD': 15},
                    {'ND': 8, 'Proef': 3, "CA": 16, 'PV': randint(176, 190), 'Pvmin': 176, 'Pvmax': 190, 'Bônus Ataque': 7,
                    'Dano Rodada': randint(51, 56), 'Danomin': 51, 'Danomax': 56, 'CD': 16},
                    {'ND': 9, 'Proef': 4, "CA": 16, 'PV': randint(191, 205), 'Pvmin': 191, 'Pvmax': 205, 'Bônus Ataque': 7,
                    'Dano Rodada': randint(57, 62), 'Danomin': 57, 'Danomax': 62, 'CD': 16},
                    {'ND': 10, 'Proef': 4, "CA": 17, 'PV': randint(206, 220), 'Pvmin': 206, 'Pvmax': 220, 'Bônus Ataque': 7,
                    'Dano Rodada': randint(63, 68), 'Danomin': 63, 'Danomax': 68, 'CD': 16},
                    {'ND': 11, 'Proef': +4, "CA": 17, 'PV': randint(221, 235), 'Pvmin': 221, 'Pvmax': 235,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(69, 74), 'Danomin': 69, 'Danomax': 74, 'CD': 17},
                    {'ND': 12, 'Proef': +4, "CA": 17, 'PV': randint(236, 250), 'Pvmin': 236, 'Pvmax': 250,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(75, 80), 'Danomin': 75, 'Danomax': 80, 'CD': 17},
                    {'ND': 13, 'Proef': +5, "CA": 18, 'PV': randint(251, 265), 'Pvmin': 251, 'Pvmax': 265,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(81, 86), 'Danomin': 81, 'Danomax': 86, 'CD': 18},
                    {'ND': 14, 'Proef': +5, "CA": 18, 'PV': randint(266, 280), 'Pvmin': 266, 'Pvmax': 280,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(87, 92), 'Danomin': 87, 'Danomax': 92, 'CD': 18},
                    {'ND': 15, 'Proef': +5, "CA": 18, 'PV': randint(281, 295), 'Pvmin': 281, 'Pvmax': 295,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(93, 98), 'Danomin': 93, 'Danomax': 98, 'CD': 18},
                    {'ND': 16, 'Proef': +5, "CA": 18, 'PV': randint(296, 310), 'Pvmin': 296, 'Pvmax': 310,
                    'Bônus Ataque': 9, 'Dano Rodada': randint(99, 104), 'Danomin': 99, 'Danomax': 104, 'CD': 18},
                    {'ND': 17, 'Proef': +6, "CA": 19, 'PV': randint(311, 325), 'Pvmin': 311, 'Pvmax': 325,
                    'Bônus Ataque': 10, 'Dano Rodada': randint(105, 110), 'Danomin': 105, 'Danomax': 110, 'CD': 19},
                    {'ND': 18, 'Proef': +6, "CA": 19, 'PV': randint(326, 340), 'Pvmin': 326, 'Pvmax': 340,
                    'Bônus Ataque': 10, 'Dano Rodada': randint(111, 116), 'Danomin': 111, 'Danomax': 116, 'CD': 19},
                    {'ND': 19, 'Proef': +6, "CA": 19, 'PV': randint(341, 355), 'Pvmin': 341, 'Pvmax': 355,
                    'Bônus Ataque': 10, 'Dano Rodada': randint(117, 122), 'Danomin': 117, 'Danomax': 122, 'CD': 19},
                    {'ND': 20, 'Proef': +6, "CA": 19, 'PV': randint(356, 400), 'Pvmin': 356, 'Pvmax': 400,
                    'Bônus Ataque': 10, 'Dano Rodada': randint(123, 140), 'Danomin': 123, 'Danomax': 140, 'CD': 19},
                    {'ND': 21, 'Proef': +7, "CA": 19, 'PV': randint(401, 445), 'Pvmin': 401, 'Pvmax': 445,
                    'Bônus Ataque': 11, 'Dano Rodada': randint(141, 158), 'Danomin': 141, 'Danomax': 158, 'CD': 20},
                    {'ND': 22, 'Proef': +7, "CA": 19, 'PV': randint(446, 490), 'Pvmin': 446, 'Pvmax': 490,
                    'Bônus Ataque': 11, 'Dano Rodada': randint(159, 176), 'Danomin': 159, 'Danomax': 176, 'CD': 20},
                    {'ND': 23, 'Proef': +7, "CA": 19, 'PV': randint(491, 535), 'Pvmin': 491, 'Pvmax': 535,
                    'Bônus Ataque': 11, 'Dano Rodada': randint(177, 194), 'Danomin': 177, 'Danomax': 194, 'CD': 20},
                    {'ND': 24, 'Proef': +7, "CA": 19, 'PV': randint(536, 580), 'Pvmin': 536, 'Pvmax': 580,
                    'Bônus Ataque': 11, 'Dano Rodada': randint(195, 212), 'Danomin': 195, 'Danomax': 212, 'CD': 21},
                    {'ND': 25, 'Proef': +8, "CA": 19, 'PV': randint(581, 625), 'Pvmin': 581, 'Pvmax': 625,
                    'Bônus Ataque': 12, 'Dano Rodada': randint(213, 230), 'Danomin': 213, 'Danomax': 230, 'CD': 21},
                    {'ND': 26, 'Proef': +8, "CA": 19, 'PV': randint(626, 670), 'Pvmin': 626, 'Pvmax': 670,
                    'Bônus Ataque': 12, 'Dano Rodada': randint(231, 248), 'Danomin': 231, 'Danomax': 248, 'CD': 21},
                    {'ND': 27, 'Proef': +8, "CA": 19, 'PV': randint(671, 715), 'Pvmin': 671, 'Pvmax': 715,
                    'Bônus Ataque': 13, 'Dano Rodada': randint(249, 266), 'Danomin': 249, 'Danomax': 266, 'CD': 22},
                    {'ND': 28, 'Proef': +8, "CA": 19, 'PV': randint(716, 760), 'Pvmin': 715, 'Pvmax': 760,
                    'Bônus Ataque': 13, 'Dano Rodada': randint(267, 284), 'Danomin': 267, 'Danomax': 284, 'CD': 22},
                    {'ND': 29, 'Proef': +9, "CA": 19, 'PV': randint(761, 805), 'Pvmin': 761, 'Pvmax': 805,
                    'Bônus Ataque': 13, 'Dano Rodada': randint(285, 302), 'Danomin': 285, 'Danomax': 302, 'CD': 22},
                    {'ND': 30, 'Proef': +9, "CA": 19, 'PV': randint(806, 850), 'Pvmin': 806, 'Pvmax': 850,
                    'Bônus Ataque': 14, 'Dano Rodada': randint(303, 320), 'Danomin': 303, 'Danomax': 320, 'CD': 23} ]

        if nd_pretendido == 0:
            nd_pretendido = nd_livro[0]
        elif nd_pretendido == 1/8:
            nd_pretendido = nd_livro[1]
        elif nd_pretendido == 1/4:
            nd_pretendido = nd_livro[2]
        elif nd_pretendido == 1/2:
            nd_pretendido = nd_livro[3]
        elif nd_pretendido > 30:
            nd_pretendido = 30
            nd_pretendido = nd_livro[nd_pretendido+3]
        else:
            nd_pretendido = nd_livro[nd_pretendido+3]
        return nd_pretendido

    @staticmethod
    def nd_resultante (nd_ofensivo=0,  nd_defensivo=0, nd_pretendido=0):
        """
            Retorna ND alterado do ND pretendido com os ajustes de nd ofensivo e defensivo
        :param nd_ofensivo: calculo do nd ofencivo
        :param nd_defensivo:  calculo do nd defensivo
        :param nd_pretendido: retorno do ND correto

        """

        nd_livro = [{'ND': 0, 'Proef': 2, "CA": 13, 'PV': randint(1, 6), 'Pvmin': 1, 'Pvmax': 6, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(0, 1), 'Danomin': 0, 'Danomax': 1, 'CD': 13},
                    {'ND': 1 / 8, 'Proef': 2, "CA": 13, 'PV': randint(7, 35), 'Pvmin': 7, 'Pvmax': 35, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(2, 3), 'Danomin': 2, 'Danomax': 3, 'CD': 13},
                    {'ND': 1 / 4, 'Proef': 2, "CA": 13, 'PV': randint(36, 49), 'Pvmin': 36, 'Pvmax': 49, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(4, 5), 'Danomin': 4, 'Danomax': 5, 'CD': 13},
                    {'ND': 1 / 2, 'Proef': 2, "CA": 13, 'PV': randint(50, 70), 'Pvmin': 50, 'Pvmax': 70, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(6, 8), 'Danomin': 6, 'Danomax': 8, 'CD': 13},
                    {'ND': 1, 'Proef': 2, "CA": 13, 'PV': randint(71, 85), 'Pvmin': 71, 'Pvmax': 85, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(9, 14), 'Danomin': 9, 'Danomax': 14, 'CD': 13},
                    {'ND': 2, 'Proef': 2, "CA": 13, 'PV': randint(86, 100), 'Pvmin': 86, 'Pvmax': 100, 'Bônus Ataque': 3,
                    'Dano Rodada': randint(15, 20), 'Danomin': 15, 'Danomax': 20, 'CD': 13},
                    {'ND': 3, 'Proef': 2, "CA": 13, 'PV': randint(101, 115), 'Pvmin': 101, 'Pvmax': 115, 'Bônus Ataque': 4,
                    'Dano Rodada': randint(21, 26), 'Danomin': 21, 'Danomax': 26, 'CD': 13},
                    {'ND': 4, 'Proef': 2, "CA": 14, 'PV': randint(116, 130), 'Pvmin': 116, 'Pvmax': 130, 'Bônus Ataque': 5,
                    'Dano Rodada': randint(27, 32), 'Danomin': 27, 'Danomax': 32, 'CD': 14},
                    {'ND': 5, 'Proef': 3, "CA": 15, 'PV': randint(131, 145), 'Pvmin': 131, 'Pvmax': 145, 'Bônus Ataque': 6,
                    'Dano Rodada': randint(33, 38), 'Danomin': 33, 'Danomax': 38, 'CD': 15},
                    {'ND': 6, 'Proef': 3, "CA": 15, 'PV': randint(146, 160), 'Pvmin': 146, 'Pvmax': 160, 'Bônus Ataque': 6,
                    'Dano Rodada': randint(39, 44), 'Danomin': 39, 'Danomax': 44, 'CD': 15},
                    {'ND': 7, 'Proef': 3, "CA": 15, 'PV': randint(161, 175), 'Pvmin': 161, 'Pvmax': 175, 'Bônus Ataque': 6,
                    'Dano Rodada': randint(45, 50), 'Danomin': 45, 'Danomax': 50, 'CD': 15},
                    {'ND': 8, 'Proef': 3, "CA": 16, 'PV': randint(176, 190), 'Pvmin': 176, 'Pvmax': 190, 'Bônus Ataque': 7,
                    'Dano Rodada': randint(51, 56), 'Danomin': 51, 'Danomax': 56, 'CD': 16},
                    {'ND': 9, 'Proef': 4, "CA": 16, 'PV': randint(191, 205), 'Pvmin': 191, 'Pvmax': 205, 'Bônus Ataque': 7,
                    'Dano Rodada': randint(57, 62), 'Danomin': 57, 'Danomax': 62, 'CD': 16},
                    {'ND': 10, 'Proef': 4, "CA": 17, 'PV': randint(206, 220), 'Pvmin': 206, 'Pvmax': 220, 'Bônus Ataque': 7,
                    'Dano Rodada': randint(63, 68), 'Danomin': 63, 'Danomax': 68, 'CD': 16},
                    {'ND': 11, 'Proef': +4, "CA": 17, 'PV': randint(221, 235), 'Pvmin': 221, 'Pvmax': 235,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(69, 74), 'Danomin': 69, 'Danomax': 74, 'CD': 17},
                    {'ND': 12, 'Proef': +4, "CA": 17, 'PV': randint(236, 250), 'Pvmin': 236, 'Pvmax': 250,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(75, 80), 'Danomin': 75, 'Danomax': 80, 'CD': 17},
                    {'ND': 13, 'Proef': +5, "CA": 18, 'PV': randint(251, 265), 'Pvmin': 251, 'Pvmax': 265,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(81, 86), 'Danomin': 81, 'Danomax': 86, 'CD': 18},
                    {'ND': 14, 'Proef': +5, "CA": 18, 'PV': randint(266, 280), 'Pvmin': 266, 'Pvmax': 280,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(87, 92), 'Danomin': 87, 'Danomax': 92, 'CD': 18},
                    {'ND': 15, 'Proef': +5, "CA": 18, 'PV': randint(281, 295), 'Pvmin': 281, 'Pvmax': 295,
                    'Bônus Ataque': 8, 'Dano Rodada': randint(93, 98), 'Danomin': 93, 'Danomax': 98, 'CD': 18},
                    {'ND': 16, 'Proef': +5, "CA": 18, 'PV': randint(296, 310), 'Pvmin': 296, 'Pvmax': 310,
                    'Bônus Ataque': 9, 'Dano Rodada': randint(99, 104), 'Danomin': 99, 'Danomax': 104, 'CD': 18},
                    {'ND': 17, 'Proef': +6, "CA": 19, 'PV': randint(311, 325), 'Pvmin': 311, 'Pvmax': 325,
                    'Bônus Ataque': 10, 'Dano Rodada': randint(105, 110), 'Danomin': 105, 'Danomax': 110, 'CD': 19},
                    {'ND': 18, 'Proef': +6, "CA": 19, 'PV': randint(326, 340), 'Pvmin': 326, 'Pvmax': 340,
                    'Bônus Ataque': 10, 'Dano Rodada': randint(111, 116), 'Danomin': 111, 'Danomax': 116, 'CD': 19},
                    {'ND': 19, 'Proef': +6, "CA": 19, 'PV': randint(341, 355), 'Pvmin': 341, 'Pvmax': 355,
                    'Bônus Ataque': 10, 'Dano Rodada': randint(117, 122), 'Danomin': 117, 'Danomax': 122, 'CD': 19},
                    {'ND': 20, 'Proef': +6, "CA": 19, 'PV': randint(356, 400), 'Pvmin': 356, 'Pvmax': 400,
                    'Bônus Ataque': 10, 'Dano Rodada': randint(123, 140), 'Danomin': 123, 'Danomax': 140, 'CD': 19},
                    {'ND': 21, 'Proef': +7, "CA": 19, 'PV': randint(401, 445), 'Pvmin': 401, 'Pvmax': 445,
                    'Bônus Ataque': 11, 'Dano Rodada': randint(141, 158), 'Danomin': 141, 'Danomax': 158, 'CD': 20},
                    {'ND': 22, 'Proef': +7, "CA": 19, 'PV': randint(446, 490), 'Pvmin': 446, 'Pvmax': 490,
                    'Bônus Ataque': 11, 'Dano Rodada': randint(159, 176), 'Danomin': 159, 'Danomax': 176, 'CD': 20},
                    {'ND': 23, 'Proef': +7, "CA": 19, 'PV': randint(491, 535), 'Pvmin': 491, 'Pvmax': 535,
                    'Bônus Ataque': 11, 'Dano Rodada': randint(177, 194), 'Danomin': 177, 'Danomax': 194, 'CD': 20},
                    {'ND': 24, 'Proef': +7, "CA": 19, 'PV': randint(536, 580), 'Pvmin': 536, 'Pvmax': 580,
                    'Bônus Ataque': 11, 'Dano Rodada': randint(195, 212), 'Danomin': 195, 'Danomax': 212, 'CD': 21},
                    {'ND': 25, 'Proef': +8, "CA": 19, 'PV': randint(581, 625), 'Pvmin': 581, 'Pvmax': 625,
                    'Bônus Ataque': 12, 'Dano Rodada': randint(213, 230), 'Danomin': 213, 'Danomax': 230, 'CD': 21},
                    {'ND': 26, 'Proef': +8, "CA": 19, 'PV': randint(626, 670), 'Pvmin': 626, 'Pvmax': 670,
                    'Bônus Ataque': 12, 'Dano Rodada': randint(231, 248), 'Danomin': 231, 'Danomax': 248, 'CD': 21},
                    {'ND': 27, 'Proef': +8, "CA": 19, 'PV': randint(671, 715), 'Pvmin': 671, 'Pvmax': 715,
                    'Bônus Ataque': 13, 'Dano Rodada': randint(249, 266), 'Danomin': 249, 'Danomax': 266, 'CD': 22},
                    {'ND': 28, 'Proef': +8, "CA": 19, 'PV': randint(716, 760), 'Pvmin': 715, 'Pvmax': 760,
                    'Bônus Ataque': 13, 'Dano Rodada': randint(267, 284), 'Danomin': 267, 'Danomax': 284, 'CD': 22},
                    {'ND': 29, 'Proef': +9, "CA": 19, 'PV': randint(761, 805), 'Pvmin': 761, 'Pvmax': 805,
                    'Bônus Ataque': 13, 'Dano Rodada': randint(285, 302), 'Danomin': 285, 'Danomax': 302, 'CD': 22},
                    {'ND': 30, 'Proef': +9, "CA": 19, 'PV': randint(806, 850), 'Pvmin': 806, 'Pvmax': 850,
                    'Bônus Ataque': 14, 'Dano Rodada': randint(303, 320), 'Danomin': 303, 'Danomax': 320, 'CD': 23}]
        if nd_pretendido == 0:
            nd_pretendido = nd_livro[0]
        elif nd_pretendido == 1/8:
            nd_pretendido = nd_livro[1]
        elif nd_pretendido == 1/4:
            nd_pretendido = nd_livro[2]
        elif nd_pretendido == 1/2:
            nd_pretendido = nd_livro[3]
        elif nd_pretendido > 30:
            nd_pretendido = 30
            nd_pretendido = nd_livro[nd_pretendido+3]
        else:
            nd_pretendido = nd_livro[nd_pretendido+3]

        nd_resultante = floor(((nd_ofensivo + nd_defensivo) / 2) + nd_pretendido['ND'])
        
        if nd_resultante == 0:
            nd_resultante = nd_livro[0]
        elif nd_resultante == 1 / 8:
            nd_resultante = nd_livro[1]
        elif nd_resultante == 1 / 4:
            nd_resultante = nd_livro[2]
        elif nd_resultante == 1 / 2:
            nd_resultante = nd_livro[3]
        elif nd_resultante > 30:
            nd_resultante = 30
            nd_resultante = nd_livro[nd_resultante + 3]
        else:
            nd_resultante = nd_livro[nd_resultante + 3]

        return nd_resultante['ND']


    
    

    @staticmethod
    def vantagem(bonus=0):
        """
        Função para resolver parada de dados de vantagem

            :param bonus: Número a ser somado ao resultado
            :return: informação sobre a rolagem
        """
        global retorno
    

        rolagem_final = []
        parada_de_dados = []

        dado1 = randint(1, 20)
        dado2 = randint(1, 20)
        vantagem = [dado1, dado2]
        rolagem_final.append(max(vantagem))
        parada_de_dados.append(vantagem)


        if bonus != 0:
            retorno = f'As jogadas foram{parada_de_dados}. Final {rolagem_final} + {bonus}, Total {sum(rolagem_final) + bonus}'
        else:
            retorno = f'As jogadas foram{parada_de_dados}. Final {rolagem_final}, Total {sum(rolagem_final)}'

        return retorno

    @staticmethod
    def desvantagem(bonus=0):
        """
        Função para resolver parada de dados de desvantagem

            :param desvantagem: Se a funão vantagem ésetada como True, são jogados 2 dados de 20 lados e o resultado é o menor
            :return: informação sobre a rolagem
        """
        global retorno


        rolagem_final = []
        parada_de_dados = []

        dado1 = randint(1, 20)
        dado2 = randint(1, 20)
        vantagem = [dado1, dado2]
        rolagem_final.append(min(vantagem))
        parada_de_dados.append(vantagem)


        if bonus != 0:
            retorno = f'As jogadas foram{parada_de_dados}. Final {rolagem_final} + {bonus}, Total {sum(rolagem_final) + bonus}'
        else:
            retorno = f'As jogadas foram{parada_de_dados}. Final {rolagem_final}, Total {sum(rolagem_final)}'

        return retorno

    @staticmethod
    def calcular_nd(nome = 'Indefinido', nd_pretendido=0, ca=0, pv=0, b_ataque=0, dano_rodada=0, dano_area = False, n_ataques =1, cd=0, vôo=False, resist=False, imunidade=False, ação_ardilosa=False, aparar=False, matilha = False):
        """
        Faciclita a criação ou verificação do nível de desafio de um oponente

            nome = Nome da criatura/npc a ser analizado
            nd_pretendido - Refere-se ao Nível de desafio base
            ca - Refere-se a Classe de Armadura
            pv - Refere-se aos Pontos de Vida
            b_ataque - Refere-se ao Bônus de Ataque
            dano_rodada - Refere-se a quantidade máxima de dano causado
            dano_area - Refere-se a capacidade de causar dano em área
            n_ataques - Refere-se ao Número de Ataques
            cd - Refere-se a Dificuldade para testesde resistência de uma habilidade
            vôo - Refere-se acapacidade de Vôo de uma criatura. Por padão está em False, se alterado para True a criatura tem movimentação de vôo.
            resist - Refere-se as resistências a dano de uma criatura. Por padrão está em False, se alterado para True a criatura possui resistências.
            imunidade - Refere-se a Imunidades de uma criatura. Por padrão está em False, se alterado para True a criatura possui imunidade.
            ação_ardilosa - Refere-se ao bônus referente a uma Ação Ardilosa de uma criatura. Por padão está em False, se alterado para True a criatura possui esta habilidade.
            aparar- Refere-se a caacidade de usar a reação Aparar uma criatura. Por padão está em False, se alterado para True a criatura possui esta habilidade.
            matilha - Refere-se ao bônus referente a ataques em grupo de uma criatura. Por padão está em False, se alterado para True a criatura possui esta habilidade.

        """

        nd_defensivo = nd_ofensivo = nd_resultante = 0
        #Nd de Referência do Livro
        nd_livro = [  {'ND': 0, 'Proef': 2, "CA": 13, 'PV': randint(1, 6), 'Pvmin': 1, 'Pvmax': 6, 'Bônus Ataque': 3, 'Dano Rodada': randint(0, 1), 'Danomin': 0, 'Danomax': 1,'CD': 13},
            {'ND': 1/8, 'Proef': 2, "CA": 13, 'PV': randint(7, 35), 'Pvmin': 7, 'Pvmax': 35,'Bônus Ataque': 3, 'Dano Rodada': randint(2, 3),'Danomin': 2, 'Danomax': 3, 'CD': 13},
            {'ND': 1/4, 'Proef': 2, "CA": 13, 'PV': randint(36, 49), 'Pvmin': 36, 'Pvmax': 49,'Bônus Ataque': 3, 'Dano Rodada': randint(4, 5), 'Danomin': 4, 'Danomax': 5,'CD': 13},
            {'ND': 1/2, 'Proef': 2, "CA": 13, 'PV': randint(50, 70), 'Pvmin': 50, 'Pvmax': 70,'Bônus Ataque': 3, 'Dano Rodada': randint(6, 8), 'Danomin': 6, 'Danomax': 8,'CD': 13},
            {'ND': 1, 'Proef': 2, "CA": 13, 'PV': randint(71, 85), 'Pvmin': 71, 'Pvmax': 85,'Bônus Ataque': 3, 'Dano Rodada': randint(9, 14), 'Danomin': 9, 'Danomax': 14,'CD': 13},
            {'ND': 2, 'Proef': 2, "CA": 13, 'PV': randint(86, 100), 'Pvmin': 86, 'Pvmax': 100,'Bônus Ataque': 3, 'Dano Rodada': randint(15, 20), 'Danomin': 15, 'Danomax': 20,'CD': 13},
            {'ND': 3, 'Proef': 2, "CA": 13, 'PV': randint(101, 115), 'Pvmin': 101, 'Pvmax': 115,'Bônus Ataque': 4, 'Dano Rodada': randint(21, 26), 'Danomin': 21, 'Danomax': 26,'CD': 13},
            {'ND': 4, 'Proef': 2, "CA": 14, 'PV': randint(116, 130), 'Pvmin': 116, 'Pvmax': 130,'Bônus Ataque': 5, 'Dano Rodada': randint(27, 32), 'Danomin': 27, 'Danomax': 32,'CD': 14},
            {'ND': 5, 'Proef': 3, "CA": 15, 'PV': randint(131, 145), 'Pvmin': 131, 'Pvmax': 145,'Bônus Ataque': 6, 'Dano Rodada': randint(33, 38), 'Danomin': 33, 'Danomax': 38,'CD': 15},
            {'ND': 6, 'Proef': 3, "CA": 15, 'PV': randint(146, 160), 'Pvmin': 146, 'Pvmax': 160,'Bônus Ataque': 6, 'Dano Rodada': randint(39, 44), 'Danomin': 39, 'Danomax': 44,'CD': 15},
            {'ND': 7, 'Proef': 3, "CA": 15, 'PV': randint(161, 175), 'Pvmin': 161, 'Pvmax': 175,'Bônus Ataque': 6, 'Dano Rodada': randint(45, 50), 'Danomin': 45, 'Danomax': 50,'CD': 15},
            {'ND': 8, 'Proef': 3, "CA": 16, 'PV': randint(176, 190), 'Pvmin': 176, 'Pvmax': 190,'Bônus Ataque': 7, 'Dano Rodada': randint(51, 56), 'Danomin': 51, 'Danomax': 56,'CD': 16},
            {'ND': 9, 'Proef': 4, "CA": 16, 'PV': randint(191, 205), 'Pvmin': 191, 'Pvmax': 205,'Bônus Ataque': 7, 'Dano Rodada': randint(57, 62), 'Danomin': 57, 'Danomax': 62,'CD': 16},
            {'ND': 10, 'Proef': 4, "CA": 17, 'PV': randint(206, 220), 'Pvmin': 206, 'Pvmax': 220,'Bônus Ataque': 7, 'Dano Rodada': randint(63, 68), 'Danomin': 63, 'Danomax': 68,'CD': 16},
            {'ND': 11, 'Proef': +4, "CA": 17, 'PV': randint(221, 235), 'Pvmin': 221, 'Pvmax': 235,'Bônus Ataque': 8, 'Dano Rodada': randint(69, 74), 'Danomin': 69, 'Danomax': 74,'CD': 17},
            {'ND': 12, 'Proef': +4, "CA": 17, 'PV': randint(236, 250), 'Pvmin': 236, 'Pvmax': 250,'Bônus Ataque': 8, 'Dano Rodada': randint(75, 80), 'Danomin': 75, 'Danomax': 80,'CD': 17},
            {'ND': 13, 'Proef': +5, "CA": 18, 'PV': randint(251, 265), 'Pvmin': 251, 'Pvmax': 265,'Bônus Ataque': 8, 'Dano Rodada': randint(81, 86), 'Danomin': 81, 'Danomax': 86,'CD': 18},
            {'ND': 14, 'Proef': +5, "CA": 18, 'PV': randint(266, 280), 'Pvmin': 266, 'Pvmax': 280,'Bônus Ataque': 8, 'Dano Rodada': randint(87, 92), 'Danomin': 87, 'Danomax': 92,'CD': 18},
            {'ND': 15, 'Proef': +5, "CA": 18, 'PV': randint(281, 295), 'Pvmin': 281, 'Pvmax': 295,'Bônus Ataque': 8, 'Dano Rodada': randint(93, 98), 'Danomin': 93, 'Danomax': 98,'CD': 18},
            {'ND': 16, 'Proef': +5, "CA": 18, 'PV': randint(296, 310), 'Pvmin': 296, 'Pvmax': 310,'Bônus Ataque': 9, 'Dano Rodada': randint(99, 104), 'Danomin': 99, 'Danomax': 104,'CD': 18},
            {'ND': 17, 'Proef': +6, "CA": 19, 'PV': randint(311, 325), 'Pvmin': 311, 'Pvmax': 325,'Bônus Ataque': 10, 'Dano Rodada': randint(105, 110), 'Danomin': 105, 'Danomax': 110,'CD': 19},
            {'ND': 18, 'Proef': +6, "CA": 19, 'PV': randint(326, 340), 'Pvmin': 326, 'Pvmax': 340,'Bônus Ataque': 10, 'Dano Rodada': randint(111, 116), 'Danomin': 111, 'Danomax': 116,'CD': 19},
            {'ND': 19, 'Proef': +6, "CA": 19, 'PV': randint(341, 355), 'Pvmin': 341, 'Pvmax': 355,'Bônus Ataque': 10, 'Dano Rodada': randint(117, 122), 'Danomin': 117, 'Danomax': 122,'CD': 19},
            {'ND': 20, 'Proef': +6, "CA": 19, 'PV': randint(356, 400), 'Pvmin': 356, 'Pvmax': 400,'Bônus Ataque': 10, 'Dano Rodada': randint(123, 140), 'Danomin': 123, 'Danomax': 140,'CD': 19},
            {'ND': 21, 'Proef': +7, "CA": 19, 'PV': randint(401, 445), 'Pvmin': 401, 'Pvmax': 445,'Bônus Ataque': 11, 'Dano Rodada': randint(141, 158), 'Danomin': 141, 'Danomax': 158,'CD': 20},
            {'ND': 22, 'Proef': +7, "CA": 19, 'PV': randint(446, 490), 'Pvmin': 446, 'Pvmax': 490,'Bônus Ataque': 11, 'Dano Rodada': randint(159, 176), 'Danomin': 159, 'Danomax': 176,'CD': 20},
            {'ND': 23, 'Proef': +7, "CA": 19, 'PV': randint(491, 535), 'Pvmin': 491, 'Pvmax': 535,'Bônus Ataque': 11, 'Dano Rodada': randint(177, 194), 'Danomin': 177, 'Danomax': 194,'CD': 20},
            {'ND': 24, 'Proef': +7, "CA": 19, 'PV': randint(536, 580), 'Pvmin': 536, 'Pvmax': 580,'Bônus Ataque': 11, 'Dano Rodada': randint(195, 212), 'Danomin': 195, 'Danomax': 212,'CD': 21},
            {'ND': 25, 'Proef': +8, "CA": 19, 'PV': randint(581, 625), 'Pvmin': 581, 'Pvmax': 625,'Bônus Ataque': 12, 'Dano Rodada': randint(213, 230), 'Danomin': 213, 'Danomax': 230,'CD': 21},
            {'ND': 26, 'Proef': +8, "CA": 19, 'PV': randint(626, 670), 'Pvmin': 626, 'Pvmax': 670,'Bônus Ataque': 12, 'Dano Rodada': randint(231, 248), 'Danomin': 231, 'Danomax': 248,'CD': 21},
            {'ND': 27, 'Proef': +8, "CA": 19, 'PV': randint(671, 715), 'Pvmin': 671, 'Pvmax': 715,'Bônus Ataque': 13, 'Dano Rodada': randint(249, 266), 'Danomin': 249, 'Danomax': 266,'CD': 22},
            {'ND': 28, 'Proef': +8, "CA": 19, 'PV': randint(716, 760), 'Pvmin': 715, 'Pvmax': 760,'Bônus Ataque': 13, 'Dano Rodada': randint(267, 284), 'Danomin': 267, 'Danomax': 284,'CD': 22},
            {'ND': 29, 'Proef': +9, "CA": 19, 'PV': randint(761, 805), 'Pvmin': 761, 'Pvmax': 805,'Bônus Ataque': 13, 'Dano Rodada': randint(285, 302), 'Danomin': 285, 'Danomax': 302,'CD': 22},
            {'ND': 30, 'Proef': +9, "CA": 19, 'PV': randint(806, 850), 'Pvmin': 806, 'Pvmax': 850,'Bônus Ataque': 14, 'Dano Rodada': randint(303, 320), 'Danomin': 303, 'Danomax': 320,'CD': 23},]
        # Setup do ND pretendido
        if nd_pretendido == 0:
            nd_pretendido = nd_livro[0]
        elif nd_pretendido == 1/8:
            nd_pretendido = nd_livro[1]
        elif nd_pretendido == 1/4:
            nd_pretendido = nd_livro[2]
        elif nd_pretendido == 1/2:
            nd_pretendido = nd_livro[3]
        elif nd_pretendido > 30:
            nd_pretendido = 30
            nd_pretendido = nd_livro[nd_pretendido+3]
        else:
            nd_pretendido = nd_livro[nd_pretendido+3]
        # Setup das informações contidas
        if ca == 0:
            ca = nd_pretendido['CA']
        if pv == 0:
            pv = nd_pretendido['PV']
        if b_ataque == 0:
            b_ataque = nd_pretendido['Bônus Ataque']
        if dano_rodada ==0:
            dano_rodada = nd_pretendido['Dano Rodada']
        if cd == 0:
            cd = nd_pretendido['CD']

        # Início das Análise das capacidades
        nd_defensivo = 0
        nd_ofensivo = 0

        #Teste CA
        if ca > nd_pretendido['CA']:
            nd_defensivo += floor((ca - nd_pretendido['CA'])/2)
        if ca < nd_pretendido['CA']:
            nd_defensivo -= floor((nd_pretendido['CA'] - ca)/2)
        if vôo == True:
            nd_defensivo += 1
        if ação_ardilosa == True:
            nd_defensivo += 2
        if aparar == True:
            nd_defensivo += 1

        # Teste Pv
        count_pv = 0
        pv_efetivo = pv
        # VULNERABILIDADE, RESISTÊNCIA E IMUNIDADE A DANO
        # Nível de Desafio Pretendido     Multiplicador de PV por Resistências    Multiplicador de PV por Imunidades
        # 1–4                                             X 2                               X 2
        # 5–10                                            X 1,5                             X 2
        # 11–16                                           X 1,25                           X 1,5
        # 17 ou maior                                     X 1                              X 1,25

        if resist == True:
            if 0 <= nd_pretendido['ND'] <= 4:
                pv_efetivo = pv * 2
            elif 5 <= nd_pretendido['ND'] <= 10:
                pv_efetivo = pv * 1.5
            elif 11 <= nd_pretendido['ND'] <= 16:
                pv_efetivo = pv * 1.25
            elif nd_pretendido['ND'] > 17:
                pv_efetivo = pv * 1

        if imunidade == True:
            if 0 <= nd_pretendido['ND'] <= 4:
                pv_efetivo = pv * 2
            elif 5 <= nd_pretendido['ND'] <= 10:
                pv_efetivo = pv * 2
            elif 11 <= nd_pretendido['ND'] <= 16:
                pv_efetivo = pv * 1.5
            elif nd_pretendido['ND'] > 17:
                pv_efetivo = pv * 1.25

        if nd_pretendido['Pvmin']> pv_efetivo or pv_efetivo > nd_pretendido['Pvmax']:
            for c in  nd_livro:
                if c['Pvmin']<= pv_efetivo <= c['Pvmax']:
                    if nd_pretendido['ND'] < c['ND']:
                        nd_defensivo += (c['ND'] - nd_pretendido['ND'])
                    if nd_pretendido['ND'] > c['ND']:
                        if c['ND']==0 :
                            nd_defensivo -= (nd_pretendido['ND']) +4
                        elif count_pv == 1 :
                            nd_defensivo -= (nd_pretendido['ND']) +3
                        elif count_pv == 2 :
                            nd_defensivo -= (nd_pretendido['ND']) +2
                        elif count_pv == 3 :
                            nd_defensivo -= (nd_pretendido['ND']) +1
                        elif count_pv >= 4:
                            nd_defensivo -= (nd_pretendido['ND'] - c['ND'])
                count_pv +=1

        # Teste Ataque
        if matilha ==True:
            nd_ofensivo +=1

        if b_ataque > nd_pretendido['Bônus Ataque']:
            nd_ofensivo += floor((b_ataque - nd_pretendido['Bônus Ataque']) / 2)
        if b_ataque < nd_pretendido['Bônus Ataque']:
            b_ataque -= floor((nd_pretendido['Bônus Ataque'] - b_ataque) / 2)
        # Teste Dano 'Danomin' 'Danomax'
        count_dano = 0
        if nd_pretendido['Danomin']> dano_rodada or pv > nd_pretendido['Danomax']:
            for c in  nd_livro:
                if c['Danomin']<= dano_rodada <= c['Danomax']:
                    if nd_pretendido['ND'] < c['ND']:
                        nd_ofensivo += (c['ND'] - nd_pretendido['ND'])
                    if nd_pretendido['ND'] > c['ND']:
                        if c['ND']==0 :
                            nd_ofensivo -= (nd_pretendido['ND']) +4
                        elif count_dano == 1 :
                            nd_ofensivo -= (nd_pretendido['ND']) +3
                        elif count_dano == 2 :
                            nd_ofensivo -= (nd_pretendido['ND']) +2
                        elif count_dano == 3 :
                            nd_ofensivo -= (nd_pretendido['ND']) +1
                        elif count_dano >= 4:
                            nd_ofensivo -= (nd_pretendido['ND'] - c['ND'])
                count_dano +=1
        # Teste CD
        if cd > nd_pretendido['CD']:
            nd_ofensivo += (cd - nd_pretendido['CD'])
        if cd < nd_pretendido['CD']:
            b_ataque -= (nd_pretendido['CD'] - cd)

        #Resultados
        nd_resultante = floor(((nd_ofensivo + nd_defensivo) / 2) + nd_pretendido['ND'])
        if nd_resultante == 0:
            nd_resultante = nd_livro[0]
        elif nd_resultante == 1/8:
            nd_resultante = nd_livro[1]
        elif nd_resultante == 1/4:
            nd_resultante = nd_livro[2]
        elif nd_resultante == 1/2:
            nd_resultante = nd_livro[3]
        elif nd_resultante > 30:
            nd_resultante = 30
            nd_resultante = nd_livro[nd_resultante+3]
        else:
            nd_resultante = nd_livro[nd_resultante+3]
        #Criação do Retorno
        criação = {'Nome': nome, 'CA':ca, 'PV': pv, 'Proeficiência': nd_resultante['Proef'], 'Bônus Ataque': b_ataque,
                'Dano Rodada': dano_rodada, 'Números de ataques': n_ataques, 'Dano por ataque': dano_rodada/n_ataques,
                'CD': cd}
        if  dano_area == True:
            criação['Dano em área']= floor(dano_rodada/2)
        if vôo == True:
            criação['Vôo'] = 'Ativo'
        if resist == True:
            criação['Resistência'] = 'Ativo'
        if imunidade == True:
            criação['Imunidade'] = 'Ativo'
        if ação_ardilosa == True:
            criação['Ação Ardilosa'] = 'Ativo'
        if aparar == True:
            criação['Aparar'] = 'Ativo'
        if matilha == True:
            criação['Matilha'] = 'Ativo'
        criação['ND'] = nd_resultante['ND']

        return criação

    @staticmethod
    def npc(nd =0 ,nome_npc="", raça = '', tendencia='', força = 0 ,destreza = 0, constituição = 0, inteligencia = 0 ,sabedoria = 0 , carisma = 0, ca = 0, pv = 0, magia =False, classe = '', cd = 0 ):

        if nd ==0:
            nd = randint(0, 5)
        nd = RPGController.livro_nd(nd)

        if nome_npc =='':
            nome_npc = RPGController.nome_aleatório()
        if raça == '':
            raça = RPGController.raça_aleatória()
        if tendencia =='':
            tendencia = RPGController.tendência_aleatória()
        personagem = nome_npc
        atributos = RPGController.gerar_atributos(força, destreza, constituição, inteligencia, sabedoria, carisma)
        força= atributos['Força'][0]
        bfor= atributos['Força'][1]
        destreza= atributos['Destreza'][0]
        bdes = atributos['Destreza'][1]
        constituição= atributos['Constituição'][0]
        bcon = atributos['Constituição'][1]
        inteligencia= atributos['Inteligência'][0]
        bint = atributos['Inteligência'][1]
        sabedoria= atributos['Sabedoria'][0]
        bsab = atributos['Sabedoria'][1]
        carisma= atributos['Carisma'][0]
        bcar = atributos['Carisma'][1]
        proef = nd['Proef']

        if ca == 0:
            ca = randint(nd['CA']-1, nd['CA']+2)
        if pv == 0:
            pv = nd['PV']
        if cd == 0:
            cd = nd['CD']

        save = RPGController.saves_aleatorios(proef= nd['Proef'] , bfor= atributos['Força'][1] , bdes=atributos['Destreza'][1], bcon=atributos['Constituição'][1], bint=atributos['Inteligência'][1], bsab=atributos['Sabedoria'][1], bcar=atributos['Carisma'][1])

        perícias = RPGController.pericias_aleatorias(proef= nd['Proef'] , bfor= atributos['Força'][1] , bdes=atributos['Destreza'][1], bcon=atributos['Constituição'][1], bint=atributos['Inteligência'][1], bsab=atributos['Sabedoria'][1], bcar=atributos['Carisma'][1])

        n_de_ataques = floor(nd['Dano Rodada']/7)

        bônusataque = bonusdano = 0
        if n_de_ataques >3:
            n_de_ataques = floor(nd['Dano Rodada']/12)
            bônusataque = 2
            bonusdano = 4
            if n_de_ataques > 3:
                n_de_ataques = floor(nd['Dano Rodada']/16)
                bônusataque = 4
                bonusdano = 8

        if bônusataque > 0:
            ataques = RPGController.ataques_aleatorios(proef=nd['Proef'], bfor=atributos['Força'][1], bdes=atributos['Destreza'][1], bônusataque= bônusataque , bonusdano= bonusdano)
        else:
            ataques = RPGController.ataques_aleatorios(proef= nd['Proef'] , bfor= atributos['Força'][1] , bdes=atributos['Destreza'][1])

        if magia:
            if classe == '':
                feitiços = RPGController.aptidão_mágica(magia=True)
            else:
                feitiços = RPGController.aptidão_mágica(magia=True, classe = classe)
        else:
            feitiços = RPGController.aptidão_mágica()

        npc_gerado = {'Nome': personagem,
                    'Raça': raça,
                    'Tendência': tendencia,
                    'Proeficiência': nd['Proef'],
                    'PV': pv,
                    'Classe de Armadura': ca,
                    'Atributos': {'Força': [força, (força - 10) // 2],
                    'Destreza': [destreza, (destreza - 10) // 2],
                    'Constituição': [constituição, (constituição - 10) // 2],
                    'Inteligência': [inteligencia, (inteligencia - 10) // 2],
                    'Sabedoria': [sabedoria, (sabedoria - 10) // 2],
                    'Carisma': [carisma, (carisma - 10) // 2]},
                    'Saves': save,
                    'Perícias': perícias,
                    'Número de ataques': n_de_ataques,
                    'Ataque1': ataques['Ataque1'],
                    'Ataque2': ataques['Ataque2'],
                    'CD': cd}

        nd = RPGController.calcular_nd(nome=npc_gerado['Nome'], nd_pretendido=1, pv=npc_gerado['PV'], ca=npc_gerado['Classe de Armadura'],
                        b_ataque= max(nd['Proef'] + bfor + bônusataque, nd['Proef'] + bdes + bônusataque), dano_rodada=npc_gerado['Número de ataques']*(6+bonusdano))

        if feitiços['Aptidão Mágica'] == 15:
            npc_gerado['Tipo de magia'] = feitiços['Classe']
            npc_gerado['Truques'] = feitiços['Truques']
            if feitiços['Magias1'] > 0:
                npc_gerado['1° Círculo'] = feitiços['Magias1']
                if feitiços['Magias2']> 0:
                    npc_gerado['2° Círculo'] =  feitiços['Magias2']
                    if feitiços['Magias3']> 0:
                        npc_gerado['3° Círculo'] =  feitiços['Magias3']
                        if feitiços['Magias4'] > 0:
                            npc_gerado['4° Círculo'] = feitiços['Magias4']
                            if feitiços['Magias5'] > 0:
                                npc_gerado['5° Círculo'] = feitiços['Magias5']

        npc_gerado['ND'] = nd['ND']
        return npc_gerado



