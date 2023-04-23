from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        endValue = len(letters) - 1
        if ((target == letters[start]) and (target < letters[start + 1])):
            return letters[start + 1]

        elif (target == letters[endValue]):
            return letters[0]

        else:
            while (start != endValue):
                mid = int(start + (endValue - start) / 2)
                if (target == letters[mid]) and (letters[mid] < letters[mid + 1]):
                    print("hi")
                    return letters[mid + 1]

                elif (target > letters[mid - 1] and target < letters[mid]):
                    print("hi1")
                    return letters[mid]

                elif (target < letters[mid + 1] and target > letters[mid]):
                    print("h12")
                    return letters[mid + 1]

                elif (target < letters[mid]):
                    endValue = mid - 1

                else:
                    start = mid + 1

        return letters[0]


letters = ["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"]

target = "k"

print(Solution().nextGreatestLetter(letters=letters, target=target))


