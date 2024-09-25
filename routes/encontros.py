from flask import Blueprint, render_template, request, redirect


blueprint_encontros = Blueprint("encontros", __name__, template_folder="templates")

@blueprint_encontros.route('/', methods=['GET', 'POST'])
def index_encontros():
    if request.method == 'GET':
        return render_template('encontros.html')
    
    if request.method == 'POST':        
        return redirect('/')

      