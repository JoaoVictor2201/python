def adicionar_tarefa(tarefas, titulo='Nao informado'):
  tarefa = {
    "nome": titulo,
    "concluida": True
  }
  tarefas.append(tarefa)
  print(f'Tarefa -{titulo}- adicionada')
  return

tarefas = [] # Iniciando a lista de tarefas

while True:
  print('\nMenu do Gerenciador de Lista de Tarefas')
  print('1. Adicionar tarefa')
  print('2. Ver tarefas')
  print('3. Atualizar tarefa')
  print('4. Completar tarefa')
  print('5. Deletar tarefas concluidas')
  print('6. Sair')

  escolha = int(input('Digite a sua escolha: '))

  if escolha == 1:
    titulo = input('Informe o nome da tarefa: ')
    adicionar_tarefa(tarefas, titulo)

  elif escolha == 2:
    for tarefa in tarefas:
      print(f'[ ]' if tarefa["concluida"] == False else '[x]', end=' - ')
      print(tarefa["nome"])
  
  elif escolha == 3:
    break

  elif escolha == 6:
    break

  else: # Opão que não está no programa
    print('Escolha uma opção válida!')