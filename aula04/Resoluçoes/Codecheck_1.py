def isLeapYear(year):
    return year%4 == 0 and year%100 != 0 or year%400 == 0

def printLeapYears(year1, year2):
    """Print all leap years in range [year1, year2[."""
    year  = year1
    while year < year2:
        result = isLeapYear(year)
        if result == True:
            print(year)
            year+=1
        else:
            year +=1
            continue

def numLeapYears(year1, year2):
    """Return the number of leap years in range [year1, year2[."""
    # Try to use a for loop!
    count=0
    for year in range(year1, year2):
        result = isLeapYear(year)
        if result == True:
            count +=1
        else:
            continue
    return count

def nextLeapYear(year):
    """Return the first leap year after the given year."""
    # Which kind of loop is more appropriate?
    year +=1
    while True:
        result = isLeapYear(year)
        if result == True:
            break
        else:
            year +=1
    return year

def listLeapYears(year1, year2):
    """Return a list of leap years in range [year1, year2[."""
    lst = []
    # To add a value to the list, use:
    # lst.append(value)
    # (We'll get back to lists later in the course.)
    for year in range(year1, year2):
        result = isLeapYear(year)
        if result == True:
            lst.append(year)
        else:
            continue
    return lst


# MAIN PROGRAM:
def main():
    printLeapYears(1870, 1921)

    x = numLeapYears(1679, 2079)
    print("In [1679, 2079[ there are", x, "leap years")

    print(f"{nextLeapYear(2024) = }")  # 2028
    print(f"{nextLeapYear(1893) = }")  # 1896
    print(f"{nextLeapYear(1896) = }")  # 1904

    print(listLeapYears(1970, 2002))

main()