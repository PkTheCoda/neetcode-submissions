# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        start_group = dummy
        end_group = dummy
        counter = 0

        while end_group:

            end_group = end_group.next
            counter += 1

            if not end_group:
                break

            if counter == k:
                counter = 0 # reset to 1 because end_group doesnt end on end of curr section, but start of nxt section

                # reverse start_group -> end_group area
                prev = None
                curr = start_group.next
                end_group_next = end_group.next
                original_tail = start_group.next

                while curr != end_group_next:
                    curr_next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = curr_next
                
                # at the end, link start_group.next (first node in section) to end_group_next (starting node of next section)
                
                start_group.next = end_group
                original_tail.next = end_group_next
                start_group = original_tail
                end_group = start_group
        
        return dummy.next
