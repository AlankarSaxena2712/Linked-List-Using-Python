# Printing the ((n/2) + 1)th node in this program

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

    def middle_of_list(self):
        temp = self.head
        prev = self.head

        if temp is None:
            print("Linked List doesn't exist")
            return
        else:
            while temp is not None and temp.next is not None:
                prev = prev.next
                temp = temp.next.next
        
        print(prev.data)
    
    def printlist(self):
        temp = self.head

        while(temp is not None):
            print(temp.data, end= " ")
            temp = temp.next

    
if __name__ == "__main__":
    llist = LinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.insert(6)
    llist.insert(7)

    llist.printlist()
    print()
    llist.middle_of_list()
