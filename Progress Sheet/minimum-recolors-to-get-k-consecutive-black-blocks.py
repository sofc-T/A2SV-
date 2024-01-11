class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        recolors = blocks[:k].count("W")
        minn = recolors
        l, r =0, k
        while r < len(blocks):
            if blocks[l] == "W":
                recolors -= 1
            if blocks[r] == "W":
                recolors += 1
            l += 1
            r += 1
            minn = min(recolors,minn)
        return minn