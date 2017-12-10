from collections import Counter

def day4(text):
    f = open(text)
    correct = 0
    line = f.readline()
    words = line.split()
    l = 0
    for x in words:
        current = x
        for g in words:
            if g == current:
                l +=1
    if l == len(words):
        correct += 1
    print correct
    while line:
        line = f.readline()
        words = line.split()
        l = 0
        for x in words:
            current = x
            for g in words:
                if g == current:
                    l += 1
        if l == len(words):
            correct += 1
    print('test')
    correct -= 1 # offset final read
    print correct

    f.close()

def is_anagram(input1, input2):
    return Counter(input1) == Counter(input2)

def day4b(text):
    f = open(text)
    correct = 0
    line = f.readline()
    words = line.split()
    l = 0
    for x in words:
        current = x
        for g in words:
            if is_anagram(g, current):
                l +=1
    if l == len(words):
        correct += 1
    print correct
    while line:
        line = f.readline()
        words = line.split()
        l = 0
        for x in words:
            current = x
            for g in words:
                if is_anagram(g, current):
                    l += 1
        if l == len(words):
            correct += 1
    print('test')
    correct -= 1 # offset final read
    print correct

    f.close()


if __name__ == '__main__':
    day4('day4input')
