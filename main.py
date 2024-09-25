from flask import Flask, render_template, redirect
from flask_login import logout_user, current_user
from database.database import db
from flask_migrate import Migrate
from extensions import login_manager

from routes.login import blueprint_login
from routes.user import blueprint_user
from routes.npc import blueprint_npc
from routes.personagens import blueprint_pj
from routes.equipamentos import blueprint_equip
from routes.campanhas import blueprint_campanha
from routes.rolador import blueprint_rolador
from routes.encontros import blueprint_encontros


app = Flask(__name__)
login_manager.init_app(app)

conexao="sqlite:///rpgtools.sqlite"

app.config['SECRET_KEY'] = '3751920526716512651$%!$!%!ivivILVVHKnnwvqw'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(blueprint_login, url_prefix='/login')
app.register_blueprint(blueprint_user, url_prefix='/user')
app.register_blueprint(blueprint_npc, url_prefix='/npc')
app.register_blueprint(blueprint_pj, url_prefix='/pj')
app.register_blueprint(blueprint_equip, url_prefix='/equip')
app.register_blueprint(blueprint_campanha, url_prefix='/campanha')
app.register_blueprint(blueprint_rolador, url_prefix='/rolador')
app.register_blueprint(blueprint_encontros, url_prefix='/encontros')

migrate = Migrate(app, db)


@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect('/login')       
    return render_template('index.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect ('/')
app.run(host='0.0.0.0', port=81, debug=True)