def main():
    file = open('input', 'r')
    ids = []

    for line in file:
        ids.append(line)

    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            id_a, id_b = ids[i], ids[j]
            dist = 0
            common = ''
            for k in range(len(id_a)):
                if id_a[k] == id_b[k]:
                    common += id_a[k]
                else:
                    dist += 1
            if dist == 1:
                return common

    return None


print main()
