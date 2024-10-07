from database.database import db

class EncontroCampanha(db.Model):
    __tablename__ = "encontros_campanha"

    id = db.Column(db.Integer, primary_key=True)
    id_encontro = db.Column(db.Integer, db.ForeignKey('encontros.id'), nullable=False)
    id_campanha = db.Column(db.Integer, db.ForeignKey('campanha.id'), nullable=False)
    notas = db.Column(db.JSON, nullable=False)


    def __init__(self, id_encontro, id_campanha, notas=None):
        self.id_encontro = id_encontro
        self.id_campanha = id_campanha
        self.notas = notas


    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def delete(cls, id):
        encontro_campanha_obj = cls.query.filter_by(id=id).first()
        if encontro_campanha_obj:
            db.session.delete(encontro_campanha_obj)
            db.session.commit()
            return True
        return False
