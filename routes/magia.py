from flask import Blueprint, render_template, request, redirect,  jsonify, flash
import json
from model.magias_model import Magias
from controller.mestre_controller import MestreController

from flask_login import logout_user, current_user
from database.database import db

CLASSES_NUMERO = {
    'Mago': 1,
    'Clérigo': 2,
    'Feiticeiro': 3,
    'Bardo': 4,
    'Druida': 5,
    'Bruxo': 6,
    'Paladino': 7,
    'Patrulheiro': 8
}

NUMERO_CLASSES = {v: k for k, v in CLASSES_NUMERO.items()}

ESCOLAS_NUMERO = {
    'Abjuração': 1,
    'Advinhação': 2,
    'Conjuração': 3,
    'Encantamento': 4,
    'Evocação': 5,
    'Ilusão': 6,
    'Necromancia': 7,
    'Transmutação': 8
}

NUMERO_ESCOLAS = {v: k for k, v in ESCOLAS_NUMERO.items()}


blueprint_magia = Blueprint("magia", __name__, template_folder="templates")

@blueprint_magia.route('/', methods=['GET', 'POST'])
def index_magia():
    if request.method == 'GET':
        classe = request.args.get('classe', 'Todas')
        escola = request.args.get('escola', 'Todas')
        organizar = request.args.get('organizar', 'Nome')
        nivel = request.args.get('magianivel', 'Todos')

        print("filtro nivel: ", nivel)
        
        magias = MestreController.ajuste_exibir_magias(classe=classe, escola=escola, organizar=organizar, pt=True, nivel=nivel)        

        for magia in magias:
            magia.magia['classes'] = [NUMERO_CLASSES.get(numero, 'Desconhecida') for numero in magia.magia['classes']]

            if magia.magia['escola'] is not None:
                magia.magia['escola'] = NUMERO_ESCOLAS.get(int(magia.magia['escola']))

            else:
                magia.magia['escola'] = 'Desconhecida'  
        
        
        return render_template('magias.html', magias=magias, escolas_numero=ESCOLAS_NUMERO, classe=classe, escola=escola, organizar=organizar, magianivel=nivel)
    if request.method == 'POST':        
        return redirect('/')
    


@blueprint_magia.route('/criarmagia', methods=['GET', 'POST'])
def criarmagia():
    if request.method == 'GET':
        magias = Magias.todas_magias()
        return render_template('criarmagia.html', magias=magias, escolas_numero=ESCOLAS_NUMERO)

    if request.method == 'POST':

        nome = request.form.get('nome')
        spellname = request.form.get('spellname')
        
        nivel = request.form.get('nivel')
        if nivel == 'Truque':
            nivel = '0'
        

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
        for classe, numero in CLASSES_NUMERO.items():
            if request.form.get(classe):
                classes.append(numero)

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
                flash(f"Magia criada com sucesso!", "success")

        return redirect(request.url)

    
    
    
    
    
@blueprint_magia.route('/criarmagiajson', methods=['GET', 'POST'])
def criarmagiajson():
    if request.method == 'GET':
        return render_template('criarmagiajson.html')

    if request.method == 'POST':
        texto = request.form.get('texto')
        try:

            magia_data = json.loads(texto)


            if isinstance(magia_data, dict):

                magia = Magias.criar_magia(magia_data=magia_data)


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
            classes_selecionadas = [NUMERO_CLASSES.get(numero, 'Desconhecida') for numero in magia.magia['classes']]
            magia_escola_numero = int(magia.magia['escola'])            


            return render_template('editarmagia.html', 
                                   magia=magia, 
                                   classes_selecionadas=classes_selecionadas, 
                                   classes_numero=CLASSES_NUMERO, 
                                   escolas_numero=ESCOLAS_NUMERO, 
                                   magia_escola_numero=magia_escola_numero)
        else:
            flash("Magia não encontrada", "danger")
            return redirect(request.url)
        
    if request.method == 'POST':
        
        escola = request.form.get('escola')
        print(f"Valor da escola recebido: {escola}")  

        escola_numero = ESCOLAS_NUMERO.get(escola)
        print(f"Número da escola: {escola_numero}") 
            
        nome = request.form.get('nome')
        spellname = request.form.get('spellname')
        
        nivel = request.form.get('nivel')
        if nivel == 'Truque':
            nivel = '0'           

        
        distancia = request.form.get('distancia')
       
        # Convertendo classes (de nomes para números)
        classes = []
        for classe, numero in CLASSES_NUMERO.items():
            if request.form.get(classe):
                classes.append(numero)
        
        
        
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
