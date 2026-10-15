# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        single=double=head
        while double and double.next is not None:
            double=double.next.next
            single=single.next
            if double == single:
                break
        else:
                return None

        p= head
        while p!=double:
            p=p.next
            double=double.next
        return p
