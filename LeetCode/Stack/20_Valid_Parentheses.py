"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false



Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.


"""


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack =[]
#         for item in s:
#             if item == "(" or item =="[" or item =="{":
#                 stack.append(item)
#             else:
#                 if not stack:
#                     return False
#                 elif item == ")" and stack[-1] == "(":
#                     stack.pop()
#                 elif item == "]" and stack[-1] == "[":
#                     stack.pop()
#                 elif item == "}" and stack[-1] == "{":
#                     stack.pop()
#                 else:
#                     return False
#         return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        dic = {'(': ')', '{': '}', '[': ']'}
        left = "([{"
        for i in s:
            if i in left:
                lst.append(dic[i])
            elif lst and lst[-1] == i:
                lst.pop()
            else:
                return False
        return not lst
