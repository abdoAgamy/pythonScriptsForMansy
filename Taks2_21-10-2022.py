import sys

def handel_draw():
    first_shape = 6
    for i in range(first_shape):
        sys.stdout.write("*" * i + "\n")
    second_shape = 4
    while second_shape >= 1:
        sys.stdout.write("*" * second_shape + "\n")
        second_shape -= 1

def handel_factorial():
    num = int(input("Enter number to calculate factorial"))
    base = 1
    if num == 0:
        base = 1
        sys.stdout.write(f"Factorial of {num} is: {base}" + "\n")
    elif num <= 0:
        sys.stdout.write(f"Invalid " + "\n")
    else:
        for i in range(1, num + 1):
            base = base * i
        sys.stdout.write(f"Factorial of {num} is: {base}" + "\n")


def handel_fibonacci():
    n1 = 0
    n2 = 1
    count = 0
    fib_list = []
    while count < 9:
        fib_list.append(n1)
        both = n1 + n2
        n1 = n2
        n2 = both
        count += 1
    print(fib_list)
    fib_element = int(input("Pick a number from the list "))
    for num in fib_list:
        if fib_element == num:
            if fib_element == 21:
                print("Out of  Range")
                break
            next = fib_list.index(num)
            print(f"Next Element is {fib_list[next+1]}")
    if fib_element not in fib_list:
       print(f"{fib_element} is Not in the List")



def End():
    sys.exit()


if __name__ == '__main__':
    mapper = {
        1: "handel_fibonacci",
        2: "handel_factorial",
        3: "handel_draw",
        0: "End"
    }
    while True:
        choice = int(input("Enter number between 1 : 3  or 0 to exit\n"))
        if choice in mapper.keys():
            eval(mapper.get(choice))()
        else:
            sys.stdout.write("Invalid Choice\n")
