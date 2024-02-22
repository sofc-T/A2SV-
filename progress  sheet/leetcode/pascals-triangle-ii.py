class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def findRow(row,index):
            if index == 0:
                return list(row)
            ans = []
            for idx in range(len(row)):
                if idx == 0:
                    ans.append(1)
                else:
                    ans.append(row[idx-1] + row[idx])
            ans.append(1)
            return findRow(tuple(ans),index-1)
        return findRow((),rowIndex+1)
