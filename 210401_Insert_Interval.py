from typing import List
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
'''

class Solution():
    def insert(self, intervals:List[List[int]], newInterval: List[int]) -> List[List[int]]: 
            if len(intervals) == 0:
                return [newInterval]
            result = []
            int_start = newInterval[0]
            int_end = newInterval[1]
            mergedInterval = []
            # Edge case : [[6,8]], [1,5] // [[1,5]], [6,8] -> interval에 비해 더 작거나 더 큰 경우
            for interval in intervals:
                if int_end < interval[0]:
                    result.append(interval)
                else:
                    if int_start > interval[1]:
                        result.append(interval)
                    else:
                        int_start = min(int_start, interval[0])
                        int_end = max(int_end, interval[1])
                        mergedInterval = [int_start, int_end]
            result.append(mergedInterval)
            result.sort(key=lambda x: x[0])
            return result

intervals = [[6,8]]
newInterval = [1,5]
s = Solution()
print(s.insert(intervals, newInterval)) 