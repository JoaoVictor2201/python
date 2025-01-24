contador_1 = 0
contador_2 = 0

while contador_1 < 5: # Loop com condição de parada
  print(f'contador 1: {contador_1}')
  contador_1 += 1

print('\n')

while True: # Loop infinito até que o if seja TRUE
  print(f'contador 2: {contador_2}')
  contador_2 += 1
  if contador_2 == 4:
    print('chegou em 4')
    break
  