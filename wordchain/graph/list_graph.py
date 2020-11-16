class Node:
    def __init__(self, item=None, link=None):
        self.item = item
        self.link = link


class LinkedList:
    def __init__(self, index=0):
        self.size = 0
        self.head = None
        self.tale = None
        self.index = index

    def size(self):
        return self.size

    def add(self, item):
        if self.tale is not None:
            self.tale.link = Node(item)
            self.tale = self.tale.link
        else:
            self.head = Node(item)
            self.tale = self.head
        self.size += 1
        return self


a = LinkedList(0)
b = LinkedList(1)
c = LinkedList(2)
d = LinkedList(3)
e = LinkedList(4)

a.add(1)
b.add(0).add(2).add(4)
c.add(1).add(3).add(4)
d.add(2).add(4)
e.add(1).add(2).add(3)

graph = [a, b, c, d, e]

for v in graph:
    e = v.head
    print(v.index, end=': ')
    while e is not None:
        print(e.item, end=', ')
        e = e.link
    print()

