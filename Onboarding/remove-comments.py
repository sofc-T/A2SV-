class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        ind = 0
        
        code = ""
        open = False
        while ind < len(source):
            i, mark = 0, 0
            b = 0
            line = source[ind]
            while i < len(line)-1:
                if line[i:i+2] == "//":
                    b = 1
                    break
                elif line[i:i+2] == "/*":
                    open = True
                    code += line[mark:i]
                    i += 2
                    
                    while i < len(line)-1: 
                        if line[i:i+2] == "*/":
                            mark = i + 2
                            open = False
                            b = 2
                            i += 2
                            break
                        i += 1
                        if open and i == len(line)-1:
                            ind += 1
                            while len(source[ind]) < 2:
                                ind += 1
                            line = source[ind]
                            i = 0
                else:
                    i += 1
            if b == 1:code += line[mark:i]
            else:code += line[mark:i+1]
            if code: res.append(code)
            code = ""
            ind += 1
            mark = 0
        return res
            
                                