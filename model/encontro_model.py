from database.database import db

class Encontro(db.Model):
    __tablename__ = "encontros"

    id = db.Column(db.Integer, primary_key=True)
    encontro = db.Column(db.JSON, nullable=False)

    def __init__(self, encontro):
        self.encontro = encontro

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def delete(cls, id):
        encontro_obj = cls.query.filter_by(id=id).first()
        if encontro_obj:
            db.session.delete(encontro_obj)
            db.session.commit()
            return True
        return False

    @classmethod
    def update(cls, id, encontro):
        encontro_obj = cls.query.filter_by(id=id).first()
        if encontro_obj:
            encontro_obj.encontro = encontro
            db.session.commit()
            return encontro_obj
        return None
