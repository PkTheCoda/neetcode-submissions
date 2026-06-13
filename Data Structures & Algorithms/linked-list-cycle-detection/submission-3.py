# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# slow/fast pointer optimal solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next: #both fast and its next pointer have to exist or else you'll call .next on None
            slow = slow.next
            fast = fast.next.next
            
            if (fast == slow):
                return True
        
        return False
