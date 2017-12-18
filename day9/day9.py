score = 0
secondary_score = 0

def day9(input):
    global score
    global secondary_score
    ignore = False
    bracket_flag = False
    bracket = 0
    x = 0
    while x < len(input):
        if input[x] == '>' and ignore:
            ignore = False
        elif input[x] == '!' and ignore:
            x += 1
        elif ignore:
            secondary_score += 1
            pass
        elif input[x] == '{':
            bracket += 1
        elif input[x] == '}':
            score += bracket
            bracket -= 1
        elif input[x] == '!':
            secondary_score += 1
            pass
        elif input[x] == '<':
            ignore = True
        else:
            pass
        x += 1


if __name__ == "__main__":
    test = 'day9test.txt'
    input = 'day9.txt'
    with open(input) as f:
        lines = f.read().replace('\n', '')
        day9(lines)
        print(score)
        print(secondary_score)