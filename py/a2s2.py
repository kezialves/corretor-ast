def ex_cond(valor):
  if valor > 10:
    print("Valor maior que 10")
  elif valor == 10:
    print("Valor igual a 10")
  else:
    print("Valor menor que 10")

def ex_rep(lista):
  for item in lista:
    if item % 2 == 0:
      print(f"{item} é par")
    else:
      print(f"{item} é ímpar")

  count = 0
  while count < 5:
    print(f"Contagem: {count}")
    count += 1

ex_cond(15)
ex_rep([1, 2, 3, 4, 5])
