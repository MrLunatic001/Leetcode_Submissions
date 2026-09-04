class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals (meetings) by end time
        intervals.sort(key=lambda x: x[1])
        
        numberOfScheduledMeetings = len(intervals)
        prev = 0
        # We need to keep at least one meeting in our schedule
        meetingsToKeep = 1

        for cur in range(1, numberOfScheduledMeetings):
            if intervals[cur][0] >= intervals[prev][1]:
                meetingsToKeep += 1

                # we can keep the previous meeting
                # So, now we check if we can keep the current one
                prev = cur

        meetingsToRemove = numberOfScheduledMeetings - meetingsToKeep
        
        return meetingsToRemove