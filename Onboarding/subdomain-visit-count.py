class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(int)
        for domain in cpdomains:
            ind = domain.index(" ")
            cont = [domain[:ind],domain[ind+1:]]
            num = int(cont[0])
            for ind in range(len(domain)):
                if domain[ind] == " " or domain[ind] == ".":
                    res[domain[ind+1:]] += num
        ans = []
        for key in res:
            ans.append(str(res[key]) + " " + str(key))
        return ans