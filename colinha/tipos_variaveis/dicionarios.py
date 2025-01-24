def funcao():
  return 'jogando'

# Declaração
pessoa = {
  "nome": "Joao",
  "idade": 26,
  "jogos Preferidos": ["The Witcher 3", "The Last Of Us", "God of War"],
  "jogar": funcao(),
  "casado": False
}

# Acessando valores das chaves
print(f'1 - Nome: {pessoa["nome"]}')
print(f'2 - {pessoa["funcao"]}')

# Removendo chaves
del pessoa["casado"]

# Método keys()
chaves = pessoa.keys()          # Parece uma lista mas não é
lista_chaves = list(chaves)     # Transformando em lista
print(f'3 - {lista_chaves[2]}') # Exibindo

# Método values()
valores = pessoa.values()
lista_valores = list(valores)
print(f'4 - {lista_valores[2]}')

# Método items()
itens = pessoa.items()
lista_itens = list(itens)
print(f'5 - {lista_itens[2]}')
print(f'6 - {lista_itens[2][1]}')
print(f'7 - {lista_itens[2][1][2]}') 