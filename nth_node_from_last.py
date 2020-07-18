class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        temp = self.head
        if temp is None:
            NewNode = Node(data)
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode

    def print_nth_node(self, n):
        temp = self.head
        prev = self.head
        if self.head is None:
            print("Linked List doesn't exist")
            return
        for _ in range(n):
            if temp is not None:
                temp = temp.next
            else:
                print("Enough nodes are not present in the Linked List")
                return
        while temp is not None:
            prev = prev.next
            temp = temp.next

        print(prev.data)

    def printlist(self):
        temp = self.head

        # looping thorugh the Linked List
        while(temp is not None):
            print(temp.data, end= " ")
            temp = temp.next

    
if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(0)
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.insert(6)

    llist.print_nth_node(4)
    llist.printlist()
