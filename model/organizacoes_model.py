from database.database import db

class Organizacoes(db.Model):
    __tablename__ = "organizacoes"

    id = db.Column(db.Integer, primary_key=True)
    org = db.Column(db.JSON, nullable=False)

    def __init__(self, org):
        self.org = org

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
