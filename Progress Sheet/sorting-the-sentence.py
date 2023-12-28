class Solution:
    def sortSentence(self, s: str) -> str:
        nums = s.split(" ")
        x = ''
        for j in range(1,len(nums)+1):
            for i in nums:
                if int(i[len(i)-1]) == j:
                    x = x + str(i.replace(i[len(i)-1] , " "))
        return x[0:len(x)-1]
