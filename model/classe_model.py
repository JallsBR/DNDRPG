from database.database import db


class Classe(db.Model):
    __tablename__ = "classe"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    dado_de_vida = db.Column(db.String(10), nullable=False)
    save1 = db.Column(db.String(15), nullable=False)
    save2 = db.Column(db.String(15), nullable=False)
    pericias = db.Column(db.Text, nullable=False)
    prof_arma = db.Column(db.String(200), nullable=False)
    prof_armadura = db.Column(db.Text, nullable=False)
    equipamento = db.Column(db.Text, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    multiclasse = db.Column(db.Text, nullable=False)   


   


    def __init__(self, nome, dado_de_vida, save1, save2, pericias, prof_arma, prof_armadura, equipamento,descricao, multiclasse):
        self.nome = nome
        self.dado_de_vida = dado_de_vida
        self.save1 = save1
        self.save2 = save2
        self.pericias = pericias
        self.prof_arma = prof_arma
        self.prof_armadura = prof_armadura
        self.equipamento = equipamento
        self.descricao = descricao
        self.multiclasse = multiclasse
        
    def __repr__(self):
        return  f"Classe({self.nome}, {self.dado_de_vida}, {self.save1}, {self.save2})"