def parseMDY(dateStr):
    """Return (year, month, day) from date in MM/DD/YYYY format."""
    parts = dateStr.split("/")
    if len(parts) == 3:
        month, day, year = map(int, parts)
    elif len(parts) == 1:
        year = int(parts[0])
        month = day = 0
    else:
        raise ValueError("Invalid date format")
    return (year, month, day)

def yearsBetween(date1, date2):
    """Return integer number of years between two (y, m, d) dates."""
    dia1 = date1[2]
    mes1=date1[1]
    ano1=date1[0]
    dia2=date2[2]
    mes2=date2[1]
    ano2=date2[0]

    dif_anos = ano2-ano1

    if mes2<mes1:
        dif_anos -=1

    if (mes1==mes2) and dia2<dia1:
        dif_anos -=1

    return dif_anos

def main():
    # Test parseMDY
    print(f"{parseMDY('12/25/2024') = }")  # (2024, 12, 25)
    print(f"{parseMDY('4/25/1974') = }")   # (1974, 4, 25)
    print(f"{parseMDY('1755') = }")        # (1755, 0, 0)

    # Test yearsBetween
    print(f"{yearsBetween((1900, 6, 1), (1935, 5, 31)) = }")  # 34
    print(f"{yearsBetween((1900, 6, 1), (1935, 6, 1)) = }")   # 35
    print(f"{yearsBetween((1900, 6, 1), (1936, 5, 31)) = }")  # 35


# This program may be used as a module too
if __name__ == "__main__":
    main()

