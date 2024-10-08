from flask import Blueprint, render_template, request, redirect
from model.arma_model import Arma
from model.armadura_model import Armadura
from model.equipamento_model import Equipamento


blueprint_equip = Blueprint("equip", __name__, template_folder="templates")

@blueprint_equip.route('/', methods=['GET', 'POST'])
def index_equip():
    if request.method == 'GET':
        armas = Arma.get_armas()
        armaduras = Armadura.get_armadura()
        equip=Equipamento.get_equipamentos()
        
        return render_template('itens.html', armas=armas, armaduras=armaduras, equip=equip)
    
    if request.method == 'POST':        
        return redirect('/')



@blueprint_equip.route('/<tipo>', methods=['GET', 'POST'])
def index2_equip(tipo):  # Adiciona o tipo como parâmetro da função
    if request.method == 'GET':
        armas = Arma.get_armas()
        armaduras = Armadura.get_armadura()
        equip = Equipamento.get_equipamentos()
        
        if tipo == 'arma':
            return render_template('arma.html', armas=armas)
        elif tipo == 'armadura':
            return render_template('armadura.html', armaduras=armaduras)  
        elif tipo == 'equip':
            return render_template('equipamento.html', equip=equip)
        else:
            return render_template('itens.html', armas=armas, armaduras=armaduras, equip=equip)
    
    if request.method == 'POST':

        return redirect('/')

