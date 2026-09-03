class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for s in spells:
            idx = search(s,potions,success)
            ans.append(len(potions) - idx)

        return ans

def search(spell, potions, success):
    left  = 0
    right = len(potions) - 1
    idx = len(potions) 
    while left <= right:
        mid = (left + right) // 2
        if spell*potions[mid] >= success:
            changed = True
            if mid < idx:
                idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return idx