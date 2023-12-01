class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sorted_words = sorted(words,key= lambda x : [order.index(y) for y in x])
        return sorted_words == words