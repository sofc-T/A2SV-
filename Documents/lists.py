if __name__ == '__main__':
    n = int(input())
    list=[]
    i=1
    while i <= n:
        cmd = input().strip().split(" ")
        if cmd[0]=="insert":
            list.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'append':
            list.append(int(cmd[1]))
        elif cmd[0] == 'sort' and list:
            list.sort()
        elif cmd[0] == 'remove' and list:
            list.remove(int(cmd[1]))
        elif cmd[0] == 'reverse' and list:
            list.reverse()
        elif cmd[0] == 'pop' and list:
            list.pop()
        elif cmd[0] =="print":
            print(list)
        else:
            pass
        i+=1






