from helper import parse_file
from collections import Counter


def main():
    guard_data = parse_file()
    profile = [[] for _ in range(60)]

    for guard_id, events in guard_data.iteritems():
        for event in events:
            start = event[0]
            end = event[1]
            for i in range(start, end):
                profile[i].append(guard_id)

    best_minute = None
    highest_freq = 0

    for minute in range(len(profile)):
        guards = profile[minute]
        if len(guards) > highest_freq:
            best_minute = minute + 1
            highest_freq = len(guards)

    c = Counter(profile[best_minute])
    guard_id = c.most_common(1)[0][0]

    return guard_id * best_minute


print main()
