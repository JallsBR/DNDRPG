from flask import Blueprint, render_template, request, redirect, flash
from controller.user_controller import UserController
from model.user_model import User

from extensions import login_manager
from flask_login import login_user, logout_user
import locale
from datetime import datetime

@login_manager.user_loader
def get_user(id):
    return User.query.get(id)

blueprint_login = Blueprint("login", __name__, template_folder="templates")
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
agora = datetime.now().strftime('%d/%m/%Y')

@blueprint_login.route('/', methods=['GET', 'POST'])
def login():
    error = False
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        user = User.query.filter_by(login=login).first()

        if not user or not user.verify_senha(senha):
            print("Credenciais não encontradas")
            error = True
            return render_template('login.html', error=error)

        login_user(user)
        return redirect('/')

    return render_template('login.html', error=error)


@blueprint_login.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        login = request.form.get('login')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')
        tipo = "não informado"


        if not (nome and sobrenome and email and telefone and login and senha and csenha):
            flash("Todos os campos devem ser preenchidos!")
            return redirect('/login/register')

        if senha != csenha:
            flash("As senhas não coincidem!")
            return redirect('/login/register')

        success, message = UserController.create_user(nome, sobrenome, email, telefone, login, senha, tipo)
        if success:
            return redirect('/login')
        else:
            flash(f"Erro ao criar usuário: {message}")
            return redirect('/login/register')

    return render_template('register.html')

@blueprint_login.route('logout')
def logout():
    logout_user()
    return redirect ('/')