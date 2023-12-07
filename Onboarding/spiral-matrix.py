class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right= 0, len(matrix)-1 , 0, len(matrix[0])-1
        res = []
        while top <= bottom and left <= right:
            # print(res)
            for ind in range(left,right+1):
                res.append(matrix[top][ind])
            top += 1
            if top > bottom:break
            for ind in range(top,bottom+1):
                res.append(matrix[ind][right])
            right -= 1
            if left > right: break
            for ind in range(right,left-1,-1):
                res.append(matrix[bottom][ind])
            bottom -= 1
            if top > bottom:break
            for ind in range(bottom,top-1,-1):
                res.append(matrix[ind][left])
            left += 1
        return res
