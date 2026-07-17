class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mininum = inf
        arr.sort()
        answer = []
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) < mininum:
                mininum = (arr[i+1] - arr[i])

        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) == mininum:
                answer.append([arr[i],arr[i+1]])
        return answer
        