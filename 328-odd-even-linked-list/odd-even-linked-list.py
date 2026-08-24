# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ans = head
        if head.next:
            skipStart = head.next
            skipPointer = head.next
        while head and head.next and head.next.next:
            head.next = head.next.next
            head = head.next
            if head.next:
                skipPointer.next = head.next
                skipPointer = skipPointer.next
            else:
                skipPointer.next = None
        head.next = skipStart
                
            
            




        return ans
        