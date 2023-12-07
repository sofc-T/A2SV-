class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        store2 = {word:ind for ind, word in enumerate(list2)}
        ans, minn = [], 2001
        for ind, word in enumerate(list1):
            val = ind + store2.get(word,inf)
            if val < minn:
                ans = [word]
                minn = val
            elif val == minn:
                ans.append(word)
                minn = val
        return ans