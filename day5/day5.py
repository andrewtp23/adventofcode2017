def day5(text):
    steps = 0
    num_list = []
    with open(text) as f:
        for line in f:
            num_list.append(int(line))

    x = 0
    while x >= 0 and x < len(num_list):
        steps += 1
        old = x
        x += num_list[x]
        num_list[old] += 1
    print steps

def day5b(text):
    steps = 0
    num_list = []
    with open(text) as f:
        for line in f:
            num_list.append(int(line))

    x = 0
    while x >= 0 and x < len(num_list):
        steps += 1
        old = x
        x += num_list[x]
        if num_list[old] >= 3:
            num_list[old] -= 1
        else:
            num_list[old] += 1
    print steps

if __name__ == '__main__':
    day5('day5test')
    day5('day5input.txt')
    day5b('day5input.txt')