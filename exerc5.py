# Importando biblioteca de cursos do PyMYSQL

import pymysql.cursors

# Conexão com o Banco de Dados
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interPy',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Inserindo dados dentro de uma tabela MySQL
''' 
name = input('Digite seu nome: ')
endereco = input('Digite seu endereço: ')

x='drop table pessoas'

y='create table pessoas(id smallint(5) primary key auto_increment, nome varchar(80) not null, endereco varchar(300));'

z='insert into pessoas(nome,endereco) values("{}","{}")'.format(name,endereco)

with conexao.cursor() as cursor:
    cursor.execute()
    conexao.commit() # Salva as alterações realizadas no banco de dados

'''

with conexao.cursor() as cursor:
    query = "SELECT * from pessoas"
    cursor.execute(query)
    rows = cursor.fetchall() # Cria um dicionário para cada linha encontrada na tabela do cursor.execute().

for i in rows:
    print('O nome do cliente é {} e ele mora na {}'.format(i['nome'], i['endereco']))

