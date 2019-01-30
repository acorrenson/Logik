import re

def lex(seq):
    l = len(seq)
    
    while l > 0:
        c = seq[0]
        next_position = 0

        if c == ' ':
            seq = seq[1:]
        
        elif c in ('0', '1'):
            yield ('value', c)
            seq = seq[1:]

        elif re.match('->|et|ou', seq):
            yield ('binop', seq[0:2])
            next_position = 2

        elif re.match('non', seq):
            yield ('unop', seq[0:4])
            next_position = 4

        elif re.match('[a-zA-Z]+', seq):
            match = re.match('[a-zA-Z]+', seq, re.M)
            yield ('symb', match.group(0))
            next_position = match.end()

        elif c in ('(', ')'):
            yield (c, '')
            next_position = 1

        else:
            print('errror')
            break
        
        seq = seq[next_position:]
        l = len(seq)


def pprint(token):
    print('\033[31m'
        + token[0]
        + "\033[0m"
        + (6 - len(token[0]))*" " + ":",
        end=" "
    )
    print(token[1])


if __name__ == '__main__':
    seq = input('>>> ')
    for i, tokens in enumerate(lex(seq)):
        print(i+1, end=" ")
        pprint(tokens)


