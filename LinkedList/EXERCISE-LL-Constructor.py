class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #this class will create a node and will be called when creating a Linked List
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    def __init__(self,value):
        new_node = Node(value)
        #in a linked list, we need head and a tail so that they point to a node
        self.head = new_node
        self.tail = new_node
        self.length = 1

        # def append(self,value):


        # def prepend(self,value):


        # def insert(self,index,value):




 
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    