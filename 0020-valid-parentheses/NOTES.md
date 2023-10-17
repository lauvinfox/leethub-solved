Alternative solution:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchCh = {")":"(", "]":"[", "}":"{"}
        
        for ch in s:
            if ch in matchCh:
                if stack and stack[-1] == matchCh[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return not stack​
