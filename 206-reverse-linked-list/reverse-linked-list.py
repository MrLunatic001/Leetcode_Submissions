# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        counter = 0
        while head and head.next:
            nextElem = head.next
            if counter == 0:
                head.next = None
                
            else:
                head.next = prevElem

            prevElem = head
            head = nextElem
            counter += 1
        head.next = prevElem

        return head
        