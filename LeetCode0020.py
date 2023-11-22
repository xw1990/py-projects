
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['1']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        print("remain:",stack)
        return len(stack) == 1

test = Solution()    
print("result:",test.isValid('[][][][][][]'))