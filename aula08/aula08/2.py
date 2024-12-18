with open("names.txt", "r", encoding="utf-8") as f:
    f.readline()
    dic = {}
    for line in f:
        name = line.strip().split(" ")
        first_name = name[0]
        last_name = name[-1]


        if last_name not in dic:
            dic[last_name]=set()
            dic[last_name].add(first_name)
        else:
            dic[last_name].add(first_name)

    for a in dic:
        print(a, ":", dic[a])