class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        # 1. 전체 길이를 구한 후, 원하는 인덱스의 값을 가져오기
        # length = 1
        # cur = self.head
        
        # while cur.next is not None:
        #     cur = cur.next
        #     length += 1

        # print("length is", length)

        # end_length = length - k

        # cur = self.head

        # for i in range(end_length):
        #     cur = cur.next

        # return cur

        # 2. fast, slow를 이용하여 한칸씩 노드 이동하기
        # fast는 slow 보다 인덱스 k번 앞서고, fast가 끝에 도달하면 slow는 끝에서 k 번재 값
        fast = self.head
        slow = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!