import ast

# define as estruturas de sintaxe extraídas
class StructuresExtractor(ast.NodeVisitor):

    # tuplas que armazenam as informações necessárias de cada estrutura
    def __init__(self):
        self.filtered_ast = []

    # encontra função
    # def visit_FunctionDef(self, node):
    #     self.filtered_ast.append(("Função", node.name, node.col_offset))
    #     self.generic_visit(node)

    # encontra for
    def visit_For(self, node):
        self.filtered_ast.append(("Laço", node.col_offset))
        self.generic_visit(node)
    
    # encontra while
    def visit_While(self, node):
        self.filtered_ast.append(("Laço", node.col_offset))
        self.generic_visit(node)

    # encontra if-elif-else
    # um 'elif' é representado como um 'If' dentro do orelse do 'if' anterior
    def visit_If(self, node):
        self.filtered_ast.append(("Condição", node.col_offset))
        self.generic_visit(node)

        # encontra 'elif' e 'else'
        current_node = node
        while current_node.orelse:
            # verifica se o próximo nó é um 'elif'
            if isinstance(current_node.orelse[0], ast.If):
                current_node = current_node.orelse[0]
                self.filtered_ast.append(("Condição", current_node.col_offset))
                self.generic_visit(current_node)
            else:
                # se não for um 'If', é um 'else'
                if current_node.orelse:
                    self.filtered_ast.append(("Condição", current_node.orelse[0].col_offset))
                break

# cria a AST, extraindo as estruturas de sintaxe
def extract_structures(solution_file):

    with open(solution_file, 'r') as file:
        source_code = file.read()

    # converte o código fonte em AST
    tree = ast.parse(source_code)

    # define o extrator e percorre a AST
    extractor = StructuresExtractor()
    extractor.visit(tree)

    return extractor.filtered_ast
