N = int(input())


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Dll:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def push_front(self, data):
        new_node = Node(data)

        first = self.head.next

        new_node.prev = self.head
        new_node.next = first

        self.head.next = new_node
        first.prev = new_node

        self.length += 1

    def push_back(self, data):
        new_node = Node(data)

        last = self.tail.prev

        new_node.prev = last
        new_node.next = self.tail

        last.next = new_node
        self.tail.prev = new_node

        self.length += 1

    def pop_front(self):
        if self.length == 0:
            return None

        removed = self.head.next
        next_node = removed.next

        self.head.next = next_node
        next_node.prev = self.head

        self.length -= 1
        return removed.data

    def pop_back(self):
        if self.length == 0:
            return None

        removed = self.tail.prev
        prev_node = removed.prev

        self.tail.prev = prev_node
        prev_node.next = self.tail

        self.length -= 1
        return removed.data

    def size(self):
        return self.length

    def empty(self):
        return 1 if self.length == 0 else 0

    def front(self):
        return self.head.next.data

    def back(self):
        return self.tail.prev.data


dll = Dll()

for _ in range(N):
    line = input().split()
    cmd = line[0]

    if cmd == 'push_back':
        dll.push_back(line[1])
    elif cmd == 'push_front':
        dll.push_front(line[1])
    elif cmd == 'pop_front':
        print(dll.pop_front())
    elif cmd == 'pop_back':
        print(dll.pop_back())
    elif cmd == 'size':
        print(dll.size())
    elif cmd == 'empty':
        print(dll.empty())
    elif cmd == 'front':
        print(dll.front())
    elif cmd == 'back':
        print(dll.back())