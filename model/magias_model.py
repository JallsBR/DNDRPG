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
    def classe_magias(cls, classe, pt=True, nivel=None):
        classe_numero = CLASSES_NUMERO.get(classe)


        query = cls.query.filter(cls.magia['classes'].contains([classe_numero]))

        if nivel is not None:

            if nivel == "truque":
                query = query.filter(cls.magia['nivel'] == 'truque')
            else:
                query = query.filter(cls.magia['nivel'] == str(nivel))

        if pt:
            return query.order_by(asc(cls.magia['nome'])).all()
        else:
            return query.order_by(asc(cls.magia['spellname'])).all()

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
            
    @classmethod
    def filtrar_magias(cls, classe=None, escola=None, organizar=None, pt=True):
        """
        Filtra as magias com base em classe, escola e critério de organização.
        """
        query = cls.query

        if classe and classe != "Todas":

            classe_numero = CLASSES_NUMERO.get(classe)
            if classe_numero is not None:

                query = query.filter(cls.magia['classes'].contains([classe_numero]))       

        if escola and escola != "Todas":
            escola_numero = ESCOLAS_NUMERO.get(escola)
            if escola_numero is not None:
                query = query.filter(cls.magia['escola'] == escola_numero)

        if organizar == 'Nome':
            query = query.order_by(asc(cls.magia['nome'])) if pt else query.order_by(asc(cls.magia['spellname']))
        elif organizar == 'NomeOriginal':
            query = query.order_by(asc(cls.magia['spellname']))
        elif organizar == 'Nivel':
            query = query.order_by(
                case(
                    (cls.magia['nivel'] == 'truque', 0),
                    else_=cast(cls.magia['nivel'], Integer)
                )
            )
        else:
            query = query.order_by(asc(cls.magia['nome']))

        return query.all()
