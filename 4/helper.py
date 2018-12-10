import re


def parse_file():
    file = open('input', 'r')
    events = []

    for line in file:
        events.append(line)

    events.sort()

    guard_data = {}
    current_guard = None

    for i in range(len(events)):
        event = events[i]
        if "Guard" in event:
            m = re.search("#(\d+)", event)
            current_guard = int(m.groups()[0])
            continue

        if "wakes" in event:
            falls_asleep = int(get_minute(events[i-1]))
            wakes_up = int(get_minute(event))
            pair = (falls_asleep, wakes_up)

            if current_guard in guard_data:
                guard_data[current_guard].append(pair)
            else:
                guard_data[current_guard] = [pair]

    return guard_data


def get_minute(event):
    m = re.search(":(\d+)", event)
    return m.groups()[0]
