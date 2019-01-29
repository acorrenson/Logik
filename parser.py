from lexer import *


def priority(char):
    if char == "non":
        return 5
    if char == "et":
        return 4
    if char == "ou":
        return 3
    if char == "->":
        return 1


class Seq:
    def __init__(self, string):
        self.str = string
        self.index = -1

    def next_char(self):
        self.index += 1
        if self.index < len(self.str):
            return self.str[self.index]
        return None

    def see_next(self):
        if self.index+1 < len(self.str):
            return self.str[self.index+1]
        return None


def parse(seq, end=None):

    expr = []
    oper = []

    c = seq.next_char()

    while c not in (end, (end, '')):

        if c[0] == 'symb':
            expr.append(('symb', c[1]))

        elif c[0] == "(":
            expr.append(parse(seq, ")"))
            print(expr)

        elif c[0] == 'binop':
            if len(oper) > 0:
                t = oper[-1]
                while len(oper) > 0 and priority(t) >= priority(c[1]):
                    op = oper.pop()
                    op2 = expr.pop()
                    op1 = expr.pop()
                    expr.append((op, op1, op2))
            oper.append(c[1])

        elif c[0] == 'unop':
            if seq.see_next() is None:
                raise Exception("error")
            elif seq.see_next()[0] == "(":
                seq.next_char()
                e = parse(seq, ')')
                expr.append(('non', e))
            elif seq.see_next()[0] == "symb":
                e = seq.next_char()
                expr.append(('non', e))

        c = seq.next_char()

    while len(oper) != 0:
        op = oper.pop()
        op2 = expr.pop()
        op1 = expr.pop()
        expr.append((op, op1, op2))

    return expr.pop()


def pprint(ast):
    def red(string):
        return '\033[31m' + string + '\033[0m'
    def print_rec(ast, i):
        if ast[0] == "symb":
            print("  "*i + ast[1])
        elif ast[0] == "non":
            print("  "*i + red(ast[0]))
            print_rec(ast[1], i+1)
        else:
            print("  "*i + red(ast[0]))
            print_rec(ast[1], i+1)
            print_rec(ast[2], i+1)

    print_rec(ast, 0)


if __name__ == '__main__':
    string = input('>>> ')
    tokens = lex(string)
    seq = Seq(list(tokens))
    pprint(parse(seq))
