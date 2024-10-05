from database.database import db
from sqlalchemy import or_



class Personagem(db.Model):
    __tablename__ = "personagens"
    
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))  
    ficha = db.Column(db.JSON, nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    tipo = db.Column(db.String(25), nullable=False, default="não informado")


    user = db.relationship("User", foreign_keys=[id_user], back_populates="personagens")


    def __init__(self, id_user,ficha, nome, tipo="não informado"):
        self.id_user = id_user
        self.ficha = ficha
        self.nome = nome
        self.tipo = tipo    
    
    @classmethod
    def npcs_id(cls, id_user, id=None):
        query = cls.query.filter_by(id_user=id_user, tipo="NPC")
        
        if id is not None:
            query = query.filter_by(id=id)
        
        # Ordenar os NPCs pelo campo 'nome'
        query = query.order_by(cls.nome.asc())
        
        return query.all()
    
    @classmethod
    def monstros(cls, id_user, id=None):
        query = cls.query.filter_by(id_user=id_user, tipo="Criatura")
        
        if id is not None:
            # Filtrar pelo id ou por registros onde id seja None
            query = query.filter(or_(cls.id == id, cls.id == None))
        
        # Ordenar os NPCs pelo campo 'nome'
        query = query.order_by(cls.nome.asc())
        
        return query.all()
    
        
    @classmethod
    def update_ficha(cls, id, nova_ficha, novo_nome):
        npc = cls.query.get(id)
        if npc:
            npc.ficha = nova_ficha
            npc.nome = novo_nome
            db.session.commit()
            return npc
        return None
    
    
    # Função para deletar o personagem
    @classmethod
    def delete(cls, id):
        npc = cls.query.get(id)
        if npc:
            db.session.delete(npc)
            db.session.commit()
            return True
        return False
    
    @classmethod
    def npc_por_id(cls, id):
        query = cls.query.filter_by(id=id)
        return query.first()  