class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start time ascending; if starts match, sort by end time descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining_count = 0
        max_end = 0
        
        for start, end in intervals:
            # If the current end extends past the maximum end seen so far
            if end > max_end:
                remaining_count += 1
                max_end = end
                
        return remaining_count
