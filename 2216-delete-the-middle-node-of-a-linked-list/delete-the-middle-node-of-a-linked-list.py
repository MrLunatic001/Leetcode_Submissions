# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headRef = head
        newHead = head
        l = []
        length = 0
        while head:
            l.append(head)
            length += 1
            head = head.next
        mid = length // 2
        counter = 0
        if mid == 0:
            return None
        while newHead:
            if counter + 1== mid:
                newHead.next = newHead.next.next
                break
            else:
                newHead = newHead.next
                counter += 1

        return headRef