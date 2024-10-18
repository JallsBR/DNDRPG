from flask import Blueprint, render_template, request, redirect,  jsonify
from model.campanha_model import Campanha
from model.cenario_model import Cenario
from model.personagens_model import Personagem
from model.cenariocampanha_model import CenarioCampanha
from model.encontro_model import Encontro
from model.encontrocampanha_model import EncontroCampanha
from model.organizacoes_model import Organizacoes
from model.organizacoescampanha_model import OrganizacoesCampanha
from model.npcscampanha_model import NPCsCampanha
from flask_login import logout_user, current_user
from database.database import db






blueprint_mestre = Blueprint("mestre", __name__, template_folder="templates")

@blueprint_mestre.route('/', methods=['GET', 'POST'])
def index_mestre():
    if request.method == 'GET':

        return render_template('mestre.html')
    
    if request.method == 'POST':        
        return redirect('/')
    
    

# CENARIOS -----------------------------------------------------------------

@blueprint_mestre.route('/cenario', methods=['GET', 'POST'])
def index_cenario():
    if request.method == 'GET':
        cenarios = Cenario.cenario_userid(current_user.id)
        personagens = Personagem.npcs_id(id_user=current_user.id)
        return render_template('cenarios.html', cenarios=cenarios, personagens=personagens)
    
    if request.method == 'POST':

        # Coletando dados do formulário
        nome = request.form.get('nome')
        descricaocurta = request.form.get('descricaocurta')
        categoria = request.form.get('categoria')
        if not categoria:
            categoria = 'Geral'
        descricao = request.form.get('descricao')
        historia = request.form.get('historia')
        
        # Coletando regras
        nome_regras = request.form.getlist('nome_regra[]')
        descricao_regras = request.form.getlist('descricao_regra[]')
        observacao_regras = request.form.getlist('observacao_regra[]')
        
        # Coletando informações
        pericias = request.form.getlist('pericia[]')
        cds = request.form.getlist('cd[]')
        informacoes = request.form.getlist('informacao[]')
        
        # Coletando NPCs
        nomes_npcs = request.form.getlist('nome_npc[]')
        ids_npcs = 1
        observacoes_npcs = request.form.getlist('observacao_npc[]')
        
        # Coletando organizações
        nomes_organizacoes = request.form.getlist('nome_organizacao[]')
        ids_organizacoes = 1
        observacoes_organizacoes = request.form.getlist('observacao_organizacao[]')
        
        # Coletando cenários agregados
        nomes_cenarios = request.form.getlist('nome_cenario_agregado[]')
        ids_cenarios = 1
        observacoes_cenarios = request.form.getlist('observacao_cenario_agregado[]')

        # Coletando outras informações
        titulos_outros = request.form.getlist('titulo[]')
        textos_outros = request.form.getlist('texto[]')
        
        cenarios_data = {
        "nome": nome,
        "descricaocurta": descricaocurta,
        "descricao": descricao,
        "historia": historia,
        "categoria": categoria,
        "regras": [
            {
                "nome_regra": nome_regras[i],
                "descricao_regra": descricao_regras[i],
                "observacao": observacao_regras[i]
            } for i in range(len(nome_regras))
        ],
        "info_cenario": [
            {
                "pericia": pericias[i],
                "cd": cds[i],
                "informacao": informacoes[i]
            } for i in range(len(pericias))
        ],
        "npcs": [
            {
                "nome": nomes_npcs[i],
                "id": ids_npcs[i],
                "observacao": observacoes_npcs[i]
            } for i in range(len(nomes_npcs))
        ],
        "organizacoes": [
            {
                "nome": nomes_organizacoes[i],
                "id": ids_organizacoes[i],
                "observacao": observacoes_organizacoes[i]
            } for i in range(len(nomes_organizacoes))
        ],
        "outras": [
            {
                "titulo": titulos_outros[i],
                "texto": textos_outros[i]
            } for i in range(len(titulos_outros))
        ],
        "cenarios_agregados": [
            {
                "nome": nomes_cenarios[i],
                "id": ids_cenarios[i],
                "observacao": observacoes_cenarios[i]
            } for i in range(len(nomes_cenarios))
            ]
        }        
        
        
        cenario_data = cenarios_data
        print("CENARIO: ",cenario_data)
        tipo = categoria
        
        if cenario_data and tipo:
            novo_cenario = Cenario(id_user=current_user.id, cenario=cenario_data, tipo=tipo)
            db.session.add(novo_cenario)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Novo cenário criado com sucesso!'}), 201
        else:
            return jsonify({'status': 'error', 'message': 'Dados insuficientes para criar o cenário.'}), 400


@blueprint_mestre.route('/editar_cenario/<id>', methods=['GET', 'POST'])
def editar_cenario(id):
    cenario = Cenario.query.get(id)    
    if request.method == 'GET':
        if cenario:
            return render_template('edit_cenario.html', cenario=cenario, enumerate=enumerate)
        else:
            return jsonify({"error": "Cenário não encontrado ou não autorizado."}), 404

    if request.method == 'POST':
        # Coletando dados do formulário
        nome = request.form.get('nome')
        descricaocurta = request.form.get('descricaocurta')
        categoria = request.form.get('categoria')
        if not categoria:
            categoria = 'Geral'
        descricao = request.form.get('descricao')
        historia = request.form.get('historia')

        # Coletando regras
        nome_regras = request.form.getlist('nome_regra[]')
        descricao_regras = request.form.getlist('descricao_regra[]')
        observacao_regras = request.form.getlist('observacao_regra[]')

        # Coletando informações
        pericias = request.form.getlist('pericia[]')
        cds = request.form.getlist('cd[]')
        informacoes = request.form.getlist('informacao[]')

        # Coletando NPCs
        nomes_npcs = request.form.getlist('nome_npc[]')
        ids_npcs = 1
        observacoes_npcs = request.form.getlist('observacao_npc[]')

        # Coletando organizações
        nomes_organizacoes = request.form.getlist('nome_organizacao[]')
        ids_organizacoes = 1
        observacoes_organizacoes = request.form.getlist('observacao_organizacao[]')

        # Coletando cenários agregados
        nomes_cenarios = request.form.getlist('nome_cenario_agregado[]')
        ids_cenarios = 1
        observacoes_cenarios = request.form.getlist('observacao_cenario_agregado[]')

        # Coletando outras informações
        titulos_outros = request.form.getlist('titulo[]')
        textos_outros = request.form.getlist('texto[]')

        # Construindo o dicionário com os dados
        cenario_data = {
            "nome": nome,
            "descricaocurta": descricaocurta,
            "descricao": descricao,
            "historia": historia,
            "categoria": categoria,
            "regras": [
                {
                    "nome_regra": nome_regras[i],
                    "descricao_regra": descricao_regras[i],
                    "observacao": observacao_regras[i]
                } for i in range(len(nome_regras))
            ],
            "info_cenario": [
                {
                    "pericia": pericias[i],
                    "cd": cds[i],
                    "informacao": informacoes[i]
                } for i in range(len(pericias))
            ],
            "npcs": [
                {
                    "nome": nomes_npcs[i],
                    "id": ids_npcs[i],
                    "observacao": observacoes_npcs[i]
                } for i in range(len(nomes_npcs))
            ],
            "organizacoes": [
                {
                    "nome": nomes_organizacoes[i],
                    "id": ids_organizacoes[i],
                    "observacao": observacoes_organizacoes[i]
                } for i in range(len(nomes_organizacoes))
            ],
            "outras": [
                {
                    "titulo": titulos_outros[i],
                    "texto": textos_outros[i]
                } for i in range(len(titulos_outros))
            ],
            "cenarios_agregados": [
                {
                    "nome": nomes_cenarios[i],
                    "id": ids_cenarios[i],
                    "observacao": observacoes_cenarios[i]
                } for i in range(len(nomes_cenarios))
            ]
        }

        if cenario and cenario.id_user == current_user.id:
            # Aqui você atualiza o cenário com os dados novos
            Cenario.update(id, cenario=cenario_data)
            return jsonify({"message": "Cenário atualizado com sucesso."}), 200
        else:
            return jsonify({"error": "Cenário não encontrado ou não autorizado."}), 404


@blueprint_mestre.route('/delete_cenario/<id>', methods=['DELETE'])
def deletar_cenario(id):
    cenario = Cenario.query.get(id)
    if cenario and cenario.id_user == current_user.id:
        Cenario.delete(id)
        return jsonify({"message": "Cenário deletado com sucesso."}), 200
    else:
        return jsonify({"error": "Cenário não encontrado ou não autorizado."}), 404, 
    
    
# Campanha -----------------------------------------------------------------
    
@blueprint_mestre.route('/campanha', methods=['GET', 'POST'])
def index_campanha():
    if request.method == 'GET':
        return render_template('campanha.html')
    
    if request.method == 'POST':        
        return redirect('/')
    
    
  

@blueprint_mestre.route('/encontro', methods=['GET', 'POST'])
def index_encontro():
    if request.method == 'GET':

        return render_template('encontros.html')
    
    if request.method == 'POST':        
        return redirect('/')
      

@blueprint_mestre.route('/organizacao', methods=['GET', 'POST'])
def index_organizacao():
    if request.method == 'GET':

        return render_template('construcao.html')
    
    if request.method == 'POST':        
        return redirect('/')