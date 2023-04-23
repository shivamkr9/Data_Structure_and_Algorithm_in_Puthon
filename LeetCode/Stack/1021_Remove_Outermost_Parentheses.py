"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.



Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".



Constraints:

    1 <= s.length <= 105
    s[i] is either '(' or ')'.
    s is a valid parentheses string.


"""

from collections import deque


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        isValid = True
        output_str = ""
        dq = deque()
        counter = -1
        for item in s:
            if item == "(":
                counter += 1
                if counter == 0 and isValid == True:
                    isValid = False
                    continue
                else:
                    # output_str += item
                    dq.append(item)
            else:
                counter -= 1
                if counter == -1 and isValid == False:
                    isValid = True
                    continue
                else:

                    # output_str += item
                    dq.append(item)
        return "".join(dq)  # output_str


"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1

        return "".join(res)
"""


def main():
    s = "(()())(())(()(()))"
    solution = Solution()
    result = solution.removeOuterParentheses(s)
    print(result)


if __name__ == "__main__":
    main()
