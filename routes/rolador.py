from flask import Blueprint, render_template, request, redirect


blueprint_rolador = Blueprint("rolador", __name__, template_folder="templates")

@blueprint_rolador.route('/', methods=['GET', 'POST'])
def index_rolador():
    if request.method == 'GET':
        return render_template('rolador.html')
    
    if request.method == 'POST':        
        return redirect('/')

      