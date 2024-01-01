class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        maxx, i = 0, 0
        j = 0
        for processor in processorTime:
            maxx = max(maxx,max(tasks[i:i+(len(tasks)//len(processorTime))])+processorTime[j])
            i += len(tasks)//len(processorTime)
            j += 1
        return maxx