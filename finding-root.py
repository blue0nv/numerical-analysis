eq = ""

def func_input():
    global eq
    print("This program finds the root of a given function, for power use '^' and for multiplication use '*'")

    while True:
        eq = input("Enter the function in terms of x: ")

        if 'x' not in eq:
            print("Please enter a valid function containing 'x'.")
            continue

        eq = eq.replace("^", "**")

        try:
            x = 1
            test = eval(eq)
        except Exception:
            print("Please enter a valid function.")
            continue

        print("Valid function, please choose a method")
        break
    return eq

def fn(x):
    global eq
    return eval(eq)

func_input()