# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None

        if not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1

        newlist = None

        if list1.val > list2.val:
            newlist = list2
            list2 = list2.next
        else:
            newlist = list1
            list1 = list1.next

        curr = newlist
        while list1 or list2:

            # one list is empty, so then rest of the list is just the non-empty list
            if not list1 and list2:
                curr.next = list2
                break
            elif not list2 and list1:
                curr.next = list1
                break
            
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            
            curr = curr.next
        
        return newlist
            



        
        