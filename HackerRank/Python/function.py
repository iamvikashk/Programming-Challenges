if __name__ == '__main__':
    year = int(input().strip())

    def is_leap(data):
        leap = False
        if data % 400 == 0:
            leap = True
        elif data % 100 == 0:
            leap = False
        elif data % 4 == 0:
            leap = True
        print(leap)

    is_leap(year)
