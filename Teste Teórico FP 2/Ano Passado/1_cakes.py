def cakes(recipe, available):
    bolos = 0
    lst = []
    for k in recipe.keys():
        for key in available.keys():
            if k == key and len(available) >= len(recipe):
                quantidade = available[k]//recipe[k]
                lst.append(quantidade)
                bolos = min(lst)
    return bolos

def main():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200} 
    print(cakes(recipe, available)) # Deve printar 2

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000} # Deve printar 0
    print(cakes(recipe, available))

    recipe = {"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000}
    print(cakes(recipe, available)) # Deve printar 11

if __name__ == "__main__":
    main()