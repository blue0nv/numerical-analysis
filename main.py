import config
import functions

print("This program finds the root of a given function, for power use '^'")

def main():
    flag = True
    while flag:
        config.target_error = float(input("Enter the acceptable error percentage: "))
        functions.func_input()
        is_solved = False

        print("1. Bisection Method")
        print("2. Secant Method")
        print("3. False Position Method")
        print("4. Simple Fixed Point Method")
        print("5. Newton Method")

        is_chosen = False
        while not is_chosen:
            choice = input("Please enter the number of the desired method to calculate the root: ")

            match choice:
                case "1":
                    is_chosen = True
                    xl = float(input("Please enter the lower bound of the root: "))
                    xu = float(input("Please enter the upper bound of the root: "))
                    if functions.fn(xl) * functions.fn(xu) < 0:
                        print("The equation is solvable")
                        res = functions.bisection(xl, xu)
                        is_solved = True
                    else:
                        print("The equation is not solvable")

                case "2":
                    is_chosen = True
                    xi_1 = float(input("Please enter Xi_-1: "))
                    x0 = float(input("Please enter Xi_0: "))
                    res = functions.secant(xi_1, x0)
                    is_solved = True

                case "3":
                    is_chosen = True
                    xl = float(input("Please enter the lower bound of the root: "))
                    xu = float(input("Please enter the upper bound of the root: "))
                    if functions.fn(xl) * functions.fn(xu) < 0:
                        print("The equation is solvable")
                        res = functions.false_position(xl, xu)
                        is_solved = True
                    else:
                        print("The equation is not solvable")

                case "4":
                    is_chosen = True
                    functions.func_arrange()
                    xi = float(input("Please enter the initial guess of the root: "))
                    res = functions.simple_fixed_point(xi)
                    is_solved = True

                case "5":
                    is_chosen = True
                    xi = float(input("Please enter the initial guess of the root: "))
                    res = functions.newton(xi)
                    is_solved = True

                case _:
                    print("Please enter a valid option")
                    continue

        if is_solved:
            print("The result is: " + str(res))

        ans = input("Do you want to try again? (y/n): ")
        if ans == "y":
            continue
        else:
            flag = False

main()