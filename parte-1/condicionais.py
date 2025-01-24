idade = 18

# if
if idade >= 18:
  print('Maior de idade')

if idade < 18:
  print('Menor de idade')

# elif
if idade >= 18:
  print('Maior de idade')
elif idade < 18:
  print('Menor de idade')

# else
if idade >= 18:
  print('Maior de idade')
else:
  print('Menor de idade')

# Diferença
if idade != 20:
  print('Você não tem 20 anos')
else:
  print('Você tem 20 anos')

# Sintaxe reduzida
print('Maior de idade' if idade >= 18 else 'Menor de idade')
print('Você não tem 20 anos' if idade != 20 else 'Você tem 20 anos')