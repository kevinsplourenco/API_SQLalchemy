from models import Pessoas, Usuarios


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


def insere_usario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    consulta_usuarios()
