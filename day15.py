def day15(a, b):
    count = 0
    pos = 0
    while pos < 40000000:
        a *= 16807
        b *= 48271
        a %= 2147483647
        b %= 2147483647
        mask = 0x0000FFFF
        a_m = a & mask
        b_m = b & mask
        if a_m == b_m:
            count += 1
        pos += 1
    print(count)

def day15b(a, b):
    count = 0
    pos = 0
    while pos < 5000000:
        a_notready = True
        b_notready = True
        while a_notready:
            a *= 16807
            a %= 2147483647
            if a % 4 == 0:
                a_notready = False
        while b_notready:
            b *= 48271
            b %= 2147483647
            if b % 8 == 0:
                b_notready = False

        mask = 0x0000FFFF
        a_m = a & mask
        b_m = b & mask
        if a_m == b_m:
            count += 1
        pos += 1
    print(count)

if __name__ == '__main__':
    #day15(512, 191)
    #day15b(65, 8921)
    day15b(512, 191)