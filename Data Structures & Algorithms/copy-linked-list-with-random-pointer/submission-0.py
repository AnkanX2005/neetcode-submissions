"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        originalToCopy = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            originalToCopy[curr] = copy
            curr = curr.next

        cur = head
        while cur:
            copy = originalToCopy[cur]
            copy.next = originalToCopy[cur.next]
            copy.random = originalToCopy[cur.random]
            cur = cur.next

        return originalToCopy[head]        