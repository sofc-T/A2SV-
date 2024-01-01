class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # tasks.sort()
        # processorTime.sort(reverse=True)
        # maxx, i = 0, 0
        # j = 0
        # for processor in processorTime:
        #     maxx = max(maxx,max(tasks[i:i+(len(tasks)//len(processorTime))])+processorTime[j])
        #     i += len(tasks)//len(processorTime)
        #     j += 1
        # return maxx


        
        # s = zip(sorted(tasks),sorted(processorTime))
        # t = zip(sorted(tasks)[::-4],sorted(processorTime))
        # print(list(s),list(t))
        return max(task + time for (task,time) in zip(sorted(tasks)[::-4],sorted(processorTime)))