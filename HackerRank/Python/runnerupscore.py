if __name__ == '__main__':
    n = int(input().strip())
    arr = sorted(list(map(int, input().split())))
    max_num = arr[-1]
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < max_num:
            print(arr[i])
            break
