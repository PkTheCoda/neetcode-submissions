# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first get both ends of the list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # initialize both heads
        list1 = head
        list2 = slow.next

        # slow ends on end of l1, so sever it from l2
        slow.next = None

        # reverse list2
        curr = list2
        prev = None
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        
        # prev now head of list2
        list2 = prev

        # merge both lists
        while list2: # only while list2 because list2 always has less elements than l1. any leftover elements r part of list1 and can just be merged
            l1next, l2next = list1.next, list2.next
            list1.next = list2
            list2.next = l1next
            list1 = l1next
            list2 = l2next
        
        return None


