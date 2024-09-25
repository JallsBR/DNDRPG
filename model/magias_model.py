from database.database import db


class Magias(db.Model):
    __tablename__ = "magias"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique=True)
    nome_original = db.Column(db.String(40), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False)
    escola = db.Column(db.String(120), nullable=False)
    descrição = db.Column(db.Text, nullable=False)
    descrição_original = db.Column(db.Text)
    tempo = db.Column(db.String(120), nullable=False)
    alcance = db.Column(db.String(120), nullable=False)
    componentes = db.Column(db.String(120), nullable=False)
    duracao = db.Column(db.String(120), nullable=False)
    efeito_nd = db.Column(db.String(150), nullable=False)
    livro = db.Column(db.String(120), nullable=False)
    classes = db.Column(db.String(120), nullable=False)

   


    def __init__(self, nome, level, escola, nome_original, descrição, tempo, alcance, componentes, duracao, efeito_nd ):
        self.nome = nome
        self.level = level
        self.escola = escola
        self.nome_original = nome_original
        self.descrição = descrição
        self.tempo = tempo
        self.alcance = alcance
        self.componentes = componentes
        self.duracao = duracao
        self.efeito_nd = efeito_nd
        
        
    def __repr__(self):
        return f"<Magia {self.nome}>"