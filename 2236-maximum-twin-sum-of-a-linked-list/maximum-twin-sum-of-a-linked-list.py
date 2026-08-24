# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = -inf
        st = []
        n = 0
        headRef = head
        while head:
            n += 1
            st.append(head.val)
            head = head.next
        for i in range(n//2):
            maxSum = max(maxSum, st[i] + st[n-1-i])
        return maxSum
