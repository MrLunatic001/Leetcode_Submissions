class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        maxAltitude = 0
        for g in gain:
            altitude += g
            if altitude > maxAltitude:
                maxAltitude = altitude
        return maxAltitude