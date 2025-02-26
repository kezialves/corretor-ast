import argparse
import os
import corrector

def main(solution_file, template_file):

    # verifica se o arquivo solução existe
    if not os.path.exists(solution_file):
        print(f"Erro: Arquivo '{solution_file}' não encontrado.\n")
        return

    # verifica se o arquivo solução é .py
    if not solution_file.endswith(".py"):
        print("Erro: O arquivo solução não é um arquivo Python.\n")
        return
    
    # verifica se o arquivo gabarito existe
    if not os.path.exists(template_file):
        print(f"Erro: Arquivo '{template_file}' não encontrado.\n")
        return

    # verifica se o arquivo gabarito é .py
    if not template_file.endswith(".py"):
        print("Erro: O arquivo gabarito não é um arquivo Python.\n")
        return

    # chama o corretor
    corrector.corrector(solution_file, template_file)

# configura o parser de argumentos
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Compara um arquivo solução com um arquivo gabarito.")
    
    parser.add_argument(
        "solucao", # nome do argumento
        help="Caminho do arquivo solução Python." # mensagem de ajuda
    )

    parser.add_argument(
        "gabarito", # nome do argumento
        help="Caminho do arquivo gabarito Python." # mensagem de ajuda
    )

    # faz o parser dos argumentos
    args = parser.parse_args()

    # chama a main com o nome do arquivo passado como argumento
    main(args.solucao, args.gabarito)

# python3 main.py py/a1s1.py py/a1t.py
