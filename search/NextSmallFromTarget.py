from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    start =0
    end= len(nums) -1
    if end == -1:
        return -1
    elif nums[start] == target:
        return -1
    else:
        while(start<=end):
            mid = start + (end - start)//2
            if nums[mid] == target:
                if nums[mid-1]<target:
                    return mid-1
                end = mid -1
            elif nums[mid]<target:
                start = mid+1
            else:
                end = mid
    return -1


nums = [5,7,7,8,8,10]
target = 15

print(searchRange(nums, target))