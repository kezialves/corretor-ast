def inputMatriz():
    # Lê a entrada do usuário
    entrada = input("Digite a matriz: ")
    
    # Divide a entrada em linhas
    linhas = entrada.split(';')
    
    # Inicializa a matriz
    matriz = []
    
    for linha in linhas:
        # Remove espaços em branco e divide os números por vírgula
        numeros = linha.strip().split(',')
        
        # Converte os números para inteiros e adiciona à matriz
        linha_matriz = [int(numero) for numero in numeros]
        matriz.append(linha_matriz)
    
    return matriz

def somaMatriz(matriz1, matriz2):
    # Verifica se as matrizes têm as mesmas dimensões
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None
    
    # Inicializa a matriz resultante
    resultado = []
    
    for i in range(len(matriz1)):
        linha_resultado = []
        for j in range(len(matriz1[0])):
            # Soma os elementos correspondentes
            linha_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(linha_resultado)
    
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
