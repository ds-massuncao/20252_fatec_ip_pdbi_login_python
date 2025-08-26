import psycopg

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

def existe(usuario):
    with psycopg.connect(
        host = 'localhost',
        port = '5432',
        dbname = '20252_fatec_ipi_pbdi_marcos_assuncao',
        user = 'postgres',
        password  = 'postgres'
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM tb_usuario WHERE login = %s AND senha = %s',
                (f'{usuario.login}', f'{usuario.senha}')
            )
            result = cursor.fetchone()
            return result != None

def inserir(usuario):
    with psycopg.connect(
        host = 'localhost',
        port = '5432',
        dbname = '20252_fatec_ipi_pbdi_marcos_assuncao',
        user = 'postgres',
        password  = 'postgres'
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_usuario (login, senha) Values %s, %s'
                
            )
            result = cursor.fetchone()
            return result

def menu():
    texto = '0-Sair\n1-login\n2-logoff\n3-Cadastrar\n'
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input('Digite seu login')
            senha = input('Digite sua senha')
            usuario = Usuario(login,senha)
            print("usuario OK" if existe(usuario) else "Usuario NOK")        
        elif op == 2:
            usuario = None
            print('logoff feito com sucesso')
        op = int(input(texto))
        elif op == 3:
            login = input('Digite seu login')
            senha = input('Digite sua senha')
            usuario = Usuario(login,senha)
            usuario.inserir()
            
    else: 
        print('Até Mais!!')

menu()