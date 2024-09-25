from database.database import db


class AcoesEspeciais(db.Model):
    __tablename__ = "acoesespeciais"

    id = db.Column(db.Integer, primary_key=True)
    acao = db.Column(db.String(100), nullable=False, unique=True)
    descricao = db.Column(db.Text, nullable=False)   
    efeito_nd = db.Column(db.String(150), nullable=False)

   


    def __init__(self, acao, descricao, efeito_nd):
        self.acao = acao
        self.descricao = descricao
        self.efeito_nd = efeito_nd
        
    def __repr__(self):
        return f"<Acao {self.acao}>"