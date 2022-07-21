    # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #在现有链表前先定义一个空节点
        dummy = ListNode(-1)
        dummy.next = head
#这个dummy节点作为返回的空头节点不需要更新，但是我们需要一个节点来进入循环    
        prev_node = dummy

        while head and head.next:
            first_node = head
            second_node = head.next
            
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            prev_node = first_node
            head= first_node.next
            
        return dummy.next


##主要知识点：The head node in the linkedlist can be viewed as the first node. 
#           If the first node in the linkedlist is empty, we call it a null head node