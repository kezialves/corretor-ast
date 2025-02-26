def inputMatriz():
    # Lê a entrada do usuário e divide em linhas
    entrada = input("Digite a matriz: ")
    linhas = entrada.split(';')
    
    # Usa list comprehension para criar a matriz
    matriz = [[int(numero) for numero in linha.strip().split(',')] for linha in linhas]
    return matriz

def somaMatriz(matriz1, matriz2):
    # Verifica se as matrizes têm as mesmas dimensões
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None
    
    # Usa list comprehension e zip para somar as matrizes
    resultado = [
        [a + b for a, b in zip(linha1, linha2)]
        for linha1, linha2 in zip(matriz1, matriz2)
    ]
    return resultado

# Programa principal
matriz1 = inputMatriz()
matriz2 = inputMatriz()

resultado = somaMatriz(matriz1, matriz2)

if resultado is None:
    print("Não é possível somar as matrizes")
else:
    print("Matriz resultante:")
    for linha in resultado:
        print(linha)
