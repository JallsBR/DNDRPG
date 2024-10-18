from flask import Blueprint, render_template, request, redirect,  jsonify, flash
import json
from model.magias_model import Magias
from model.cenario_model import Cenario

from flask_login import logout_user, current_user
from database.database import db






blueprint_magia = Blueprint("magia", __name__, template_folder="templates")

@blueprint_magia.route('/', methods=['GET', 'POST'])
def index_magia():
    if request.method == 'GET':
        # Captura os parâmetros de filtro da URL
        classe = request.args.get('classe', 'Todas')
        escola = request.args.get('escola', 'Todas')
        organizar = request.args.get('organizar', 'Nome')

        # Filtra as magias com base nos parâmetros fornecidos
        magias = Magias.filtrar_magias(classe=classe, escola=escola, organizar=organizar)
        
        return render_template('magias.html', magias=magias)
    if request.method == 'POST':        
        return redirect('/')
    


@blueprint_magia.route('/criarmagia', methods=['GET', 'POST'])
def criarmagia():
    if request.method == 'GET':
        magias = Magias.todas_magias()
        return render_template('criarmagia.html', magias=magias)

    if request.method == 'POST':
        # Coletando os dados do formulário
        nome = request.form.get('nome')
        spellname = request.form.get('spellname')
        
        nivel = request.form.get('nivel')
        if nivel == '0':
            nivel = 'Truque'
            
        escola = request.form.get('escola')
        distancia = request.form.get('distancia')
        casting = request.form.get('casting')
        duracao = request.form.get('duracao')
        componentes = request.form.get('componentes')
        componentes = componentes.split(',')
        texto = request.form.get('texto')
        spelldescription = request.form.get('spelldescription')
        upgrade = request.form.get('upgrade')
        livro = request.form.get('livro')

        classes = []
        for classe in ['Mago', 'Clérigo', 'Feiticeiro', 'Bardo', 'Druida', 'Bruxo', 'Paladino', 'Patrulheiro']:
            if request.form.get(classe):
                classes.append(classe)

        magia_data = {
            'nome': nome,
            'spellname': spellname,
            'spelldescription': spelldescription,
            'nivel': nivel,
            'escola': escola,
            'classes': classes, 
            'casting': casting,
            'distancia': distancia,
            'componentes': componentes,
            'duracao': duracao,
            'texto': texto,
            'upgrade': upgrade,
            'livro': livro,
        }
                  
        print("Magia", magia_data)
              
        if magia_data:
                magia = Magias.criar_magia(magia_data)

                if isinstance(magia, str):
                    flash(f"Erro ao criar magia: {magia}", "danger")
                else:
                    flash(f"Erro ao criar magia: {magia}", "danger")

        return redirect(request.url)
    
    
    
    
    
@blueprint_magia.route('/criarmagiajson', methods=['GET', 'POST'])
def criarmagiajson():
    if request.method == 'GET':
        return render_template('criarmagiajson.html')

    if request.method == 'POST':
        texto = request.form.get('texto')
        try:
            # Converte a string JSON em um dicionário Python
            magia_data = json.loads(texto)

            # Verifica se o dicionário está no formato esperado
            if isinstance(magia_data, dict):
                # Cria a magia usando os dados fornecidos
                magia = Magias.criar_magia(magia_data=magia_data)

                # Verifica se ocorreu algum erro
                if isinstance(magia, str):
                    flash(f"Erro ao criar magia: {magia_data.get('nome', 'Nome não encontrado')}", "danger")
                else:
                    flash(f"Magia '{magia_data.get('nome', 'Nome não encontrado')}' criada com sucesso!", "success")
            else:
                flash("Erro: O JSON enviado não está no formato correto.", "danger")
        
        except json.JSONDecodeError as e:
            flash(f"Erro ao interpretar o JSON: {str(e)}", "danger")

        return redirect(request.url)
    
    
@blueprint_magia.route('/deletar/<int:magia_id>', methods=['POST'])
def delete_magia(magia_id):
    """Rota para deletar uma magia pelo ID"""
    sucesso = Magias.deletar_magia(magia_id)  
    if sucesso == True:
        flash(f"Magia deletada com sucesso!", "success")  
    else:
        flash(f"Erro ao deletar magia: {sucesso}", "danger") 

    return redirect(request.url) 

@blueprint_magia.route('/editar/<id>', methods=['GET', 'POST'])
def editar_magia(id):
    if request.method == 'GET':
        magia = Magias.magia_id(id)
        if magia:
            return render_template('editarmagia.html', magia=magia)
        else:
            flash("Magia não encontrada", "danger")            
            return redirect(request.url)
        
    if request.method == 'POST':
        
        nome = request.form.get('nome')
        spellname = request.form.get('spellname')
        
        nivel = request.form.get('nivel')
        if nivel == '0':
            nivel = 'Truque'
            
        escola = request.form.get('escola')
        distancia = request.form.get('distancia')
        classes = request.form.get('classes')
        classes = classes.split(',')
        casting = request.form.get('casting')
        duracao = request.form.get('duracao')
        componentes = request.form.get('componentes')
        componentes = componentes.split(',')
        texto = request.form.get('texto')
        spelldescription = request.form.get('spelldescription')
        upgrade = request.form.get('upgrade')
        livro = request.form.get('livro')
        
        magia_data = {
            'nome': nome,
            'spellname': spellname,
            'spelldescription': spelldescription,
            'nivel': nivel,
            'escola': escola,
            'classes': classes, 
            'casting': casting,
            'distancia': distancia,
            'componentes': componentes,
            'duracao': duracao,
            'texto': texto,
            'upgrade': upgrade,
            'livro': livro,
        }
        
        if magia_data:
                magia = Magias.alterar_magia(magia_id=id, updated_data=magia_data)

                if isinstance(magia, str):
                    flash(f"Erro ao atualizar magia: {magia.magia['nome']}", "danger") 
                else:
                    flash(f"Magia {magia.magia['nome']} atualizada com sucesso!", "success") 
                
        return redirect('/magia')
