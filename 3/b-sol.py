# this really should be done using a sweep line algorithm
def main():
    file = open('input', 'r')
    grid = [0] * 1000 * 1000
    claims = []

    for line in file:
        claims.append(line)
        id, start_col, start_row, width, height = parse_claim(line)
        for w in range(width):
            for h in range(height):
                idx = get_idx(start_col, start_row, w, h)
                grid[idx] += 1

    for claim in claims:
        id, start_col, start_row, width, height = parse_claim(claim)
        no_overlap = True
        for w in range(width):
            for h in range(height):
                idx = get_idx(start_col, start_row, w, h)
                if grid[idx] > 1:
                    no_overlap = False
        if no_overlap is True:
            return id


def get_idx(start_col, start_row, w, h):
    col = start_col + w
    row = start_row + h
    return row * 1000 + col


def parse_claim(line):
    claim_id, _, origin, size = line.split(' ')
    x0, y0 = [int(x) for x in origin[:-1].split(',')]
    l1, l2 = [int(x) for x in size.split('x')]
    return int(claim_id[1:]), x0, y0, l1, l2


print main()
