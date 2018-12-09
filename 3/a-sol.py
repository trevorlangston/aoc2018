# this really should be done using a sweep line algorithm
def main():
    file = open('input', 'r')
    ans = 0
    grid = [0] * 1000 * 1000

    for line in file:
        _, start_col, start_row, width, height = parse_line(line)
        for w in range(width):
            for h in range(height):
                col = start_col + w
                row = start_row + h
                idx = row * 1000 + col
                grid[idx] += 1
                if grid[idx] == 2:
                    ans += 1

    return ans


def parse_line(line):
    claim_id, _, origin, size = line.split(' ')
    x0, y0 = [int(x) for x in origin[:-1].split(',')]
    l1, l2 = [int(x) for x in size.split('x')]
    return int(claim_id[1:]), x0, y0, l1, l2


print main()
