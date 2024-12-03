import math

def floatInput(prompt, min=None, max=None):
    try:
        res = float(input(prompt))
        if min==None and max==None:
            return res
        elif min <= res <= max:
            return res
        else:
            print("Error: Value should be in [{}, {}]".format(min, max))
            return floatInput(prompt, min, max)
    except:
        print("Error: Not a float!")
        return floatInput(prompt, min, max)

def floatInput_temperature(prompt, min, max):
    try:
        res = float(input(prompt))
        if min <= res <= max:
            print("Error: Value out of range!")
            return res
        else:
            return floatInput_temperature(prompt, min, max)
    except:
        print("Error: Not a float!")
        return floatInput_temperature(prompt, min, max)


def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")

    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput_temperature("Humidity (%)? ", 0, 100)
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min=-273.15)
    print("t:", t)

    #d) What happens if you uncomment this?
    impossible = floatInput("Value in [3, 0]? ", min=3, max=0)

    return

if __name__ == "__main__":
    main()
