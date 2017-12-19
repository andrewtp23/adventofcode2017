from pprint import pprint

def day19(input):
    pos = [0, input[0].index('|')]
    word = []
    direction = [1,0]
    steps = 0
    while True:
        ch = input[pos[0]][pos[1]]

        if ch == '|' or ch == '-':
            pos[0] += direction[0]
            pos[1] += direction[1]
        elif ch == '+':
            c = [1 - abs(direction[0]), 1 - abs(direction[1])]

            if input[pos[0] + c[0]][pos[1] + c[1]] != ' ':
                pos[0] += c[0]
                pos[1] += c[1]
                direction = c
            elif input[pos[0] - c[0]][pos[1] - c[1]] != ' ':
                pos[0] -= c[0]
                pos[1] -= c[1]
                direction = [-c[0], -c[1]]
        elif ch == ' ':
            break
        else:
            pos[0] += direction[0]
            pos[1] += direction[1]
            word.append(ch)
        steps += 1
    print(''.join(word))
    print(steps)


if __name__ == '__main__':
    test = 'day19test.txt'
    test = 'day19.txt'
    with open(test) as f:
        map = list(map(list, f.readlines()))
        day19(map)