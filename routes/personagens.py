from flask import Blueprint, render_template, request, redirect
from model.personagens_model import Personagem
from flask_login import logout_user, current_user


blueprint_pj = Blueprint("pj", __name__, template_folder="templates")

@blueprint_pj.route('/', methods=['GET', 'POST'])
def index_pj():

    if request.method == 'GET':       
      
        return render_template('pj.html', )
    
    if request.method == 'POST':        
        return redirect('/')

      