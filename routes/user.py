from flask import Blueprint, render_template, request, redirect, flash, url_for
from controller.user_controller import UserController
from extensions import login_manager
from flask_login import login_user, logout_user

blueprint_user = Blueprint("user", __name__, template_folder="templates")

@blueprint_user.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('user_create.html')
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        login = request.form.get('login')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')
        

        if nome and sobrenome and email and telefone and login and senha and csenha==senha:

            success, message = UserController.create_user(nome, sobrenome, email, telefone, login, senha)
            if success:
                print("Usuário criado com sucesso, redirecionando para /login")
                return redirect('/login')
                flash(message)
            else:
                print(f"Erro ao criar usuário: {message}")
                flash(message)
                return redirect('/login')
        else:
            print("Alguns campos estão faltando.")
            flash("Todos os campos devem ser preenchidos!")
            return redirect('/login')      



@blueprint_user.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user, error = UserController.get_all_users(id)
    if error:
        flash(error)
        return redirect('/psi/recovery')

    if request.method == 'GET':
        return render_template('user_update.html', user=user)
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        login = request.form.get('login')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')

        if csenha == senha: 
            success, message = UserController.update_user(id, nome, sobrenome, email=email, telefone=telefone, login=login, senha=senha)
            if success:
                return redirect('/psi/recovery')
            else:
                flash(message)
                return render_template('user_update.html', user=user)
        else:
            flash("As senhas não coincidem.")
            return render_template('user_update.html', user=user)
