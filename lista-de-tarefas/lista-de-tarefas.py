while True:
  print('\nMenu do Gerenciador de Lista de Tarefas')
  print('1. Adicionar tarefa')
  print('2. Ver tarefas')
  print('3. Atualizar tarefa')
  print('4. Completar tarefa')
  print('5. Deletar tarefas concluidas')
  print('6. Sair')

  escolha = int(input('Digite a sua escolha: '))

  if escolha > 6: # Opão que não está no programa
    print('Escolha uma opção válida!')

  if escolha == 6: # Usuário escolheu sair do programa
    break