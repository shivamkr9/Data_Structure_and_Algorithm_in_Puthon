"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans= [-1,-1]
        start =0
        end= len(nums) -1
        if end == -1:
            return ans

        while(start<=end):
            mid = start + (end - start)//2
            # print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                start = mid+1
            elif nums[mid]> target:
                end = mid
            else:
                return ans


nums = [5,7,7,8,8,10]
target = 8

print(Solution().searchRange(nums, target))