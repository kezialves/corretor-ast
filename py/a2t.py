def exemplo_condicional(valor):
    if valor > 10:
        print("Valor maior que 10")
    elif valor == 10:
        print("Valor igual a 10")
    else:
        print("Valor menor que 10")

def exemplo_repeticao(lista):
    for item in lista:
        if item % 2 == 0:
            print(f"{item} é par")
        else:
            print(f"{item} é ímpar")

    count = 0
    while count < 5:
        print(f"Contagem: {count}")
        count += 1

exemplo_condicional(15)
exemplo_repeticao([1, 2, 3, 4, 5])
