from database.database import db
from model.magias_model import Magias


class MestreController:

    @staticmethod
    def ajuste_exibir_magias(classe=None, escola=None, organizar=None, pt=True, nivel=None):
        magias = Magias.todas_magias()
        organizarmagias = magias

        if classe and classe != 'Todas':
            organizarmagias = [magia for magia in organizarmagias if int(classe) in magia.magia['classes']]

        if escola and escola != 'Todas':
            organizarmagias = [magia for magia in organizarmagias if escola == magia.magia['escola'] ]

        if nivel and nivel != 'Todos':
            if nivel == 'Truque':
                organizarmagias = [magia for magia in organizarmagias if magia.magia['nivel'] == 'Truque']
            else:
                organizarmagias = [magia for magia in organizarmagias if int(magia.magia['nivel']) == int(nivel)]

        if organizar == 'Nome':
            organizarmagias = sorted(organizarmagias, key=lambda magia: magia.magia['nome'])
        elif organizar == 'NomeOriginal':
            organizarmagias = sorted(organizarmagias, key=lambda magia: magia.magia['spellname'])
        elif organizar == 'Nivel':
            organizarmagias = sorted(organizarmagias, key=lambda magia: (magia.magia['nivel'] != 'Truque', magia.magia['nivel']))

        return organizarmagias