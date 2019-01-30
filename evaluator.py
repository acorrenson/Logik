from parser import *

def evaluate(ast):
    op = ast[0]

    if op == 'symb':
        # TODO : evaluate according to ENV
        return 1
    elif op == 'value':
        return ast[1]
    elif op == 'unop':
        return 1 - evaluate(ast[1])
    elif op == 'ou':
        return max(evaluate(ast[1]), evaluate(ast[2]))
    elif op == 'et':
        return min(evaluate(ast[1]), evaluate(ast[2]))
    elif op == '->':
        return max(1 - evaluate(ast[1]), evaluate(ast[2]))


if __name__ == '__main__':
    # input
    string = input('>>> ')
    # lexing
    tokens = lex(string)
    # parsing
    seq = Seq(list(tokens))
    ast = parse(seq)
    # display the AST
    pprint(ast)
    print("\nRESULT : ", end=" ")
    print(evaluate(ast))

        
