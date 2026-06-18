# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)

            if not kth:
                break
            
            groupAfter = kth.next

            prev = None
            curr = groupPrev.next

            while curr != groupAfter:
                cnext = curr.next
                curr.next = prev
                prev = curr
                curr = cnext
            
            new_head = groupPrev.next
            new_head.next = curr
            groupPrev.next = prev
            groupPrev = new_head
        
        return dummy.next

    def getKth(self, node: ListNode, k):

        new = node
        for i in range(k):
            if new.next:
                new = new.next
            else:
                return None
        
        return new
        
        