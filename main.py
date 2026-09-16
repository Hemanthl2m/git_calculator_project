from operations import add, subtract, multiply, divide, average

def main():
    print("Simple Calculator")
    a = 10
    b = 5

    print("Add:", add(a, b))
    print("Subtract:", subtract(a, b))
    print("Multiply:", multiply(a, b))
    print("Division:", divide(a,b))
    print("Average: ", average(a,b))

if __name__ == "__main__":
    main()