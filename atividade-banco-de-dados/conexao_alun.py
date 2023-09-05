import sqlite3

conexao_alun = sqlite3.connect('alunos')
cursor = conexao_alun.cursor()

#cursor.execute('CREATE TABLE estudante(id INT,nome VARCHAR(100),idade INT,curso VARCHAR(100));') 

#cursor.execute('INSERT INTO estudante(id, nome, idade,curso) VALUES(1, "Pedro", 29, "Engenharia")')
#cursor.execute('INSERT INTO estudante(id, nome, idade, curso) VALUES (2,"Marília", 24, "Psicologia");')
#cursor.execute('INSERT INTO estudante(id, nome, idade, curso) VALUES (3,"Marina", 26, "Psicologia")')
#cursor.execute('INSERT INTO estudante(id, nome, idade, curso) VALUES (4,"Carolina", 29, "Matemática")')
#cursor.execute('INSERT INTO estudante(id, nome, idade, curso) VALUES (5,"João", 50, "Contabilidade")')
#cursor.execute('INSERT INTO estudante(id, nome, idade, curso) VALUES (6,"Júlia", 18, "Contabilidade")')

''' # SELECIONANDO TODOS OS REGISTROS DA TABELA

dados = cursor.execute('SELECT * FROM estudante')
for estudante in dados:
    print(estudante)
'''
''' # MOSTRANDO ALUNOS QUE TEM IDADE MAIOR QUE 20

dados = cursor.execute('SELECT nome,idade FROM estudante WHERE idade > 20')
for estudante in dados:
    print(estudante)
'''
''' # MOSTRANDO ALUNO DO CURSO DE ENGENHARIA

dados = cursor.execute('SELECT * FROM estudante WHERE curso ="Engenharia"')
for estudante in dados:
    print(estudante)
'''
''' # CONTANDO QUANTOS ALUNOS FORAM CADASTRADOS

cont = 0
dados = cursor.execute('SELECT * FROM estudante')
for estudante in dados:
    cont += 1
print(f'Ao todo tem {cont} cadastros na tabela "alunos"!')
'''
''' # ATUALIZANDO IDADE

# cursor.execute('INSERT INTO estudante(id, nome, idade, curso) VALUES (5,"João", 50, "Contabilidade")')
cursor.execute('UPDATE estudante SET idade = 30 WHERE nome = "João"')
'''
''' # EXCLUINDO ID

cursor.execute('DELETE FROM estudante WHERE id=5')
'''

dados = cursor.execute('SELECT * FROM estudante')
for estudante in dados:
    print(estudante)


conexao_alun.commit()
conexao_alun.close()