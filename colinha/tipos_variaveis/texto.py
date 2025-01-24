# Declaração
nome = "Joao Victor"
sobrenome = "Franca Pontes"

# Formatação
print('Nome:', nome, sobrenome)
print('Nome: ' + nome + ' ' + sobrenome)
print('Nome: %s %s' % (nome, sobrenome))
print(f'Nome: {nome} {sobrenome}')

# Métodos
print(nome.count('o'))
print(nome.find('o', 2))
print(nome.replace('o', 'a', 2))
print(nome.split(' '))
print(nome.startswith('J'))
print("-".join(nome))
print('ao' in nome)