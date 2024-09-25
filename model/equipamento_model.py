from database.database import db


class Equipamento(db.Model):
    __tablename__ = "equipamento"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False, unique=True)
    nome_original = db.Column(db.String(120), nullable=False, unique=True)
    descrição = db.Column(db.Text, nullable=False)   
    peso = db.Column(db.String(40))
    preco = db.Column(db.String(40))
   


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
        return f"Equipamento({self.nome}, {self.nome_original}, {self.categoria}, {self.tipo_dano}, {self.dado_dano}, {self.propriedades}, {self.maestria}, {self.peso}, {self.preco})"

    @classmethod
    def get_equipamentos(cls):
        return cls.query.order_by(cls.nome_original).all()