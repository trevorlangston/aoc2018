def main():
    file = open('input', 'r')
    sum = 0

    for line in file:
        num = int(line[1:])
        if line[0] == '+':
            sum += num
        else:
            sum -= num

    return sum


print main()
