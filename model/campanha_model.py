from database.database import db


class Campanha(db.Model):
    __tablename__ = "campanha"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    campanha = db.Column(db.JSON, nullable=False)




    def __init__(self, id_user, campanha):
        self.id_user = id_user
        self.campanha = campanha

    @classmethod
    def get_all_por_userid(cls, id_user):
        # Busca todas as campanhas de um usuário específico
        return cls.query.filter_by(id_user=id_user).all()

    @classmethod
    def update(cls, id, id_user, campanha):
        # Atualiza uma campanha existente
        campanha_obj = cls.query.filter_by(id=id, id_user=id_user).first()
        if campanha_obj:
            campanha_obj.campanha = campanha
            db.session.commit()
            return campanha_obj
        return None

    @classmethod
    def delete(cls, id, id_user):
        # Deleta uma campanha existente
        campanha_obj = cls.query.filter_by(id=id, id_user=id_user).first()
        if campanha_obj:
            db.session.delete(campanha_obj)
            db.session.commit()
            return True
        return False
