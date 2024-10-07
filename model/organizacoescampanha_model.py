from database.database import db

class OrganizacoesCampanha(db.Model):
    __tablename__ = "organizacoes_campanha"

    id = db.Column(db.Integer, primary_key=True)
    id_organizacao = db.Column(db.Integer, db.ForeignKey('organizacoes.id'), nullable=False)
    id_campanha = db.Column(db.Integer, db.ForeignKey('campanha.id'), nullable=False)
    notas = db.Column(db.String(255), nullable=True)


    def __init__(self, id_organizacao, id_campanha, notas=None):
        self.id_organizacao = id_organizacao
        self.id_campanha = id_campanha
        self.notas = notas

    @classmethod
    def get_all_por_campanha(cls, id_campanha):
        return cls.query.filter_by(id_campanha=id_campanha).all()

    @classmethod
    def delete(cls, id):
        org_campanha_obj = cls.query.filter_by(id=id).first()
        if org_campanha_obj:
            db.session.delete(org_campanha_obj)
            db.session.commit()
            return True
        return False

    @classmethod
    def update(cls, id, id_organizacao, id_campanha, notas):
        org_campanha_obj = cls.query.filter_by(id=id).first()
        if org_campanha_obj:
            org_campanha_obj.id_organizacao = id_organizacao
            org_campanha_obj.id_campanha = id_campanha
            org_campanha_obj.notas = notas
            db.session.commit()
            return org_campanha_obj
        return None
