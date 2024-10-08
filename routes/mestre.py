from flask import Blueprint, render_template, request, redirect,  jsonify
from model.campanha_model import Campanha
from model.cenario_model import Cenario
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
        return render_template('cenarios.html', cenarios=cenarios)
    
    if request.method == 'POST':
        cenario_data = request.json.get('cenario')
        tipo = request.json.get('tipo')

        if cenario_data and tipo:
            novo_cenario = Cenario(id_user=current_user.id, cenario=cenario_data, tipo=tipo)
            db.session.add(novo_cenario)
            db.session.commit()
            return jsonify({"message": "Cenário criado com sucesso."}), 201
        else:
            return jsonify({"error": "Dados insuficientes para criar o cenário."}), 400


@blueprint_mestre.route('/edit_cenario/<id>', methods=['GET', 'POST'])
def editar_cenario(id):
    cenario = Cenario.query.get(id)    
    if request.method == 'GET':
        if cenario and cenario.id_user == current_user.id:
            return render_template('edit_cenario.html', cenario=cenario)
        else:
            return jsonify({"error": "Cenário não encontrado ou não autorizado."}), 404

    if request.method == 'POST':
        cenario_data = request.json.get('cenario')
        tipo = request.json.get('tipo')

        if cenario and cenario.id_user == current_user.id:
            Cenario.update(id, cenario=cenario_data, tipo=tipo)
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
        return jsonify({"error": "Cenário não encontrado ou não autorizado."}), 404
    
    
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