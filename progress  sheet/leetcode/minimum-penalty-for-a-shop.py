class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penality = customers.count("Y")
        minPenality = [0, penality]
        for idx, val in enumerate(customers):
            if customers[idx] == "Y":
                penality -= 1
            else:
                penality += 1
            if penality < minPenality[1]:
                minPenality = [idx+1,penality]
        return minPenality[0]