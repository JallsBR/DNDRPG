from flask import Blueprint, render_template, request, redirect


blueprint_campanha = Blueprint("campanha", __name__, template_folder="templates")

@blueprint_campanha.route('/', methods=['GET', 'POST'])
def index_campanha():
    if request.method == 'GET':
        return render_template('campanha.html')
    
    if request.method == 'POST':        
        return redirect('/')

      