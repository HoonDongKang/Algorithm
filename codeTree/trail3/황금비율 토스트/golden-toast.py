n, m = map(int, input().split())
data = input()


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.END = Node(None)
        self.head = self.END
        self.tail = self.END

    def begin(self):
        return self.head

    def end(self):
        return self.tail

    def push_front(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def push_back(self, data):
        if self.begin() == self.end():
            self.push_front(data)
        else:
            new_node = Node(data)

            last = self.tail.prev

            new_node.prev = last
            new_node.next = self.tail

            last.next = new_node
            self.tail.prev = new_node

    def insert(self, node, data):
        if node == self.end():
            self.push_back(data)
        elif node == self.begin():
            self.push_front(data)
        else:
            new_node = Node(data)

            prev_node = node.prev

            new_node.prev = prev_node
            new_node.next = node

            prev_node.next = new_node
            node.prev = new_node

    def erase(self, node):
        next_node = node.next

        if node == self.begin():
            self.head = next_node
            next_node.prev = None
        else:
            prev_node = node.prev

            prev_node.next = next_node
            next_node.prev = prev_node

        node.prev = None
        node.next = None

        return next_node

    def get_result(self):
        result = []
        cur = self.head

        while cur != self.END:
            result.append(cur.data)
            cur = cur.next

        return ''.join(result)


ddl = DoublyLinkedList()

for char in data:
    ddl.push_back(char)

it = ddl.end()

for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'L':
        if it.prev is not None:
            it = it.prev

    elif cmd[0] == 'R':
        if it != ddl.end():
            it = it.next

    elif cmd[0] == 'P':
        ddl.insert(it, cmd[1])

    elif cmd[0] == 'D':
        if it != ddl.end():
            it = ddl.erase(it)

print(ddl.get_result())