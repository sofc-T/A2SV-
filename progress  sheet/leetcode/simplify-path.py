class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for chr in path:
            if chr == "..":
                if stack:
                    stack.pop()
            elif chr != "." and chr != "":
                stack.append(chr)
        return "/" + "/".join(stack)