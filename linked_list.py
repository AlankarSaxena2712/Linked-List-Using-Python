# Create a Node
class Node:
    # Function to initialize Node data
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a Linked List
class LinkedList:
    # Function to initilaize the head of linked list
    def __init__(self):
        self.head = None

    # function to print the Linked List from the head
    def printlist(self):
        temp = self.head

        # looping thorugh the Linked List
        while(temp is not None):
            print(temp.data)
            temp = temp.next

    # Function to insert the node at the beginning of the linked list
    def at_beginning(self, data):
        temp = self.head

        # if node is empty
        if temp is None:
            NewNode = Node(data)
            NewNode.next = self.head
        
        # if node already has some nodes previously
        else:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode


# Main method
if __name__ == '__main__':
    
    # created empty linked list
    llist = LinkedList()

    # created three nodes as head, second and third
    llist.head = Node('Mon')
    second = Node('Tue')
    third = Node('Wed')

    # Linking of the nodes
    llist.head.next = second
    second.next = third

    # Inserting at the Beginning of the Linked List
    llist.at_beginning("WEB")
    llist.at_beginning("WES")

    # printing the Linked List
    llist.printlist()
