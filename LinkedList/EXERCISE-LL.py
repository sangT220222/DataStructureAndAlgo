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
        temp = self.head
        pre = self.head 
        #we use temp to check if next node that it's pointing to exists, where as pre is used t
        while temp.next:
        #this loop will keep going until temp points to nothing
            pre = temp 
            temp = temp.next 
        #at the end of this loop, expect temp to be the last item you want to pop, whereas pre is our new last item(second last item)
        
        self.tail = pre #hence we have set self.tail to be the new lat item - which was the second last item before
        self.tail.next = None
        self.length -= 1
        if self.length == 0: #here is where Scenario 2 happens - when one item is in the list
            self.tail = self.head = None

        return temp.value

    #function below adds at the beginning of the list
    def prepend(self,value):
        new_node = Node(value)
        #2 scenarios - where list is empty and list is not empty
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = None  
        else:
            new_node.next = self.head            
            self.head = new_node

        self.length += 1
        return True

    #popping the first item off the list
    def pop_first(self):
        #2 scenarios - list is empty and list is not
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None #always remember to make the popped item to point at None!
        self.length -= 1
        if self.length == 0:
            self.tail = None 

        return temp.value
    
    def get_value(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index): #underscore is used as we normally put i,j there before, but here we aren't using it
            temp = temp.next
        return temp.value

    def set_value(self, index, value):
        #check if index is in the length of linked list
        temp = self.get_value(index) #utilise the get method created 
        if temp: #if temp exists
            temp.value = value
            return True
        return False
 
my_linked_list = LinkedList(4)
my_linked_list.append(69)
my_linked_list.append(63)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


my_linked_list.print_LL()
my_linked_list.pop()
print('Length:', my_linked_list.length)
print('Tail:', my_linked_list.tail.value)
my_linked_list.print_LL()
my_linked_list.prepend(444)
              
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)                                                                 

my_linked_list.pop_first()
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)      