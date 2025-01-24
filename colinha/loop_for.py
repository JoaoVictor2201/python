lista = [1, 2, 3, 4, 5]
tupla = (5, 4, 3, 2, 1)

pessoa = {
  "nome": "Joao",
  "idade": 26,
  "jogos preferidos": ["The Witcher 3", "The Last Of Us", "God of War"]
}

# for - Lista e Tuplas
for nome_que_quiser in lista:   # Percorrendo cada item da lista
  print(f'lista - {nome_que_quiser}')

print('\n') # Pulando linha

for nome_que_quiser in tupla:
  print(f'tupla - {nome_que_quiser}')

print('\n')

# for - acessando Dicionarios
# chaves
for chaves in pessoa.keys():
  print(f'chave: {chaves}')

print('\n')

# valores das chaves
for valores in pessoa.values():
  print(f'valor: {valores}')

print('\n')

# chaves e valores
for chave, valor in pessoa.items():  # Usando duas variaveis pois a função items() retorna dois valores
  print(f'chave: {chave} | valor: {valor}')

print('\n')

# for - usando range()
for numero in range(10, 15):
  print(f'numero: {numero}')

print('\n')

# for - usando enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f'indice: {indice} | valor: {valor}')