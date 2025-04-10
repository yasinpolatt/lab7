import math_utils
number1 = int(input("Number  1 : "))
number2 = int(input("Number 2 : "))

def main():
    print("Add : ")
    print(math_utils.add(number1, number2))
    print("Mod : ")
    print(math_utils.mod(number1, number2))
    print("Divide : ")
    print(math_utils.divide(number1, number2))
    print("Substract : ")
    print(math_utils.substract(number1, number2))
    print("Multiply : ")
    print(math_utils.multiply(number1, number2))
    print("Power : ")
    print(math_utils.power(number1, number2))


if __name__ == "__main__":
    main()

