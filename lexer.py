import re

def lex(seq):
    l = len(seq)
    
    while l > 0:
        c = seq[0]
        next_position = 0

        if c == ' ':
            seq = seq[1:]
        
        elif re.match('[a-zA-Z]+', seq):
            match = re.match('[a-zA-Z]+', seq, re.M)
            yield ('symb', match.group(0))
            next_position = match.end()

        elif c in ('(', ')'):
            yield (c, '')
            next_position = 1
        
        elif re.match('->|et|ou', seq):
            yield ('binop', seq[0:3])
            next_position = 3

        elif re.match('non', seq):
            yield ('binop', seq[0:4])
            next_position = 4

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


