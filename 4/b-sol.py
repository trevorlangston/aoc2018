from helper import parse_file


def main():
    guard_data = parse_file()
    profiles = []

    for guard_id, events in guard_data.iteritems():
        profile = [0] * 60

        for event in events:
            start = event[0]
            end = event[1]
            for i in range(start, end):
                profile[i] += 1
            profiles.append((guard_id, profile))

    best_minute = None
    highest_freq = 0
    guard_id = None

    for profile in profiles:
        m = max(profile[1])
        if m > highest_freq:
            highest_freq = m
            best_minute = profile[1].index(m)
            guard_id = profile[0]

    return guard_id * best_minute


print main()
