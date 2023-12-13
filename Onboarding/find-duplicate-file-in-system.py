class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for files in paths:
            vals = files.split()
            root = vals[0]
            i = 1
            while i < len(vals):
                chars = vals[i].split("(")
                store[chars[1][:-1]].append(root +"/"+ chars[0])
                i += 1
        ans = []
        for vals in store.values():
            if len(vals) > 1:
                ans.append(vals)
        return ans