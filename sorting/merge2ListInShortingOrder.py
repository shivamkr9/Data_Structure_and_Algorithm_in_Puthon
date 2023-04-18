"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

 Merge nums1 and nums2 into a single array sorted in non-decreasing order.

 The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
 accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
 Output: [1,2,2,3,5,6]

                     i.k                        j
# Input: nums1 = [1,2,3,3,5,6], m = 3, nums2 = [2,5,6], n = 3
 Note:- time complexity not be O(n^2)
"""
"""
    time complexity O(m+n) and space complexity O(1)
"""

from typing import List


class Solution:

    def merge(self, nums1, m, nums2, n):
        """
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        The final sorted array should be stored inside the array nums1.
        """
        # initialize two pointers for nums1 and nums2, starting from the end
        i, j = m - 1, n - 1
        # iterate over nums1 from the end and fill it with the largest element from nums1 or nums2
        for k in range(m + n - 1, -1, -1):
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1


def main():
    nums1: List[int] = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2: List[int] = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)


if __name__ == '__main__':
    main()
