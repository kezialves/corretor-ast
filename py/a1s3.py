import numpy as np

def inputMatriz():
    # Lê a entrada do usuário e divide em linhas
    entrada = input("Digite a matriz: ")
    linhas = entrada.split(';')
    
    # Cria a matriz usando NumPy
    matriz = np.array([list(map(int, linha.strip().split(','))) for linha in linhas])
    return matriz

def somaMatriz(matriz1, matriz2):
    # Verifica se as matrizes têm as mesmas dimensões
    if matriz1.shape != matriz2.shape:
        return None
    
    # Soma as matrizes usando NumPy
    return matriz1 + matriz2

# Programa principal
matriz1 = inputMatriz()
matriz2 = inputMatriz()

resultado = somaMatriz(matriz1, matriz2)

if resultado is None:
    print("Não é possível somar as matrizes")
else:
    print("Matriz resultante:")
    print(resultado)
