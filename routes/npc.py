from flask import Blueprint, render_template, request, redirect, flash, url_for, jsonify
from controller.user_controller import UserController
from controller.npc_controller import NPCController
from extensions import login_manager
from flask_login import login_user, logout_user
from controller.rpgcontroller import RPGController

blueprint_npc = Blueprint("npc", __name__, template_folder="templates")

@blueprint_npc.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('npc_aleatotio.html')
    
    if request.method == 'POST':
        # Recuperando os dados do formulário
        npc_nome = request.form.get('npc_nome')


        template = request.form.get('template')  
        
        raca = request.form.get('raca')
        if raca == 'outro':
            raca = request.form.get('raca-custom')

        
        tendencia = request.form.get('tendencia')
        
        genero = request.form.get('genero')

        ca = request.form.get('ca')
        pv = request.form.get('pv')
        dadosvida = request.form.get('dadosvida')
        speed = request.form.get('speed')
        voo = request.form.get('voo')
        natacao = request.form.get('natacao')
        darkvision = request.form.get('darkvision')
        classe_base = request.form.get('classe_base')
        nd = request.form.get('nd')
        saves=request.form.get('saves')
        forca = request.form.get('força')
        save_forca = request.form.get('saveforca')
        destreza = request.form.get('destreza')
        save_destreza = request.form.get('savedestreza')
        constituicao = request.form.get('constituição')
        save_constituicao = request.form.get('saveconstituicao')
        sabedoria = request.form.get('sabedoria')
        save_sabedoria = request.form.get('savesabedoria')
        inteligencia = request.form.get('inteligência')
        save_inteligencia = request.form.get('saveinteligencia')
        carisma = request.form.get('carisma')
        save_carisma = request.form.get('savecarisma')
        classe = request.form.get('classe_base')


        resistencia = request.form.get('resistencia') == 'on'
        resistencias= []
        resistencia_acido = request.form.get('resistenciaacido') == 'on'
        resistencia_concussao = request.form.get('resistenciaconcussao') == 'on'
        resistencia_cortante = request.form.get('resistenciacortante') == 'on'
        resistencia_eletrico = request.form.get('resistenciaeletrico') == 'on'
        resistencia_energia = request.form.get('resistenciaenergia') == 'on'
        resistencia_fogo = request.form.get('resistenciafogo') == 'on'
        resistencia_frio = request.form.get('resistenciafrio') == 'on'
        resistencia_necronico = request.form.get('resistencianecronico') == 'on'
        resistencia_perfurante = request.form.get('resistenciaperfurante') == 'on'
        resistencia_psiquico = request.form.get('resistenciapsiquico') == 'on'
        resistencia_radiante = request.form.get('resistenciaradiante') == 'on'
        resistencia_trovejante = request.form.get('resistenciatrovejante') == 'on'
        resistencia_veneno = request.form.get('resistenciaveneno') == 'on'
        resistencia_n_magico = request.form.get('resistataques_n_magico') == 'on'
        resistencia_n_magico = request.form.get('resistmagia') == 'on'
        
        
        
        
        if resistencia_acido:
             resistencias.append('Ácido')
        if resistencia_concussao:
            resistencias.append('Concussão')
        if resistencia_cortante:
            resistencias.append('Cortante')
        if resistencia_eletrico:
            resistencias.append('Elétrico')
        if resistencia_energia:
            resistencias.append('Energia')
        if resistencia_fogo:
            resistencias.append('Fogo')
        if resistencia_frio:
            resistencias.append('Frio')
        if resistencia_necronico:
            resistencias.append('Necrótico')
        if resistencia_perfurante:
            resistencias.append('Perfurante')
        if resistencia_psiquico:
            resistencias.append('Psíquico')
        if resistencia_radiante:
            resistencias.append('Radiante')
        if resistencia_trovejante:
            resistencias.append('Trovejante')
        if resistencia_veneno:
            resistencias.append('Veneno')
        if resistencia_n_magico:
            resistencias.append('Ataques Não-mágicos')
        if resistencia_n_magico:
            resistencias.append('Magia')


        imunidade = request.form.get('imunidade') == 'on'
        imunidades = []

        imunidade_agarrado = request.form.get('imunidadeagarrado') == 'on'
        imunidade_amedrontado = request.form.get('imunidadeamedrontado') == 'on'
        imunidade_atordoado = request.form.get('imunidadeatordoado') == 'on'
        imunidade_caido = request.form.get('imunidadecaido') == 'on'
        imunidade_cego = request.form.get('imunidadecego') == 'on'
        imunidade_enfeitiçado = request.form.get('imunidadeenfeitiçado') == 'on'
        imunidade_envenenado = request.form.get('imunidadeenvenenado') == 'on'
        imunidade_impedido = request.form.get('imunidadeimpedido') == 'on'
        imunidade_incapacitado = request.form.get('imunidadeincapacitado') == 'on'
        imunidade_inconsciente = request.form.get('imunidadeinconsciente') == 'on'
        imunidade_invisivel = request.form.get('imunidadeinvisivel') == 'on'
        imunidade_paralisado = request.form.get('imunidadeparalisado') == 'on'
        imunidade_petrificado = request.form.get('imunidadepetrificado') == 'on'
        imunidade_surdo = request.form.get('imunidadesurdo') == 'on'
        imunidade_acido = request.form.get('imunidadeacido') == 'on'
        imunidade_concussao = request.form.get('imunidadeconcussao') == 'on'
        imunidade_cortante = request.form.get('imunidadecortante') == 'on'
        imunidade_eletrico = request.form.get('imunidadeeletrico') == 'on'
        imunidade_energia = request.form.get('imunidadeenergia') == 'on'
        imunidade_fogo = request.form.get('imunidadefogo') == 'on'
        imunidade_frio = request.form.get('imunidadefrio') == 'on'
        imunidade_necronico = request.form.get('imunididanecronico') == 'on'
        imunidade_perfurante = request.form.get('imunidadeperfurante') == 'on'
        imunidade_psiquico = request.form.get('imunidadepsiquico') == 'on'
        imunidade_radiante = request.form.get('imunidaderadiante') == 'on'
        imunidade_trovejante = request.form.get('imunidadetrovejante') == 'on'
        imunidade_veneno = request.form.get('imunidadeveneno') == 'on'
        imunidade_nmagicos = request.form.get('imunidade_nmagicos') == 'on'
        imunidade_magia = request.form.get('imunidade_magia') == 'on'

        # Adiciona à lista apenas se o campo estiver marcado
        if imunidade_agarrado:
            imunidades.append('Agarrado')
        if imunidade_amedrontado:
            imunidades.append('Amedrontado')
        if imunidade_atordoado:
            imunidades.append('Atordoado')
        if imunidade_caido:
            imunidades.append('Caído')
        if imunidade_cego:
            imunidades.append('Cego')
        if imunidade_enfeitiçado:
            imunidades.append('Enfeitiçado')
        if imunidade_envenenado:
            imunidades.append('Envenenado')
        if imunidade_impedido:
            imunidades.append('Impedido')
        if imunidade_incapacitado:
            imunidades.append('Incapacitado')
        if imunidade_inconsciente:
            imunidades.append('Inconsciente')
        if imunidade_invisivel:
            imunidades.append('Invisível')
        if imunidade_paralisado:
            imunidades.append('Paralisado')
        if imunidade_petrificado:
            imunidades.append('Petrificado')
        if imunidade_surdo:
            imunidades.append('Surdo')
        if imunidade_acido:
            imunidades.append('Ácido')
        if imunidade_concussao:
            imunidades.append('Concussão')
        if imunidade_cortante:
            imunidades.append('Cortante')
        if imunidade_eletrico:
            imunidades.append('Elétrico')
        if imunidade_energia:
            imunidades.append('Energia')
        if imunidade_fogo:
            imunidades.append('Fogo')
        if imunidade_frio:
            imunidades.append('Frio')
        if imunidade_necronico:
            imunidades.append('Necrótico')
        if imunidade_perfurante:
            imunidades.append('Perfurante')
        if imunidade_psiquico:
            imunidades.append('Psíquico')
        if imunidade_radiante:
            imunidades.append('Radiante')
        if imunidade_trovejante:
            imunidades.append('Trovejante')
        if imunidade_veneno:
            imunidades.append('Veneno')
        if imunidade_nmagicos:
            imunidades.append('Não-mágicos')
        if imunidade_magia:
            imunidades.append('Magia')


        nataques = request.form.get('nataques')
        nmagias = request.form.get('nmagias')
        cd = request.form.get('cd')
        pericias = request.form.get('pericias')
        
        acrobacia = request.form.get('acrobacia')
        adestrar_animais = request.form.get('adestrar-animais')
        arcanismo = request.form.get('arcanismo')
        atletismo = request.form.get('atletismo')
        atuacao = request.form.get('atuacao')
        enganacao = request.form.get('engancao')
        furtividade = request.form.get('furtividade')
        historia = request.form.get('historia')
        intimidacao = request.form.get('intimidacao')
        intuicao = request.form.get('intuicao')
        investigacao = request.form.get('investigacao')
        medicina = request.form.get('medicina')
        natureza = request.form.get('natureza')
        percepcao = request.form.get('percepcao')
        persuacao = request.form.get('persuacao')
        prestidigitacao = request.form.get('prestidigitacao')
        religiao = request.form.get('religiao')
        sobrevivencia = request.form.get('sobrevivencia')
        pericias_atuais = []

        # Adiciona à lista apenas se o campo não estiver vazio
        if acrobacia == 'on':
            pericias_atuais.append('Acrobacia')
        if adestrar_animais == 'on':
            pericias_atuais.append('Adestrar Animais')
        if arcanismo == 'on':
            pericias_atuais.append('Arcanismo')
        if atletismo == 'on':
            pericias_atuais.append('Atletismo')
        if atuacao == 'on':
            pericias_atuais.append('Atuação')
        if enganacao == 'on':
            pericias_atuais.append('Enganação')
        if furtividade == 'on':
            pericias_atuais.append('Furtividade')
        if historia == 'on':
            pericias_atuais.append('História')
        if intimidacao == 'on':
            pericias_atuais.append('Intimidação')
        if intuicao == 'on':
            pericias_atuais.append('Intuição')
        if investigacao == 'on':
            pericias_atuais.append('Investigação')
        if medicina == 'on':
            pericias_atuais.append('Medicina')
        if natureza == 'on':
            pericias_atuais.append('Natureza')
        if percepcao == 'on':
            pericias_atuais.append('Percepção')
        if persuacao == 'on':
            pericias_atuais.append('Persuasão')
        if prestidigitacao == 'on':
            pericias_atuais.append('Prestidigitação')
        if religiao == 'on':
            pericias_atuais.append('Religião')
        if sobrevivencia == 'on':
            pericias_atuais.append('Sobrevivência')

        #------ Habilidades
        habilidades = request.form.get('habilidades')
        nome_habilidades = request.form.getlist('nomehabilidade[]')
        desc_habilidades = request.form.getlist('deschabilidade[]')
        habilidades_atuais = []
        for nome, descricao in zip(nome_habilidades, desc_habilidades):
            habilidades_atuais.append({'nome': nome, 'descricao': descricao})
        #------ Ações
        aespeciais = request.form.get('aespeciais ')
        nome_acoes = request.form.getlist('nomeacao[]')
        desc_acoes = request.form.getlist('descacao[]')
        acoes_atuais = []
        for nome, descricao in zip(nome_acoes, desc_acoes):
            if nome and descricao:  
                acoes_atuais.append({'nome': nome, 'descricao': descricao})
        #------ Ataques
        tatackes = request.form.get('tatackes')
        nome_ataques = request.form.getlist('nomeataque[]')
        tipo_ataques = request.form.getlist('tipo[]')
        bonus_ataques = request.form.getlist('bonusataque[]')
        alcance_ataques = request.form.getlist('alcanceataque[]')
        dano_ataques = request.form.getlist('danoataque[]')
        dado_ataques = request.form.getlist('dadoataque[]')
        tipodano_ataques = request.form.getlist('tipodanoataque[]')
        extra_ataques = request.form.getlist('extraataque[]')
        danototal_ataques = request.form.getlist('danototalataque[]')

        ataques_atuais = []
        for nome, tipo, bonus, alcance, dano, dado, tipodano, extra, danototal in zip(
                nome_ataques, tipo_ataques, bonus_ataques, alcance_ataques, dano_ataques,
                dado_ataques, tipodano_ataques, extra_ataques, danototal_ataques):
            ataques_atuais.append({
                'nome': nome,
                'tipo': tipo,
                'bonus': bonus,
                'alcance': alcance,
                'dano': dano,
                'dado': dado,
                'tipodano': tipodano,
                'extra': extra,
                'danototal': danototal
            })


        reacao = request.form.get('reacao')

        nome_reacoes = request.form.getlist('nomereacao[]')
        desc_reacoes = request.form.getlist('descreacao[]')

        reacoes_atuais = []
        for nome, descricao in zip(nome_reacoes, desc_reacoes):
           reacoes_atuais.append({'nome': nome, 'descricao': descricao})

        #------ Ações Lendárias
        lendarias = request.form.get('lendarias')
        desclendaria = request.form.getlist('desclendaria')

        nome_acoes_lendarias = request.form.getlist('nomelendaria[]')
        desc_acoes_lendarias = request.form.getlist('descacaolendaria[]')
        acoes_lendarias_atuais = []
        for nome, descricao in zip(nome_acoes_lendarias, desc_acoes_lendarias):
           acoes_lendarias_atuais.append({'nome': nome, 'descricao': descricao})

        informacoes = request.form.get('informacoes')
        usos = request.form.get('dicasUso')

             # Preparar os dados para retorno
        npc_form = {
            "npc_nome": npc_nome,
            "template": template,
            "raca": raca,
            "tendencia": tendencia,
            "genero": genero,
            "ca": ca,
            "pv": pv,
            "dadosvida": dadosvida,
            "speed": speed,
            "voo": voo,
            "natacao": natacao,
            "darkvision": darkvision,
            "classe_base": classe_base,
            "nd": nd,
            
            "saves": saves,
            "forca": forca,
            "save_forca": save_forca,
            "destreza": destreza,
            "save_destreza": save_destreza,
            "constituição": constituicao,
            "save_constituicao": save_constituicao,
            "sabedoria": sabedoria,
            "save_sabedoria": save_sabedoria,
            "inteligência": inteligencia,
            "save_inteligencia": save_inteligencia,
            "carisma": carisma,
            "save_carisma": save_carisma,
            
            "classe": classe,
            "imunidade": imunidade,
            "imunidades": imunidades,
            "resistencia": resistencia,
            "resistencias": resistencias,
            "nataques": nataques,
            "nmagias": nmagias,
            "cd": cd,
            "pericias": pericias,
            "pericias_atuais": pericias_atuais,
            "habilidades": habilidades,
            "habilidades_atuais": habilidades_atuais,
            "acoes": aespeciais,
            "acoes_atuais": acoes_atuais,
            "ataques": tatackes,
            "ataques_atuais": ataques_atuais,
            "reacão": reacao,
            "reacoes_atuais": reacoes_atuais,
            "lendarias": lendarias,
            "desclendaria": desclendaria,
            "acoes_lendarias_atuais": acoes_lendarias_atuais,
            "informacoes": informacoes,
            "usos": usos

        }
        #print ('NPC FORM: ', npc_form)
        
        NPCController.criar_npc(npc_form)
        
        
        # Retornar os dados como JSON
        return redirect('/')

      