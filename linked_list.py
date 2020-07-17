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
    def insert_at_beginning(self, data):

        # Getting the address of the first node
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


    # Function to insert the node at the end of the Linked List
    def insert_at_end(self, data):

        # Getting the address of the first node
        temp = self.head

        # If the Linked lIst is empty
        if temp is None:
            NewNode = Node(data)
            self.head = NewNode

        # If the Linked List has some nodes previously
        else:

            # Looping through the Linked List, to the LAST Node
            while temp.next is not None:
                temp = temp.next
            # here we reached the last node after the loop ends
            
            # inserting the node at the end
            NewNode = Node(data)
            temp.next = NewNode


    # Function to insert the node after a node(number of the node)
    def insert_after(self, data, after_node):

        # Getting the address of the first node
        temp = self.head

        # If the Linked List is Empty
        if temp is None:
            print("Node couldn't be inserted using this as the Linked List is Empty.")
            return

        # If the Linked List has some Node previously
        else:
            count = 0

            # reaching the specific node
            while count < after_node - 2:
                temp = temp.next

                # Condition to check if the Position Provided is Greater than the length of the Linked List
                # than it will insert at the end of the Linked List
                if temp.next == None:
                    break
                count = count + 1

            # inserting the node at the specific position
            NewNode = Node(data)
            NewNode.next = temp.next
            temp.next = NewNode



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
    llist.insert_at_beginning("WEB")
    llist.insert_at_beginning("WES")

    # Inserting at the End of the Linked List
    llist.insert_at_end("DES")

    # Inserting at a Specific Position in the Linked List
    llist.insert_after("res", 4)
    llist.insert_after("HELLO", 6)
    llist.insert_after("HEL", 10)

    # printing the Linked List
    llist.printlist()
