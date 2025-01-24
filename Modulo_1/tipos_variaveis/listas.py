# Declaração
lista_de_compras = ['arroz', 'banana', 'batata', 'manteiga', 'ovo']

# Exibindo
print(f'1 - {lista_de_compras}')
print(f'2 - {lista_de_compras[1]}')
print(f'3 - {lista_de_compras[2:]}')
print(f'4 - {lista_de_compras[:4]}')
print(f'5 - {lista_de_compras[2:4]}')
print(f'6 - {lista_de_compras[-1]}') # último item da lista

# Métodos
lista_de_compras.append('feijão') # Insere no final da lista
lista_de_compras.insert(2, 'detergente') # Insere num índice específico
elemento_removido = lista_de_compras.pop(3) # Remove um índice específico e retorna ele
lista_de_compras.sort() # Ordena a lista