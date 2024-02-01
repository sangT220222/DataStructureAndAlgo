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

    def print_LL(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        self.length += 1
        return True
    
    def pop(self):
        #for pop we need to consider 3 scenarios
        #1. when list is empty
        if self.length == 0:
            return None #no point as no items to pop out
        #2. when lenght of list is 1
        #3. when list is more than 1
        #we want 2 temp nodes that will store values of the items in linked list and keep track which is which
        #this where pre and temp will be effective


    # def prepend(self,value):


        # def insert(self,index,value):




 
my_linked_list = LinkedList(4)
my_linked_list.append(69)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


my_linked_list.print_LL()

                                                                                                                    