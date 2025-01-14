
def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    print("a) Table of common interests:")
    def test1():
        dic = {}
        for person1 in interests:
            for person2 in interests:
                if person1!=person2 and (person2, person1) not in dic:
                    dic[(person1, person2)] = set()
                    for interest in interests[person1]:
                        if interest in interests[person2]:
                            dic[(person1, person2)].add(interest)

        return dic
    commoninterests = test1()
    print(commoninterests)


    print("b) Maximum number of common interests:")
    maxCI = max([len(commoninterests[i]) for  i in  commoninterests])
    print(maxCI)

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [(persons) for persons in commoninterests if len(commoninterests[persons])==maxCI]
    print(maxmatches)

    print("d) Pairs with low similarity:")
    lowJaccard = [(person1, person2) for person1, person2 in commoninterests if len(commoninterests[(person1, person2)])/(len(interests[person1]) + len(interests[person2]) - len(commoninterests[person1, person2]))<0.25]
    print(lowJaccard)


# Start program:
main()

