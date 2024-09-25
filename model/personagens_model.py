from database.database import db


class Personagem(db.Model):
    __tablename__ = "personagens"
    
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    ficha = db.Column(db.JSON, nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    tipo = db.Column(db.String(25), nullable=False, default="não informado")


    user = db.relationship("User", foreign_keys=[id_user], back_populates="personagens")


    def __init__(self, id_user,ficha, nome, tipo="não informado"):
        self.id_user = id_user
        self.ficha = ficha
        self.nome = nome
        self.tipo = tipo    
