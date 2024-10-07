from database.database import db

class NPCsCampanha(db.Model):
    __tablename__ = "npcs_campanha"

    id = db.Column(db.Integer, primary_key=True)
    campanha_id = db.Column(db.Integer, db.ForeignKey('campanha.id'))
    id_personagem = db.Column(db.Integer, db.ForeignKey('personagens.id'))
    descricao = db.Column(db.JSON, nullable=False) 



    def __init__(self, id_campanha, id_personagem, descricao=None):
        self.id_campanha = id_campanha
        self.id_personagem = id_personagem
        self.descricao = descricao

    @classmethod
    def get_all_por_idcampanha(cls, id_campanha):
        return cls.query.filter_by(id_campanha=id_campanha).all()

    @classmethod
    def update(cls, id, id_campanha, id_personagem, descricao=None):
        npc_obj = cls.query.filter_by(id=id).first()
        if npc_obj:
            npc_obj.id_campanha = id_campanha
            npc_obj.id_personagem = id_personagem
            if descricao is not None:
                npc_obj.descricao = descricao  
            db.session.commit()
            return npc_obj
        return None

    @classmethod
    def delete(cls, id):
        npc_obj = cls.query.filter_by(id=id).first()
        if npc_obj:
            db.session.delete(npc_obj)
            db.session.commit()
            return True
        return False
