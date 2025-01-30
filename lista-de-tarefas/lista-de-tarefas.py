def adicionar_tarefa(tarefas):
  titulo = input('Informe o nome da tarefa: ')
  tarefa = {
    "nome": titulo,
    "concluida": False
  }
  tarefas.append(tarefa)
  print(f'Tarefa --{titulo}-- adicionada')
  return

def exibir_tarefas(tarefas):
  for tarefa in tarefas:
    if not tarefa["concluida"]:
      print(f'[ ] - {tarefa["nome"]}')
    else:
      print(f'[x] - {tarefa["nome"]}')
  return

def atualizar_tarefa(tarefas):
  exibir_tarefas(tarefas)
  escolha_atualizar = int(input('Qual tarefa você deseja atualizar: '))
  novo_titulo = input('Qual o novo nome da sua tarefa: ')
  tarefas[escolha_atualizar - 1]["nome"] = novo_titulo
  return

def concluir_tarefa(tarefas):
  exibir_tarefas(tarefas)
  escolha_concluir = int(input('Qual tarefa você concluiu: '))
  tarefas[escolha_concluir - 1]["concluida"] = True
  print(f'Tarefa {tarefas[escolha_concluir - 1]["nome"]} concluida!')
  return

def apagar_concluidas(tarefas):
  for tarefa in tarefas:
    if tarefa["concluida"]:
      tarefas.remove(tarefa)
  return


tarefas = [] # Iniciando a lista de tarefas

while True:
  print('\nMenu do Gerenciador de Lista de Tarefas')
  print('1. Adicionar tarefa')
  print('2. Ver tarefas')
  print('3. Atualizar tarefa')
  print('4. Concluir tarefa')
  print('5. Deletar tarefas concluidas')
  print('6. Sair')

  escolha = int(input('Digite a sua escolha: '))

  if escolha == 1:
    adicionar_tarefa(tarefas)

  elif escolha == 2:
    exibir_tarefas(tarefas)
  
  elif escolha == 3:
    atualizar_tarefa(tarefas)

  elif escolha == 4:
    concluir_tarefa(tarefas)

  elif escolha == 5:
    apagar_concluidas(tarefas)
    exibir_tarefas(tarefas)

  elif escolha == 6:
    break

  else: # Opção que não está no programa
    print('Escolha uma opção válida!')
