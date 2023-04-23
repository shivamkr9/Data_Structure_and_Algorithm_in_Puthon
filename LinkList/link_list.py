class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begning(self, data):
        node = Node(data, self.head)
        self.head = node

    def printList(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llist = ""
        while itr:
            llist += str(itr.data) + "-->"
            itr = itr.next

        print(llist)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def length_of_ll(self):
        count = 0
        if self.head is None:
            print("Linked list is empty", count)
            return

        itr = self.head
        while itr:
            itr = itr.next
            count += 1

        return count

    def remove_at(self, index):
        if index<0 or index>self.length_of_ll():
            raise Exception("Invalid index.")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        length = self.length_of_ll()
        if index < 0 or index > length:
            raise Exception("Invalid index.")

        if index == 0:
            self.insert_at_begning(data)
            return

        if index == length:
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next
            count += 1

def main():
    datalist = ([1,2,3,4,5,6,7,8,9])
    ll = LinkedList()
    # ll.insert_at_end(77)
    # ll.insert_at_begning(5)
    # ll.insert_at_begning(89)
    # ll.insert_at_begning(7)
    ll.insert_values(datalist)
    ll.printList()
    length = ll.length_of_ll()
    print(length)
    ll.remove_at(2)
    # ll.remove_at(20)
    ll.insert_at(0, 5)
    ll.printList()
    ll.insert_at(9, 101)
    ll.printList()
    ll.insert_at(4, 202)
    ll.printList()


if __name__ == "__main__":
    main()