def react_length(str, skip_char=''):
    stack = []
    for char in str:
        if char.upper() == skip_char.upper():
            continue

        if len(stack) and cancel(stack[-1], char):
            stack.pop()
        else:
            stack.append(char)

    return len(stack)


def cancel(a, b):
    if is_upper(a):
        if a.lower() == b:
            return True
        return False
    if a.upper() == b:
        return True
    return False


def is_upper(a):
    if a.upper() == a:
        return True
    return False
