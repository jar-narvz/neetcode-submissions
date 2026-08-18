class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in dict:
                if not stack or stack.pop() != dict[c]:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

