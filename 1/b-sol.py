class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        node = Node(data, self.head)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next


def main():
    file = open('input', 'r')
    ll = CircularLinkedList()

    # build list
    for line in file:
        num = int(line[1:])
        if line[0] == '-':
            num *= -1
        ll.add(num)

    freq_seen = {}
    freq = 0
    node = ll.head

    while True:
        if freq in freq_seen:
            return freq
        else:
            freq_seen[freq] = None

        num = node.data
        freq += num
        node = node.next


print main()
