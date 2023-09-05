import sqlite3

conexao_cliente = sqlite3.connect('clientes')
cursor = conexao_cliente.cursor()

#cursor.execute('CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

# ADICIONANDO CLIENTES
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1,"Luís", 20, 1000.5)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2, "Márcia", 43, 5250.5)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3, "Hugo", 37, 4950.0)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4, "João", 34, 200.5)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5, "Vera", 28, 72)')

''' # Nome e idade de clientes +30

dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade >= 30')
for clientes in dados:
    print(clientes)
'''
''' # Média de saldos

dados = cursor.execute('SELECT AVG(saldo) FROM clientes') #função para calcular média
for saldo in dados:
    print(f'A média entre os saldos é igual a R${saldo}')
'''
''' # Maior saldo

dados = cursor.execute('SELECT MAX(saldo) FROM clientes') #função de maior valor
for saldo in dados:
    print(f'O maior saldo é de R${saldo}')
'''
''' # Clientes com saldo acima de 1000

dados = cursor.execute('SELECT COUNT(saldo) FROM clientes WHERE saldo > 1000')
for saldo in dados:
    print(f'Há {saldo} clientes com saldo acima de R$1000!')
'''
''' # Mudando saldo de cliente  

cursor.execute('UPDATE clientes SET saldo=500.5 WHERE id=5')
'''
''' # Excluindo cliente

cursor.execute('DELETE FROM clientes WHERE id=4')
'''

#cursor.execute('CREATE TABLE compras()')

conexao_cliente.commit()
conexao_cliente.close()
