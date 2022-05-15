class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop()


class Queue:
    def __init__(self):
        self.queue = list()

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed

    def size(self):
        return len(self.queue)


class Node:  # информация об узле списка
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return ",".join(nodes)

    def append(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count



