class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def remove_at(self, index):
        if index < 0 or index > self.length() - 1:
            raise Exception("Invalid index provided")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_values):
        self.head = None
        for data in data_values:
            self.insert_at_end(data)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += f'{itr.data} ---> '
            itr = itr.next
        print(llstr)


l1 = Linked_list()
l1.insert_values([1, 2, 3, 4, 5, 6])
l1.print()
print(f'Size of the linked list --> {l1.length()}')
