class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        steps = {1:0}
        def get_index(pos):
            r = n-((pos-1)//n)-1
            if r%2 == (n-1)%2:
                c = (pos-1)%n
            else:
                c = n-(pos-1)%n-1
            return r, c

        q = deque([1])
        while q:
            i = q.popleft()
            for t in range(i+1, i+7):
                r, c = get_index(t)
                nex = board[r][c]
                if nex > 0: t = nex
                if t == n**2:
                    return steps[i]+1
                if t not in steps:
                    steps[t] = steps[i]+1
                    q.append(t)
        return -1