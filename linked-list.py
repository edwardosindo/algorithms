# def reversed_list( nodes ):


#     ################## Do not change anything below ####################
#     my_ll = MySpecialList(nodes)
#     head = my_ll.root
#     reversed_head = my_ll.reverseList(head)
#     return my_ll.print_as_list(reversed_head)
#     ################### Do not change anything above ###################

"""First Data Structure is the NOde class, which contain two elements, 
 which we will be passing in a data point or an element to be stored by this Node in the constructor 
 and by default it will be set into None"""
class Node:
    def __init__(self, data):
        self.value = data   #This is where we will be storing the past data point
        self.next = None    #This is where we will be storing the pointer to the next Node

""" 
    The next Data structure is the Linked list class, this is basically a wrapper that wraps over the nodes created above
    So the user is not never actually gonna interface with the Node class 
"""
class MySpecialList:
    def __init__(self, arr):
        # Given an array, initialize it into a Linked List
        # The head of the Linked List should be saved as self.head
        
        
        self.head = None
        # The head node shouldnt contain any data and not indexable, the user isnt gonna be able to acccess this head node. 
        # This is going to be used as a place holder to allow us to point to the first element in the list 
        # self.head = Node()

    ############################################## insert and append are same #############################################################################################################################################################
    """ 
        This function takes the root of a linked list and appends an item to the end of the Linked List.
        The function should return the head of the reversed Linked List.
    """
    def insert(self, root, item):
        """ Given the root/head of a Linked List, append the item to the end of the Linked List"""
        """ Function should return the root/head of the Linked List """

        # First check if root/head is None, if None append the item to the root Node
        if root is None:
            return Node(item)
        else:
            #create a variable to store the node that we are currently looking at(which is the root)
            current = root
            # Iterate over each one of the nodes in the list starting with the head
            # And once we get to a point where the next node of the current node is None, we know that is gonna be the last Node in the list, at which point we can insert our new node as the next node in the prior Node.
            while current.next != None:
                current = current.next
            current.next = Node(item)
        return root

    ################################################### Insert and append ends here ##########################################################################################################################################################

    ################################################### RevearseList Function ################################################################################################################################################################
    """
        This function takes the head of a Linked List and reverses it.
        The function should return the head of the reversed Linked List
    """
    def reverseList(self, head):
        prev = None
        # reversed_list_head = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    ################################################### End of RevearseList Function #################################################################################################################################################################
    
    ################################################### Start of print_as_list #######################################################################################################################################################################
    """
        This function takes the head of Linked List and converts it into a list while preserving the order of the Linked List.
        This function should return the list
    """
    def print_as_list(self, head):
        # Given the head of Linked List, this function will convert it to a list while preserving the order of the Linked List
        #Return the List
        linked_list_as_list = []
        node = head
        while node:
            linked_list_as_list.append(node.val)
            node = node.next
        return linked_list_as_list
    #################################################### End of print_as_list #########################################################################################################################################################################
