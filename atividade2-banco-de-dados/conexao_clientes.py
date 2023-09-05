import sqlite3

conexao_clientes = sqlite3.connect('clientes')
cursor = conexao_clientes.cursor()


#cursor.execute('CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

# ADICIONANDO CLIENTES
'''
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1,"Luís", 20, 1000.5)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2,"Márcia", 42, 7850.5)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3,"Júlia", 27, 100.2)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4,"Pedro", 34, 5000.0)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5,"Rafael", 32, 70.0)')
'''
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

dados = cursor.execute('SELECT MAX(saldo),nome FROM clientes') #função de maior valor
for saldo in dados:
    print(f'O maior saldo é de R${saldo}')
'''
''' # Clientes com saldo acima de 1000

dados = cursor.execute('SELECT COUNT(saldo) FROM clientes WHERE saldo > 1000')
for saldo in dados:
    print(f'Há {saldo} clientes com saldo acima de R$1000!')
'''
''' # Mudando saldo de cliente

cursor.execute('UPDATE clientes SET saldo=500.5 WHERE id=3')
'''
''' # Excluindo cliente

cursor.execute('DELETE FROM clientes WHERE id=5')
'''
""" # Criando nova tabela --> chave estrangeira

result = cursor.execute('''CREATE TABLE compras (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto VARCHAR(250),
    valor FLOAT,
    CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes (id)
)''')
"""
""" # Inserindo dados na nova tabela

result = cursor.execute('''INSERT INTO compras (id, cliente_id, produto, valor) VALUES
( 1, 1, 'Caderno', 20.0),
( 2, 1, 'Caneta', 1.10),
( 3, 2, 'Caderno', 24.0)''')
"""

result = cursor.execute('''SELECT c.nome, co.produto, co.valor
from compras as co
INNER JOIN clientes as c on c.id = co.cliente_id''')

for item in result:
    print(item)

conexao_clientes.commit()
conexao_clientes.close()
