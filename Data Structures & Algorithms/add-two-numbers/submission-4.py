# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # cleaned up w/o bloat
        carry = 0
        to_return = []

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            carried = val // 10
            staying = val % 10
            carry = carried
            to_return.append(staying)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            
        
        if carry != 0:
            to_return.append(carry)
        
        dummy = ListNode(1000)
        curr = dummy
        for i in range(len(to_return)):
            curr.next = ListNode(to_return[i])
            curr = curr.next
        
        return dummy.next
        