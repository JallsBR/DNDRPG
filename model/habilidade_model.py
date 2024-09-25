from database.database import db


class Habilidade(db.Model):
    __tablename__ = "habilidade"

    id = db.Column(db.Integer, primary_key=True)
    habilidade = db.Column(db.String(100), nullable=False, unique=True)
    descricao = db.Column(db.Text, nullable=False)   
    efeito_nd = db.Column(db.String(150), nullable=False)

   


    def __init__(self, habilidade, descricao, efeito_nd):
        self.habilidade = habilidade
        self.descricao = descricao
        self.efeito_nd = efeito_nd
        
    def __repr__(self):
        return f"<Habilidade {self.habilidade}>"