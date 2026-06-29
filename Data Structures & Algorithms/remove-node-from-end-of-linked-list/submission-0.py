# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        index = len(arr) - n
        arr.pop(index)

        dummy = ListNode()
        tail = dummy

        for value in arr:
            tail.next = ListNode(value)
            tail = tail.next
        return dummy.next    
           

        
     
                       
            
        