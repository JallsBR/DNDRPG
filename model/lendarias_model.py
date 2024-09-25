from database.database import db


class Lendarias(db.Model):
    __tablename__ = "lendarias"

    id = db.Column(db.Integer, primary_key=True)
    acaolendaria = db.Column(db.String(100), nullable=False, unique=True)
    custo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, nullable=False)   
    efeito_nd = db.Column(db.String(150), nullable=False)

   


    def __init__(self, acaolendaria, descricao, custo, efeito_nd):
        self.acaolendaria = acaolendaria
        self.custo = custo
        self.descricao = descricao
        self.efeito_nd = efeito_nd
        
    def __repr__(self):
        return f"<Lendaria {self.acaolendaria}>"