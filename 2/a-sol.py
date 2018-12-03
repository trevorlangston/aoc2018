def main():
    file = open('input', 'r')
    count_2 = 0
    count_3 = 0

    for line in file:
        d = {}
        for char in line:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        if 2 in d.values():
            count_2 += 1
        if 3 in d.values():
            count_3 += 1

    return count_2 * count_3


print main()
