class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        tcounter= Counter(t)
        tlen = len(tcounter)
        okay = []
        minn, maxx = 0, inf
        l, r = 0, 0
        while r < len(s):
            # print(minn,maxx)
            counter[s[r]] += 1
            if s[r] in tcounter and counter[s[r]] == tcounter[s[r]]:
                okay.append(1)
            if len(okay) == tlen:
                # print("ok",maxx,minn)
                if maxx - minn  > r - l + 1:
                    minn, maxx = l , r + 1
                # print("ok",maxx,minn, l, r)
                while True:
                    counter[s[l]] -= 1
                    if s[l] in tcounter  and counter[s[l]] < tcounter[s[l]]:
                        if maxx - minn  > r - l + 1:
                            minn, maxx = l , r + 1
                        okay.pop()
                        l += 1
                        while l < r and s[l] not in tcounter:
                            l += 1
                        break
                    l += 1
                # print(l,r,"out")
            r += 1
        # print(len(t))
    
        if maxx - minn  > r - l + 1 and len(okay) == tlen:
            minn, maxx = l - 1, r
        if maxx == inf:
            return ""
        # print(minn,maxx)
        return s[minn:maxx]