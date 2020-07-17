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
    def insert_at_pos(self, data, pos):

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
            while count < pos - 2:
                temp = temp.next

                # Condition to check if the Position Provided is Greater than the length of the Linked List
                # than it will insert at the end of the Linked List
                if temp.next == None:
                    print("Sorry! this location doesn't exist. So we are inserting it at the END of the Linked List")
                    break
                count = count + 1

            # inserting the node at the specific position
            NewNode = Node(data)
            NewNode.next = temp.next
            temp.next = NewNode


    # Function to insert a node after the specific data
    def insert_after(self, data, after_data):
        
        # Initializing the head of the Linked List
        temp = self.head

        # Checking if the Linked List is empty
        if temp is None:
            print("The node can't be inserted in this case as the Linked List is empty!")
            return
        
        # If the Linked List is not empty
        else:
            # Looping through the Linked List until the after_data is found
            while temp.data != after_data:
                temp = temp.next

            # Checking if the data is not found in the Linked List after which we have to insert the node
            if temp is None:
                print("The node cannot be inserted as the data you said after was not present in the Linked List")
                return
            
            # Inserting the new node after the data which was passed
            NewNode = Node(data)
            NewNode.next = temp.next
            temp.next = NewNode


    # Function to delete the node at the Beginning of the Linked List
    def delete_at_beginning(self):
        # Initializing the head of the Linked List
        temp = self.head

        # Checking if the Linked List is empty or not
        if temp is None:
            print("Sorry! The deletion couldn't be preformed as the Linked List is empty")
            return
        # If the Linked List is not empty
        else:
            # Incrementing the head of the Linked List to the second node of the Linked List
            self.head = temp.next
            # Freeing the memory of the first node of the Linked List
            temp = None


    # Function to delete the node at the end of the Linked List
    def delete_at_end(self):
        # Initializing the head of the Linked List
        temp = self.head
        # Setting a new pointer as None, to not misplace the address of the node
        prev = None

        # Checking if the Linked List is empty or not
        if temp is None:
            print("Sorry! The deletion couldn't be preformed as the Linked List is empty")
            return
        # If the Linked List is not empty
        else:
            # Looping through the Linked List to the last Node
            while temp.next != None:
                # storing the address of the previous node of the temp node
                prev = temp
                # incrementing the temp
                temp = temp.next
        
        # Linking the Previous Node of the node to be deleted to the next node of the deleted node
        prev.next = temp.next
        # Defining the node to be deleted as None, to free its space
        temp = None


    # Function to delete the node at a particular position
    def delete_at_pos(self, pos):
        # Initializing the head of the Linked List
        temp = self.head
        # Setting a new pointer as None, to not misplace the address of the node
        prev = None

        # Checking if the Linked List is empty or not
        if temp is None:
            print("Sorry! The deletion couldn't be preformed as the Linked List is empty")
            return
        # If the Linked List is not empty
        else:
            # Initializing the count variable
            count = 0
            # Looping through the Linked List to the specific position
            while count < pos - 1:
                # storing the address of the previous node of the temp node
                prev = temp
                # incrementing the temp
                temp = temp.next
                # incrementing the count variable
                count = count + 1
        
        # Linking the Previous Node of the node to be deleted to the next node of the deleted node
        prev.next = temp.next
        # Defining the node to be deleted as None, to free its space
        temp = None



    # Function to delete a node
    def delete_node(self, data):

        # Getting the address of the head
        temp = self.head

        # Setting a new pointer as None, to not misplace the address of the node
        prev = None

        # Check if the Linked List is empty
        if temp is None:
            print("Node cannot be deleted as the Linked List is empty")
            return

        # If the data is found at the first node i.e., head of the Linked List
        if temp.data == data:
            # Initilaizing the new head of the Linked List
            self.head = temp.next
            return
        
        # Looping through the Linked List to find the data to be deleted
        while ((temp != None) and (temp.data != data)):
            # storing the address of the previous node of the temp node
            prev = temp
            # incrementing the temp
            temp = temp.next

        # If the data to be deleted isn't in the Linked List
        if temp is None:
            print("The data you want to delete does not exist")
            return

        # Linking the Previous Node of the node to be deleted to the next node of the deleted node
        prev.next = temp.next
        # Defining the node to be deleted as None, to free its space
        temp = None



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
    llist.insert_at_pos("res", 4)
    llist.insert_at_pos("HELLO", 6)
    llist.insert_at_pos("HEL", 10)

    # Deleting the node which contains the data passed into the function
    llist.delete_node("Tue")

    # Deleting the node at the Beginning of the Linked List
    llist.delete_at_beginning()

    # Deleting the node at the end of the Linked List
    llist.delete_at_end()

    # Deleting the node at any specific position in the Linked List provided in the function
    llist.delete_at_pos(6)

    # printing the Linked List
    llist.printlist()
