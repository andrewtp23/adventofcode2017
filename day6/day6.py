input = '0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'
test = '0	2	7	0'

def day6(input):
    array = map(int, input.split('	'))
    cycles = 0
    pattern = set()
    pattern_instance = tuple(array)
    while pattern_instance not in pattern:
        pattern.add(pattern_instance)
        max_val = max(array)
        x = array.index(max_val)
        array[x] = 0
        while max_val > 0:
            x = (x + 1) % len(array)
            array[x] += 1
            max_val -= 1
        pattern_instance = tuple(array)
        cycles += 1
    print cycles

def day6b(input):
    array = map(int, input.split('	'))
    cycles = 0
    pattern = set()
    pattern_instance = tuple(array)
    is_looped = False
    repeated_instance = 0
    while True:
        if is_looped:
            cycles += 1
        if pattern_instance == repeated_instance:
                break
        if not is_looped and pattern_instance in pattern:
                is_looped = True
                repeated_instance = pattern_instance

        pattern.add(pattern_instance)
        max_val = max(array)
        x = array.index(max_val)
        array[x] = 0
        while max_val > 0:
            x = (x + 1) % len(array)
            array[x] += 1
            max_val -= 1
        pattern_instance = tuple(array)
    print cycles

if __name__ == '__main__':
    day6(test)
    day6(input)
    day6b(test)
    day6b(input)