class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def values(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

    def contain(self, value):
        for v in self.values():
            if v == value:
                return True
        return False


def union(llist_1, llist_2):
    if llist_1.size() == 0:
        return llist_2
    elif llist_2.size() == 0:
        return llist_1

    union_llist = LinkedList()

    for value in llist_1.values():
        if not union_llist.contain(value):
            union_llist.append(value)

    for value in llist_2.values():
        if not union_llist.contain(value):
            union_llist.append(value)
    if union_llist.size() != 0:
        return union_llist


def intersection(llist_1, llist_2):
    intersection_llist = LinkedList()
    if llist_1.size() == 0 or llist_2 == 0:
        return intersection_llist

    for value in llist_1.values():
        if llist_2.contain(value) and not intersection_llist.contain(value):
            intersection_llist.append(value)

    if intersection_llist.size() != 0:
        return intersection_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2
print('-' * 30)
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_4 = [1, 7, 8, 9, 11, 21, 1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Test case 3
print('-' * 30)
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [None, 2, 3, 4]
element_6 = [1, 2, 3, 5, 7, 9]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))

# Edge case test when one of the linklist is empty
print('-' * 30)
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
element_7 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]

for i in element_7:
    linked_list_7.append(i)

print(union(linked_list_7, linked_list_8))
print(intersection(linked_list_7, linked_list_8))
