if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score = [name,score]
        records.append(name_score)

    score_list = []
    name_list = []
    for i in range(len(records)):
        score_list = score_list + [records[i][1]]
    min_score = min(score_list)
    score_list = list(filter(lambda x: x!=min_score,score_list))
    min_score = min(score_list)
    for j in range(len(records)):
        if records[j][1] == min_score:
            name_list.append(records[j][0])
    name_list = sorted(name_list)
    for k in range(len(name_list)):
        print(name_list[k])
