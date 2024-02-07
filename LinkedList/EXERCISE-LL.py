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

        return temp

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

        return temp
    
    def get_value(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index): #underscore is used as we normally put i,j there before, but here we aren't using it
            temp = temp.next
        return temp

    def set_value(self, index, value):
        #check if index is in the length of linked list
        if index < 0 or index > self.length:
            return False
        temp = self.get_value(index) #utilise the get method created 
        temp.value = value
        return True
       
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        #as we will  be inserting a new value in the desired index, we want to get temp to be the item before the desired index
        temp = self.get_value(index - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        #scenario where index is not existent in the list
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        prev = self.get_value(index - 1)
        temp = prev.next #reason why we dind't use self.get_value as it's O(n), where as this is O(1)

        prev.next = temp.next
        temp.next = None #point this to nowhere as this node has been removed
        self.length -= 1

        return temp
    
    def reverse(self):
        #first thing we want to do is swap head and tail together
        temp = self.head
        self.head = self.tail
        self.tail = temp

        #we have 2 variables that will keep track of the before and after variable to make reverse easier
        after = temp.next
        before = None #this is None so that the initial head will point to this whilst we iterate through the list

        for _ in range(self.length):
            after = temp.next #this will apply once it's done with 1st iteration
            temp.next = before #beginning of the reversal process
            before = temp #this moves along the list, so before will move to the next node which is temp
            temp = after #temp will then be the next node, which is after

    def middle_node(self):
        #wil have 2 pointers -> slow pointer moves 1 node at a time, fast pointer moves 2 nodes at a time
        slow = fast = self.head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next #this will make fast move 2 nodes 
        return slow
    
    def has_loop(self): #method is to see if the linked list has a cycle or not
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True #cycle is found
        return False
    def partition_list(self,x):
        if not self.head:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head

        while current:
            if current.value < x:
                prev1.next = current
                prev1 = prev1.next
            else:
                prev2.next = current
                prev2 = prev2.next
            
            current = current.next #we will increment till current is None
        #setting the end of sub lists to None
        prev1.next = None
        prev2.next = None 
        #beginning of the merge of two sublists
        prev1.next = dummy2.next 
        self.head = dummy1.next

    def remove_duplicates(self):
        values = set() #sets only contain unique values
        prev = None
        curr = self.head

        while curr:
            if curr.value in values:
                prev.next = curr.next
                self.length -= 1
            else:
                prev = curr
                values.add(curr.value)
            curr = curr.next

    def binary_to_decimal(self):
        sum = 0
        power = self.length - 1
        curr = self.head
        
        while curr:
            sum += curr.value * (2**power)
            power -= 1
            curr = curr.next
        return sum
    
    def reverse_between(self, m, n):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for _ in range(m):
            prev = prev.next

        curr = prev.next

        for _ in range(n-m):
            node_move = curr.next
            curr.next = node_move.next
            node_move.next = prev.next
            prev.next = node_move
            
        self.head = dummy.next
    

def find_kth_from_end(list_name, index):
    slow = fast = list_name.head #as it's not in the LinkedList class
    for _ in range(index):
        if fast is None:
            return None #this means fast pointer is out of index
        fast = fast.next #here we are setting fast pointer k steps ahead

    while fast and fast.next: #this will keep loop until fast and fast.next is not None
        slow = slow.next
        fast = fast.next
    return slow.value



# my_linked_list = LinkedList(4)
# my_linked_list.append(69)
# my_linked_list.append(63)

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)


# my_linked_list.print_LL()
# my_linked_list.pop()
# print('Length:', my_linked_list.length)
# print('Tail:', my_linked_list.tail.value)
# my_linked_list.print_LL()
# my_linked_list.prepend(444)
              
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)                                                                 

# my_linked_list.pop_first()
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)      

# print(my_linked_list.get_value(1))
# print(my_linked_list.set_value(1,69))
# my_linked_list.insert(2,63)
# my_linked_list.print_LL()

# my_linked_list.remove(1)

# my_linked_list.print_LL()
# my_linked_list.reverse()
# my_linked_list.print_LL()

# print(find_kth_from_end(my_linked_list, 2))

# ll = LinkedList(3)
# ll.append(5)
# ll.append(8)
# ll.append(10)
# ll.append(2)
# ll.append(1)

# print("LL before partition_list:")
# ll.print_LL() # Output: 3 5 8 10 2 1

# ll.partition_list(5)

# print("LL after partition_list:")
# ll.print_LL() # Output: 3 2 1 5 8 10

# Test case 1: Binary number 110 = Decimal number 6
# linked_list = LinkedList(1)
# linked_list.append(1)
# linked_list.append(0)
# result = linked_list.binary_to_decimal()
# try:
#     assert result == 6
#     print("Test case 1 passed, returned: ", result)
# except AssertionError:
#     print("Test case 1 failed, returned: ", result)

# # Test case 2: Binary number 1000 = Decimal number 8
# linked_list = LinkedList(1)
# linked_list.append(0)
# linked_list.append(0)
# linked_list.append(0)
# result = linked_list.binary_to_decimal()
# try:
#     assert result == 8
#     print("Test case 2 passed, returned: ", result)
# except AssertionError:
#     print("Test case 2 failed, returned: ", result)

# # Test case 3: Binary number 0 = Decimal number 0
# linked_list = LinkedList(0)
# result = linked_list.binary_to_decimal()
# try:
#     assert result == 0
#     print("Test case 3 passed, returned: ", result)
# except AssertionError:
#     print("Test case 3 failed, returned: ", result)

# # Test case 4: Binary number 1 = Decimal number 1
# linked_list = LinkedList(1)
# result = linked_list.binary_to_decimal()
# try:
#     assert result == 1
#     print("Test case 4 passed, returned: ", result)
# except AssertionError:
#     print("Test case 4 failed, returned: ", result)

# # Test case 5: Binary number 1101 = Decimal number 13
# linked_list = LinkedList(1)
# linked_list.append(1)
# linked_list.append(0)
# linked_list.append(1)
# result = linked_list.binary_to_decimal()
# try:
#     assert result == 13
#     print("Test case 5 passed, returned: ", result)
# except AssertionError:
#     print("Test case 5 failed, returned: ", result)


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_LL()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_LL()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_LL()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_LL()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_LL()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
