# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_list(node: Optional[ListNode]) -> ListNode:
            prev, curr = None, node

            while curr:
                temp = curr.next
                curr.next = prev;
                prev = curr
                curr = temp
            return prev
        
        l, r = head, head.next

        while r and r.next:
            l = l.next
            r = r.next.next
        
        reversed_l_head = reverse_list(l)

        l,r = head, reversed_l_head

        while l and r:
            temp1, temp2 = l.next, r.next
            l.next = r
            r.next = temp1
            l = temp1
            r = temp2