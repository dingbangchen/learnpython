# def isOdd(n):
#     return n%2 == 1
# lista = filter(isOdd,[1,2,3,4,5,6])
# print(list(lista))


from msilib.schema import Error


class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()    # we call the node function to create a head node which has no value but a pointer to none
                              # the linked list right now has length or zero because there is no data in it

    def append(self,data):
        new_node = node(data)  #this created a node with data and point to None
        cur = self.head   # this is the header because we need to start from the head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!= None:
            total += 1      # we need to increment first and then step to next one
            cur = cur.next
        return total

    def display(self):
        elms = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elms.append(cur_node.data)
        print(elms)

    def get(self,index):
        if index >= self.length():
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next # we need to start from the first data node than the header node
            if cur_index == index:      #check the if the index is the one that we are looking for
                return cur_node.data    #if it is return the data of the node
            cur_index+=1                #if not then keep traverse to the next node's index

    def erase(self,index):
        if index >= self.length():
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1
        


my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.display()
print(my_list.get(1))
my_list.erase(1)
my_list.display()
