from sqlalchemy import asc, desc, case
from database.database import db

class Magias(db.Model):
    __tablename__ = "magias"

    id = db.Column(db.Integer, primary_key=True)
    magia = db.Column(db.JSON, nullable=False)

    def __init__(self, magia):
        self.magia = magia

    @classmethod
    def criar_magia(cls, magia_data):
        """Cria uma nova magia no banco de dados"""
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
        """Retorna uma magia pelo ID"""
        return cls.query.get(magia_id)

    @classmethod
    def alterar_magia(cls, magia_id, updated_data):
        """Atualiza uma magia existente"""
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
        """Deleta uma magia pelo ID"""
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
        """
        Retorna todas as magias que pertencem a uma classe específica,
        em ordem alfabética pelo nome em português ou inglês.
        Filtra também por nível, se fornecido.
        """
        query = cls.query.filter(cls.magia['classes'].contains([classe]))

        if nivel is not None:
            # Se um nível for especificado, filtra as magias pelo nível
            if nivel == "truque":
                query = query.filter(cls.magia['nivel'] == 'truque')
            else:
                query = query.filter(cls.magia['nivel'] == str(nivel))

        # Ordena pelo nome em português ou inglês
        if pt:
            return query.order_by(asc(cls.magia['nome'])).all()
        else:
            return query.order_by(asc(cls.magia['spellname'])).all()

    @classmethod
    def todas_magias_por_nivel(cls, pt=True):
        """
        Retorna todas as magias em ordem crescente de nível
        (tratando "truque" como nível 0), em português ou inglês
        """
        if pt:
            # Trata o nível "truque" como 0 e ordena pelo nível numérico
            return cls.query.order_by(
                case(
                    [(cls.magia['nivel'] == 'truque', 0)],
                    else_=cls.magia['nivel'].cast(db.Integer)
                )
            ).all()
        else:
            # Ordena por nível em inglês (assumindo que os níveis estão no mesmo formato)
            return cls.query.order_by(
                case(
                    [(cls.magia['nivel'] == 'truque', 0)],
                    else_=cls.magia['nivel'].cast(db.Integer)
                )
            ).all()