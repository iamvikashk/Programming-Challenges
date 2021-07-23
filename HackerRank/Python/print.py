if __name__ == '__main__':
    n = int(input().strip())
    j = "1"
    for i in range(2, n + 1):
        j = j + str(i)
    print(j)
