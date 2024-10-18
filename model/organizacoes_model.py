from database.database import db
from sqlalchemy import func

class Organizacoes(db.Model):
    __tablename__ = "organizacoes"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))  
    org = db.Column(db.JSON, nullable=False)
    


    def __init__(self, id_user, org):
        self.org = org
        self.id_user = id_user

    @classmethod
    def org_userid(cls, id_user):
        return cls.query.filter_by(id_user=id_user).order_by(func.json_extract(cls.org, '$.nome')).all()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_por_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def delete(cls, id):
        organizacao_obj = cls.query.filter_by(id=id).first()
        if organizacao_obj:
            db.session.delete(organizacao_obj)
            db.session.commit()
            return True
        return False

    @classmethod
    def update(cls, id, org):
        organizacao_obj = cls.query.filter_by(id=id).first()
        if organizacao_obj:
            organizacao_obj.org = org
            db.session.commit()
            return organizacao_obj
        return None
