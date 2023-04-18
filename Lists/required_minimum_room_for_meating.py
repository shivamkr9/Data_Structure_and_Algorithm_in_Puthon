"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Input: intervals = [[7,10],[2,4]]
Output: 1

Input: intervals = [[0,30],[15,20],[30,45]]
Output: 2

//Discuss the approach
"""


class Solution:
    def solution(self, s):
        requiredRoom = 1
        for i in range(0, len(s)-1):
            if s[i][0]>s[i+1][0]:
                continue
            elif s[i][1]>s[i+1][0]:
                requiredRoom +=1
        print(requiredRoom)


def main():
    intervals = [[0,30],[15,20],[30,45]]
    Solution().solution(intervals)


if __name__ == '__main__':
    main()
