with open ("names.txt") as f:
    f.readline()
    dic = {}
    for i in f:
        lst = i.strip().split(" ")
        first_name = lst[0]
        last_name = lst[-1]

        if last_name not in dic:
            dic[last_name]=set()
        dic[last_name].add(first_name)
    for a in dic:
        print(a, ":", dic[a])