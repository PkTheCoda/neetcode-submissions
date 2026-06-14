# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode()
        prev_original = prev
        prev.next = head

        ending = head

        # move ending forward n times
        for i in range(n):
            ending = ending.next
        
        # take ending to end, move target
        while ending:
            prev = prev.next
            ending = ending.next
        
        #prev now sits on element behind target
        target = prev.next
        prev.next = target.next
        target.next = None

        return prev_original.next
        


        