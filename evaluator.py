from parser import *
from itertools import product


def get_var(ast):
    var = []
    def r_get_var(ast):
        op = ast[0]
        if op == 'value':
            return
        elif op == 'symb':
            if ast[1] not in var:
                var.append(ast[1])
        elif op == 'non':
            r_get_var(ast[1])
        else:
            r_get_var(ast[1])
            r_get_var(ast[2])

    r_get_var(ast)
    return var


def make_env(var):
    tab = list(product([0, 1], repeat=len(var)))
    env = []
    for lines in tab:
        r = {}
        for i, v in enumerate(var):
            r[v] = lines[i]
        env.append(r)
    return (env, tab)


def evaluate(ast, env):
    op = ast[0]

    if op == 'symb':
        return env[ast[1]]
    elif op == 'value':
        return ast[1]
    elif op == 'non':
        return 1 - evaluate(ast[1], env)
    elif op == 'ou':
        return max(evaluate(ast[1], env), evaluate(ast[2], env))
    elif op == 'et':
        return min(evaluate(ast[1], env), evaluate(ast[2], env))
    elif op == '->':
        return max(1 - evaluate(ast[1], env), evaluate(ast[2], env))


def evaluate_all(ast):
    var = get_var(ast)
    env, tab = make_env(var)
    
    if len(var) > 0:
        print("\nTruth table : \n")
        print(*var)
        print('--'*(len(var)))
        
        for i, row in enumerate(env):
            print(*tab[i], end=' ')
            print(evaluate(ast, row))
    else:
        print("\nValue : \n")
        print(evaluate(ast, {}))


if __name__ == '__main__':
    # input
    string = input('>>> ')
    # lexing
    tokens = lex(string)
    # parsing
    seq = Seq(list(tokens))
    ast = parse(seq)
    # display the AST
    print('\nSyntax tree :\n')
    pprint(ast)
    evaluate_all(ast)

        
