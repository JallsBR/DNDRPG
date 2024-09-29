from database.database import db


class Armadura(db.Model):
    __tablename__ = "armadura"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique=True)
    nome_original = db.Column(db.String(40), nullable=False, unique=True)
    categoria = db.Column(db.String(40), nullable=False)
    classe_armadura = db.Column(db.String(40), nullable=False)
    forca = db.Column(db.Integer)
    furtividade = db.Column(db.Boolean, nullable=False)
    peso = db.Column(db.String(40), nullable=False)
    preco = db.Column(db.String(40), nullable=False)
   


    def __init__(self, nome, nome_original, categoria, classe_armadura, forca, furtividade, peso, preco):
        self.nome = nome
        self.nome_original = nome_original
        self.categoria = categoria
        self.classe_armadura = classe_armadura
        self.forca = forca
        self.furtividade = furtividade
        self.peso = peso
        self.preco = preco
        
    def __repr__(self):
        return f"Armadura({self.nome}, {self.nome_original}, {self.categoria}, {self.classe_armadura}, {self.forca}, {self.furtividade}, {self.peso}, {self.preco})"
    
    
    @classmethod
    def get_armadura(cls):
        return cls.query.all()
    
    @classmethod
    def get_classe_armadura_por_nome(cls, nome):
        armadura = cls.query.filter_by(nome=nome).first()
        if armadura:
            return armadura.classe_armadura
        return None