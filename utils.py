from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Lourenco', idade=23)
    print(pessoa)
    pessoa.save()


def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lourenco').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lourenco').first()
    pessoa.delete()


if __name__ == '__main__':
    # exclui_pessoa()
    # altera_pessoa()
    # insere_pessoas()
    # consulta_pessoa()
