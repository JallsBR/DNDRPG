from database.database import db


class Reacoes(db.Model):
    __tablename__ = "reacoes"

    id = db.Column(db.Integer, primary_key=True)
    reacao = db.Column(db.String(100), nullable=False, unique=True)
    descricao = db.Column(db.Text, nullable=False)   
    efeito_nd = db.Column(db.String(150), nullable=False)

   


    def __init__(self, reacao , descricao, efeito_nd):
        self.reacao = reacao
        self.descricao = descricao
        self.efeito_nd = efeito_nd
        
    def __repr__(self):
        return f"<Reacao {self.reacao}>"