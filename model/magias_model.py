from sqlalchemy import asc, desc, case, cast, Integer
from database.database import db
CLASSES_NUMERO = {
    'Mago': 1,
    'Clérigo': 2,
    'Feiticeiro': 3,
    'Bardo': 4,
    'Druida': 5,
    'Bruxo': 6,
    'Paladino': 7,
    'Patrulheiro': 8
}

ESCOLAS_NUMERO = {
    'Abjuração': 1,
    'Advinhação': 2,
    'Conjuração': 3,
    'Encantamento': 4,
    'Evocação': 5,
    'Ilusão': 6,
    'Necromancia': 7,
    'Transmutação': 8
}
class Magias(db.Model):
    __tablename__ = "magias"

    id = db.Column(db.Integer, primary_key=True)
    magia = db.Column(db.JSON, nullable=False)

    def __init__(self, magia):
        self.magia = magia

    @classmethod
    def criar_magia(cls, magia_data):
        try:
            nova_magia = cls(magia=magia_data)
            db.session.add(nova_magia)
            db.session.commit()
            return nova_magia
        except Exception as e:
            db.session.rollback()
            return str(e)
        
        

    @classmethod
    def magia_id(cls, magia_id):
        return cls.query.get(magia_id)

    @classmethod
    def alterar_magia(cls, magia_id, updated_data):
        magia = cls.query.get(magia_id)
        if magia:
            try:
                magia.magia = updated_data
                db.session.commit()
                return magia
            except Exception as e:
                db.session.rollback()
                return str(e)
        return None

    @classmethod
    def deletar_magia(cls, magia_id):
        magia = cls.query.get(magia_id)
        if magia:
            try:
                db.session.delete(magia)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                return str(e)
        return False

    @classmethod
    def todas_magias(cls, pt=True):
        """Retorna todas as magias em ordem alfabética pelo nome em português ou inglês"""
        if pt:
            return cls.query.order_by(asc(cls.magia['nome'])).all()
        else:
            return cls.query.order_by(asc(cls.magia['spellname'])).all()

    @classmethod
    def todas_magias_por_nivel(cls, pt=True):
        if pt:
            return cls.query.order_by(
                case(
                    [(cls.magia['nivel'] == 'truque', 0)],
                    else_=cls.magia['nivel'].cast(db.Integer)
                )
            ).all()
        else:
            return cls.query.order_by(
                case(
                    [(cls.magia['nivel'] == 'truque', 0)],
                    else_=cls.magia['nivel'].cast(db.Integer)
                )
            ).all()
            