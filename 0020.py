class Solution20:
    def isValid(self, s):
        stack = []
        paren_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop():
                return False

        return not stack

    def isValid2(self, s: str) -> bool:
        stack, d = [], {'{': '}', '[': ']', '(': ')'}
        for p in s:
            if p in '{[(':
                stack += [p]
            elif not (stack and d[stack.pop()] == p):
                return False
        return not stack
