import ast_generator
import os
from fuzzywuzzy import fuzz

# faz a correção do código solução
def corrector(solution_file, template_file):

    # gera a AST do gabarito
    ast_generator.ast_generator(template_file)
    # gera a AST da solução
    ast_generator.ast_generator(solution_file)

    # lê a AST do gabarito e coloca numa string
    with open(os.path.join("txt", os.path.splitext(os.path.basename(template_file))[0] + "_ast.txt"), 'r') as file:
        template_ast = file.read().replace('\n', '/')

    # print(template_ast)
    # print()

    # lê a AST da solução e coloca numa string
    with open(os.path.join("txt", os.path.splitext(os.path.basename(solution_file))[0] + "_ast.txt"), 'r') as file:
        solution_ast = file.read().replace('\n', '/')

    # print(solution_ast)
    # print()

    # calcula a similaridade usando distância de levenshtein
    similarity = fuzz.partial_ratio(template_ast, solution_ast)

    # define um limite para aceitação da solução
    if similarity >= 75.0:
        print(f"✅ Solução correta com {similarity:.2f}% de similaridade.")
    else:
        print(f"❌ Solução incorreta com {similarity:.2f}% de similaridade.")

# calcula a similaridade entre o código solução e o gabarito linha a linha
# def calculate_similarity(template_ast, solution_ast):

#     # lê cada linha dos dois arquivos
#     with open(template_ast, 'r') as template, open(solution_ast, 'r') as solution:
#         template_lines = template.readlines()
#         solution_lines = solution.readlines()

#     total_lines = len(template_lines) # total de linhas do gabarito
#     matching_lines = 0 # total de linhas iguais

#     # compara as linhas dos dois arquivos
#     for template_lines, solution_lines in zip(template_lines, solution_lines):
#         if template_lines == solution_lines:
#             matching_lines += 1

#     # calcula a porcentagem de semelhança
#     if total_lines == 0: # caso base para evitar divisão por zero
#         return 0.0
#     return (matching_lines/total_lines) * 100
