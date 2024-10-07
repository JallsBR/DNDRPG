from database.database import db

class CenarioCampanha(db.Model):
    __tablename__ = "cenario_campanha"

    id = db.Column(db.Integer, primary_key=True)
    id_cenario = db.Column(db.Integer, db.ForeignKey('cenario.id'), nullable=False)
    id_campanha = db.Column(db.Integer, db.ForeignKey('campanha.id'), nullable=False)
    notas = db.Column(db.Text, nullable=True)


    def __init__(self, id_cenario, id_campanha, notas=None):
        self.id_cenario = id_cenario
        self.id_campanha = id_campanha
        self.notas = notas

    @classmethod
    def get_all_por_campanha(cls, id_campanha):
        return cls.query.filter_by(id_campanha=id_campanha).all()

    @classmethod
    def delete(cls, id):
        cenario_campanha_obj = cls.query.filter_by(id=id).first()
        if cenario_campanha_obj:
            db.session.delete(cenario_campanha_obj)
            db.session.commit()
            return True
        return False

    @classmethod
    def update(cls, id, id_cenario=None, id_campanha=None, notas=None):
        cenario_campanha_obj = cls.query.filter_by(id=id).first()
        if cenario_campanha_obj:
            if id_cenario is not None:
                cenario_campanha_obj.id_cenario = id_cenario  # Atualiza o id_cenario se fornecido
            if id_campanha is not None:
                cenario_campanha_obj.id_campanha = id_campanha  # Atualiza o id_campanha se fornecido
            if notas is not None:
                cenario_campanha_obj.notas = notas  # Atualiza as notas se fornecido
            db.session.commit()
            return cenario_campanha_obj
        return None
