if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd = input().split()
        func = cmd[0]
        args = cmd[1:]
        if func == "insert":
            args = [int(i) for i in args]
        elif func == "print" or func == "sort" or func == "pop" or func == "reverse":
            pass
        else:
            args = int(args[0])
        if func == "print":
            print(lst)
        elif func == "insert":
            lst.insert(args[0], args[1])
        elif func == "remove":
            lst.remove(args)
        elif func == "append":
            lst.append(args)
        elif func == "sort":
            lst.sort()
        elif func == "reverse":
            lst.reverse()
        elif func == "pop":
            lst.pop()

