from flask import Blueprint, render_template, request, redirect,  jsonify, flash
from model.magias_model import Magias
from model.cenario_model import Cenario

from flask_login import logout_user, current_user
from database.database import db






blueprint_magia = Blueprint("magia", __name__, template_folder="templates")

@blueprint_magia.route('/', methods=['GET', 'POST'])
def index_magia():
    if request.method == 'GET':

        return render_template('mestre.html')
    
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
        texto = request.form.get('texto')
        spelldescription = request.form.get('spelldescription')
        upgrade = request.form.get('upgrade')
        livro = request.form.get('livro')

        classes = []
        for classe in ['Mago', 'Clérigo', 'Feiticeiro', 'Bardo', 'Druida', 'Bruxo', 'Paladino', 'Ranger']:
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
                    flash(f"Magia '{nome}' criada com sucesso!", "success")

        return redirect(request.url)
    
    
    
    
    
@blueprint_magia.route('/criarmagiajson', methods=['GET', 'POST'])
def criarmagiajson():
    if request.method == 'GET':
        return render_template('criarmagiajson.html')

    if request.method == 'POST':
        texto = request.form.get('texto')
      
        print("Magia", texto)
              
        if texto:
                magia = Magias.criar_magia(texto)

                if isinstance(magia, str):
                    flash(f"Erro ao criar magia: {texto['nome']}", "danger")
                else:
                    flash(f"Magia '{texto['nome']}' criada com sucesso!", "success")

        return redirect(request.url)