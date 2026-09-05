# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        second = slow.next
        slow.next = None
        curr = second
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        first, second = head, prev

        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

        return

        


                

