class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit = {}
        l, r = 0, 0
        maxx = 0
        while r < len(fruits):
            fruit[fruits[r]] = fruit.get(fruits[r],0) + 1
            if len(fruit) == 3:
                maxx = max(maxx,r-l)
                while True:
                    fruit[fruits[l]] -= 1
                    if fruit[fruits[l]] == 0:
                        del fruit[fruits[l]]
                        break
                    l += 1
                l += 1
            r += 1
        return max(maxx,r-l)