from parser import *
from itertools import product


def get_vars(ast):
    """List all free variables in an expression"""
    var_list = []
    def r_get_var(ast):
        typ = ast[0]
        if typ == 'value':
            return
        elif typ == 'symb':
            if ast[1] not in var_list:
                var_list.append(ast[1])
        elif typ == 'non':
            r_get_var(ast[1])
        else:
            r_get_var(ast[1])
            r_get_var(ast[2])

    r_get_var(ast)
    return var_list


def make_env(var_list):
    """Build a truth table for an expression"""
    tab = list(product([0, 1], repeat=len(var_list)))
    env_list = []
    for lines in tab:
        env = {}
        for i, v in enumerate(var_list):
            env[v] = lines[i]
        env_list.append(env)
    return (env_list, tab)


def evaluate(ast, env):
    """
        Evaluate an expression according to the valuation 
        described by 'env'
    """
    typ = ast[0]

    if typ == 'symb':
        return env[ast[1]]
    elif typ == 'value':
        return ast[1]
    elif typ == 'non':
        return 1 - evaluate(ast[1], env)
    elif typ == 'ou':
        return max(evaluate(ast[1], env), evaluate(ast[2], env))
    elif typ == 'et':
        return min(evaluate(ast[1], env), evaluate(ast[2], env))
    elif typ == '->':
        return max(1 - evaluate(ast[1], env), evaluate(ast[2], env))


def evaluate_all(ast):
    """
        Evaluate an expression and if it contains free variables, 
        display the truth table.
    """
    var_list = get_vars(ast)
    envs, tab = make_env(var_list)
    
    if len(var_list) > 0:
        print("\nTruth table : \n")
        print(*var_list)
        print('--'*(len(var_list)))
        
        for i, row in enumerate(envs):
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

        
