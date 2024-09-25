from flask import Blueprint, render_template, request, redirect
from model.personagens_model import Personagem
from flask_login import logout_user, current_user


blueprint_pj = Blueprint("pj", __name__, template_folder="templates")

@blueprint_pj.route('/', methods=['GET', 'POST'])
def index_pj():

    if request.method == 'GET':       
        npcs = Personagem.npcs_id(id_user=current_user.id)        
        return render_template('pj.html', npcs=npcs)
    
    if request.method == 'POST':        
        return redirect('/')

      