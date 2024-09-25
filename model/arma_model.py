from database.database import db


class Arma(db.Model):
    __tablename__ = "arma"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique=True)
    nome_original = db.Column(db.String(40), nullable=False, unique=True)
    categoria = db.Column(db.String(40), nullable=False)
    tipo_dano = db.Column(db.String(40), nullable=False)
    dado_dano = db.Column(db.String(40), nullable=False)
    propriedades = db.Column(db.String(40), nullable=False)
    maestria = db.Column(db.String(40), nullable=False)
    peso = db.Column(db.String(40), nullable=False)
    preco = db.Column(db.String(40), nullable=False)
   


    def __init__(self, nome, nome_original, categoria, tipo_dano, dado_dano,propriedades, maestria, peso, preco):
        self.nome = nome
        self.nome_original = nome_original
        self.categoria = categoria
        self.tipo_dano = tipo_dano
        self.dado_dano = dado_dano
        self.propriedades = propriedades
        self.maestria = maestria
        self.peso = peso
        self.preco = preco

    def __repr__(self):
        return f"Arma({self.nome}, {self.nome_original}, {self.categoria}, {self.tipo_dano}, {self.dado_dano}, {self.propriedades}, {self.maestria}, {self.peso}, {self.preco})"
    
    @classmethod
    def get_armas(cls):
        return cls.query.all()