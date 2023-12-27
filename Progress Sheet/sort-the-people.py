class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Bubble 
        # for i in range(len(names)):
        #     for idx in range(len(names)-1):
        #         if heights[idx] < heights[idx+1]:
        #             names[idx], names[idx+1] = names[idx+1], names[idx]
        #             heights[idx], heights[idx+1] = heights[idx+1], heights[idx]
        # return names
        

        # Random Idea
        # store = {name:heights[i] for i,name in enumerate(names)}
        # print(store)
        # return sorted(names,key = lambda name: store[name], reverse=True)


        # Selection
        # min_idx = 0
        # while min_idx < len(names):
        #     val = heights[min_idx]
        #     for idx in range(min_idx+1,len(heights)):
        #         if heights[idx] > heights[min_idx]:
        #             heights[idx], heights[min_idx] = heights[min_idx], heights[idx]
        #             names[idx], names[min_idx] = names[min_idx], names[idx]
        #     min_idx += 1
        # return names

        # Insertion 
        # for idx in range(1,len(heights)):
        #     while idx > 0 and heights[idx] > heights[idx-1]:
        #         heights[idx], heights[idx-1] = heights[idx-1], heights[idx]
        #         names[idx], names[idx-1] = names[idx-1], names[idx]
        #         idx -= 1
        # return names

        # Counting 
        maxx = max(heights)
        freq = [0] * (maxx + 1)
        for idx in range(len(heights)):
            freq[heights[idx]] = names[idx]
        res = []
        for name in freq:
            if name:
                res.append(name)
        return res[::-1]