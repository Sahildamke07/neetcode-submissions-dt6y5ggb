class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checkb = {')':'(', ']':'[','}':'{'}
        for c in s:
            if c in checkb:
                if stack and stack[-1] == checkb[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False
            


                


              


        