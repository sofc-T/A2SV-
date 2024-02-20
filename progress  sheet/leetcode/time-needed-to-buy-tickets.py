class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for idx, ticket in enumerate(tickets):
            if idx < k:
                if ticket > tickets[k]:
                    time += tickets[k]
                else:
                    time += ticket
            elif idx == k:
                time += ticket
            else:
                if ticket >= tickets[k]:
                    time += tickets[k] - 1
                else:
                    time += ticket
        return time