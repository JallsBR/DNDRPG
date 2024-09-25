from database.database import db


class Nome(db.Model):
    __tablename__ = "nome"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique=True)
    raca = db.Column(db.String(15), nullable=False)
    sexo= db.Column (db.String(10), nullable=False)

    def __init__(self, nome, raca, sexo):
        self.nome = nome
        self.raca = raca
        self.sexo = sexo