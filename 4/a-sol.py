from helper import parse_file


def main():
    guard_data = parse_file()

    sleepiest = None
    best_minute = None
    most_hours_slept = 0

    for guard_id, events in guard_data.iteritems():
        profile = [0] * 60
        slept = 0

        for event in events:
            start = event[0]
            end = event[1]
            slept += end - start
            for i in range(start, end):
                profile[i] += 1

        if slept > most_hours_slept:
            sleepiest = guard_id
            most_hours_slept = slept
            best_minute = profile.index(max(profile))

    return sleepiest * best_minute


print main()
