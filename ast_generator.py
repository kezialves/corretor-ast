import os
import autopep8
import structures_extractor

# gera a AST e a salva em um arquivo texto
def ast_generator(code_file):

    # --------------------------------------------------
    # pré processamento para padronizar a tabulação

    # lê o arquivo de entrada
    with open(code_file, 'r') as file:
        code = file.read()

    # formata o código usando a autopep8
    # aggressive=0 corrige espaçamento, indentação e remove espaços em branco desnecessários
    formatted_code = autopep8.fix_code(code, options={'aggressive': 0})

    # salva o código formatado em um arquivo temporário
    temporary_file = "temp_formatted.py"
    with open(temporary_file, 'w') as file:
        file.write(formatted_code)

    # --------------------------------------------------

    # extrai as estruturas do código formatado
    extracted_nodes = structures_extractor.extract_structures(temporary_file)
    # define o arquivo de saída
    output_file = os.path.join("txt", os.path.splitext(os.path.basename(code_file))[0] + "_ast.txt")

    # escreve a AST no arquivo de saída
    with open(output_file, 'w') as file:
        for item in extracted_nodes:
            # if item[0] == "Função":
            #     node_type, func_name, col = item
            #     indent = "    " * (col // 4)
            #     file.write(f"{indent}{node_type} '{func_name}'\n")
            # else:
                node_type, col = item
                indent = "    " * (col // 4)
                file.write(f"{indent}{node_type}\n")

    # remove o arquivo temporário
    os.remove(temporary_file)
