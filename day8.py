import collections
operators = {'<' : '__lt__',
             '>' : '__gt__',
             '>=' : '__ge__',
             '<=' : '__le__',
             '!=' : '__ne__',
             '==' : '__eq__'}

register = collections.defaultdict(int)
maxv = 0

def day8(input):
    r1, computation, v1, i, r2, op, v2 = input.split()
    if computation == 'inc':
        comp = '__add__'
    else:
        comp = '__sub__'

    v1 = int(v1)
    v2 = int(v2)

    if getattr(register[r2], operators[op])(v2):
        value = getattr(register[r1], comp)(v1)
        global maxv
        if value > maxv:
            maxv = value

        register[r1] = value


if __name__ == "__main__":
    with open('day8.txt') as f:
        lines = f.readlines()
        for x in lines:
            day8(x)
        all = [(v, k) for k, v in register.items()]
        print(max(all))
        print(maxv)