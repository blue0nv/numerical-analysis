import sympy as sp

eq = ""
i = 0
print("This program finds the root of a given function, for power use '^' and for multiplication use '*'")
target_error = float(input("Enter the acceptable error percentage: "))

#----------------------------------- Functions that are needed for calculations ----------------------------------------

def func_input():
    global eq
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

def derive(equ):
    x = sp.symbols('x')
    func = sp.sympify(equ)
    res = sp.diff(func, x)
    return sp.lambdify(x, res, "math")

# --------------------------------------------- Method functions -------------------------------------------------------

def newton(xi):
    global eq, i, target_error
    fn_dash = derive(eq)

    xi_1 = xi - (fn(xi) / fn_dash(xi))
    if i != 0:
        error = abs((xi_1 - xi) / xi_1) * 100

    print(f"I={i:2d} | "
          f"Xi={xi:8.4f} | "
          f"F(Xi)={fn(xi):9.4f} | "
          f"F'(Xi)={fn_dash(xi):9.4f}", end="")

    if i != 0:
        print(f" | ERROR= %{error:8.4f}", end="")

    input("     Press [Enter] to show the next iteration")

    if i != 0 and error <= target_error:
        i = 0
        return xi_1

    i += 1
    return newton(xi_1)

