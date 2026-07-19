# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head and head.next:
            nums.append(head.val)
            head = head.next

        nums.append(head.val)
        

        for i in range(1,len(nums)):
            j = i - 1
            key = nums[i]
            while nums[j] > key and j >= 0:
                nums[j+1] = nums[j]
                j -= 1

            nums[j+1] = key
        ans = ListNode()
        head = ans
        for i in range(len(nums) -1):
            head.val = nums[i]
            tempNode = ListNode()
            head.next = tempNode
            head = head.next
        head.val = nums[-1]
        head.next = None
        return ans

        