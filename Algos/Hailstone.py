def hailstone():
    n = int(input("Enter n: ").strip())
    masterSeries = []
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, n + 1):
                if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                    print(i, j, k, "Divergent")
                else:
                    out = generateSeries(i, j, k)
                    if len(out[1]):
                        masterSeries.append(out[1])
                        print(i, j, k, out[0], out[1])
                    else:
                        print(i, j, k, out[0])
    uniqueList = [list(x) for x in set(tuple(x) for x in masterSeries)]
    print("Number of different holding patterns: " + str(len(uniqueList)))


def generateSeries(a, b, number):
    convergingSeries = []
    series = []
    for i in range(1, 100):
        if number % 2 == 0:
            number = number // 2
        else:
            number = a * number + b
        if number not in series:
            series.append(number)
            convergingSeries = []
            seqType = "Divergent"
        else:
            series.append(number)
            convergingSeries = series[series.index(number):]
            seqType = "Convergent"
            break
    return seqType, convergingSeries


hailstone()
