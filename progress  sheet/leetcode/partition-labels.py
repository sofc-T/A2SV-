class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ind = {s[ind] : ind for ind in range(len(s))}
        end, l = 0, 0
        partitions = []
        for r in range(len(s)):
            end = max(end,last_ind[s[r]])
            if r == end:
                partitions.append(end+1-l)
                l = end + 1
            
        return partitions