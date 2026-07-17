# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        if not head:
            return answer
        
        values = []
        while head:
            values.append(head.val)
            if not head.next:
                break
            else:
                head = head.next
        answer = [0]*len(values)
        stack = []
        for i, val in enumerate(values):
            while stack and values[stack[-1]] < val:
                answer[stack.pop()] = val


            stack.append(i)
        
        return answer