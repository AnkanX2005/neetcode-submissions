# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # arr = []
        # curr = head
        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next

        # index = len(arr) - n
        # arr.pop(index)

        # dummy = ListNode()
        # tail = dummy

        # for value in arr:
        #     tail.next = ListNode(value)
        #     tail = tail.next
        # return dummy.next    
           

        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        reverse_head = prev
        dummy = ListNode()
        dummy.next = reverse_head

        prev = dummy
        curr = reverse_head
        count = 1

        while curr is not None:
            if count == n:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            count += 1

        head = dummy.next
        new_head = None
        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next
        return new_head                      

        
     
                       
            
        