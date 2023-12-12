class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        while n != 1:
            if n in store:
                return False
            store.add(n)
            n = sum(int(y)**2 for y in str(n))
        return True