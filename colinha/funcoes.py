# Declaração
def dizer_oi(nome):
  return f'Oi {nome}'

# Função que retorna o número ao quadrado
def quadrado(numero):
  return numero ** 2

# Função com mais de um parametro
def soma(num_1, num_2):
  soma = num_1 + num_2
  return soma

print(dizer_oi('Joao')) # Podemos printar o retorno da função direto

resultado = quadrado(4) # Ou atribuir o seu valor numa variavel
print(resultado)        # e exibir depois

soma = soma(3, 2)
print(soma)