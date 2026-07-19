class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = j = 0
        arr = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        arr.extend(nums1[i:m])
        arr.extend(nums2[j:])

        for k in range(m + n):
            nums1[k] = arr[k]