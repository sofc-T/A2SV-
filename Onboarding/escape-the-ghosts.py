class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        g_moves = inf
        for x, y in ghosts:
            g_moves = min(abs(target[0]-x) + abs(target[1]-y),g_moves)
        if abs(target[0]) + abs(target[1]) >= g_moves:
            return False
        return True