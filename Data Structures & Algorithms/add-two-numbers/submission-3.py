# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        to_return = []

        # 23 + 98
        # 3 2
        # 9 8

        while l1 or l2:

            if l1 and l2:
                val = l1.val + l2.val + carry
                carried = val // 10
                staying = val % 10
                to_return.append(staying)
                carry = carried
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                val = l1.val + carry
                carried = val // 10
                staying = val % 10
                to_return.append(staying)
                carry = carried
                l1 = l1.next
            elif l2 and not l1:
                val = l2.val + carry
                carried = val // 10
                staying = val % 10
                to_return.append(staying)
                carry = carried
                l2 = l2.next
        
        if carry != 0:
            to_return.append(carry)
        
        dummy = ListNode(1000)
        curr = dummy
        for i in range(len(to_return)):
            curr.next = ListNode(to_return[i])
            curr = curr.next
        
        return dummy.next
        