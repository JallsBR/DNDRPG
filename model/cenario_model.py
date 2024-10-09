from database.database import db
from sqlalchemy import func


class Cenario(db.Model):
    __tablename__ = "cenario"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))  
    cenario = db.Column(db.JSON, nullable=False)
    tipo = db.Column(db.String(15), nullable=False)


    def __init__(self, id_user, cenario, tipo):
        self.id_user = id_user
        self.cenario = cenario
        self.tipo = tipo

    @classmethod
    def cenario_userid(cls, id_user):
        return cls.query.filter_by(id_user=id_user).order_by(func.json_extract(cls.cenario, '$.nome')).all()

    @classmethod
    def update(cls, id, cenario=None, tipo=None):
        cenario_obj = cls.query.filter_by(id=id).first()
        if cenario_obj:
            if cenario is not None:
                cenario_obj.cenario = cenario  
            if tipo is not None:
                cenario_obj.tipo = tipo  
            db.session.commit()
            return cenario_obj
        return None

    @classmethod
    def delete(cls, id):
        cenario_obj = cls.query.filter_by(id=id).first()
        if cenario_obj:
            db.session.delete(cenario_obj)
            db.session.commit()
            return True
        return False
