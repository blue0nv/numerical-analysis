import sympy as sp
import config

def num_validator(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def input_validator(target_error, eq_text, status_label):
    if 'x' not in eq_text:
        status_label.config(text="Function must contain 'x'", fg="red")
        return False

    config.eq = eq_text
    config.new_eq = ""

    for index, letter in enumerate(config.eq):
        config.new_eq += letter

        if letter.isdigit() and index + 1 < len(config.eq) and config.eq[index + 1] == 'x':
            config.new_eq += '*'
        elif letter.isdigit() and index + 4 <= len(config.eq) and config.eq[index + 1:index + 4] in ["sin", "cos", "tan"]:
            config.new_eq += '*'
        elif letter.isdigit() and index + 5 <= len(config.eq) and config.eq[index + 1:index + 5] == "sqrt":
            config.new_eq += '*'

    config.new_eq = config.new_eq.replace("^", "**")

    try:
        x = 1
        eval(config.new_eq, config.allowed | {"x": x})
    except Exception:
        status_label.config(text="Invalid Function", fg="red")
        return False

    try:
        float(target_error)
        status_label.config(text="Valid Input", fg="green")
        return True
    except ValueError:
        status_label.config(text="Invalid Error Percentage", fg="red")
        return False


def fn(x):
    return eval(config.new_eq, config.allowed | {"x": x})

def derive(equ):
    x = sp.symbols('x')
    func = sp.sympify(equ)
    res = sp.diff(func, x)
    return sp.lambdify(x, res, "math")

# will only be called once in main when sfp is chosen
def sfp_input(gx):
    config.arranged_func = ""

    if 'x' not in gx:
        return False

    for index, letter in enumerate(gx):
        config.arranged_func += letter

        if letter.isdigit() and index + 1 < len(gx) and gx[index + 1] == 'x':
             config.arranged_func += '*'
        elif letter.isdigit() and index + 4 <= len(gx) and gx[index + 1:index + 4] in ["sin", "cos", "tan"]:
            config.arranged_func += '*'
        elif letter.isdigit() and index + 5 <= len(gx) and gx[index + 1:index + 5] == "sqrt":
            config.arranged_func += '*'


    config.arranged_func = config.arranged_func.replace("^", "**")

    try:
        x = 1
        eval(config.arranged_func, config.allowed | {"x": x})
        return True
    except Exception:
            return False


def solve(x):
    return eval(config.arranged_func, config.allowed | {"x": x})

# --------------------------------------------- Method functions -------------------------------------------------------

# Method One
def newton(xi):
    fn_dash = derive(config.new_eq)

    xi_1 = xi - (fn(xi) / fn_dash(xi))
    if config.i != 0:
        error = abs((xi_1 - xi) / xi_1) * 100

    print(f"I={config.i:2d} | "
          f"Xi={xi:9.4f} | "
          f"F(Xi)={fn(xi):9.4f} | "
          f"F'(Xi)={fn_dash(xi):9.4f}", end="")

    if config.i != 0:
        print(f" | ERROR= %{error:8.4f}", end="")

    input("     Press [Enter] to show the next iteration")

    if config.i != 0 and error <= config.target_error:
        config.i = 0
        return xi_1

    config.i += 1
    return newton(xi_1)

# Method Two
def false_position(xl, xu, xr_old=0):
    xr = xu - (fn(xu) * (xl - xu)) / (fn(xl) - fn(xu))

    if config.i != 0:
        error = abs((xr - xr_old) / xr) * 100

    print(f"I={config.i:2d} | "
          f"XL={xl:9.4f} | "
          f"F(XL)={fn(xl):9.4f} | "
          f"XU={xu:9.4f} | "
          f"F(XU)={fn(xu):9.4f} | "
          f"XR={xr:9.4f} | "
          f"F(XR)={fn(xr):9.4f}", end="")

    if config.i != 0:
        print(f" | ERROR= %{error:8.4f}", end="")

    input("     Press [Enter] to show the next iteration")

    if config.i != 0 and error <= config.target_error:
        config.i = 0
        return xr

    if fn(xl) * fn(xr) < 0:
        xu = xr
    else:
        xl = xr

    config.i += 1
    return false_position(xl, xu, xr)
def false_position_gui(xl, xu):
    results = []

    xr_old = 0
    config.i = 0

    while True:
        xr = xu - (fn(xu) * (xl - xu)) / (fn(xl) - fn(xu))

        if config.i != 0:
            error = abs((xr - xr_old) / xr) * 100
        else:
            error = None

        line = f"I={config.i} | XL={xl:.4f} | XU={xu:.4f} | XR={xr:.4f}"

        if error is not None:
            line += f" | ERROR= %{error:.4f}"

        results.append(line)

        if error is not None and error <= float(config.target_error):
            break

        if fn(xl) * fn(xr) < 0:
            xu = xr
        else:
            xl = xr

        xr_old = xr
        config.i += 1

    return results

# Method Three
def secant(xi_1, xi):
    xi_2 = xi - (fn(xi) * (xi_1 - xi)) / (fn(xi_1) - fn(xi))

    if config.i != 0:
        error = abs((xi_2 - xi) / xi_2) * 100

    print(f"I={config.i:2d} | "
          f"Xi-1={xi_1:9.4f} | "
          f"F(Xi-1)={fn(xi_1):9.4f} | "
          f"Xi={xi:9.4f} | "
          f"F(Xi)={fn(xi):9.4f}", end="")

    if config.i != 0:
        print(f" | ERROR= %{error:8.4f}", end="")

    input("     Press [Enter] to show the next iteration")

    if config.i != 0 and error <= config.target_error:
        config.i = 0
        return xi_2

    config.i += 1
    return secant(xi, xi_2)

# Method Four
def simple_fixed_point(xi):
    xi_1 = solve(xi)

    if config.i != 0:
        error = abs((xi_1 - xi) / xi_1) * 100

    print(f"I={config.i:2d} | "
          f"Xi={xi:9.4f} | "
          f"Xi+1={xi_1:9.4f} | ", end="")

    if config.i != 0:
        print(f" | ERROR= %{error:8.4f}", end="")

    input("     Press [Enter] to show the next iteration")

    if config.i != 0 and error <= config.target_error:
        config.i = 0
        return xi_1

    config.i += 1
    return simple_fixed_point(xi_1)

# Method Five
def bisection(xl, xu, xr_old=0):
    xr = (xl + xu) / 2

    if config.i != 0:
        error = abs((xr - xr_old) / xr) * 100

    print(f"I={config.i:2d} | "
          f"XL={xl:9.4f} | "
          f"F(XL)={fn(xl):9.4f} | "
          f"XU={xu:9.4f} | "
          f"F(XU)={fn(xu):9.4f} | "
          f"XR={xr:9.4f} | "
          f"F(XR)={fn(xr):9.4f}", end="")

    if config.i != 0:
        print(f" | ERROR= %{error:8.4f}", end="")

    input("     Press [Enter] to show the next iteration")

    if config.i != 0 and error <= config.target_error:
        config.i = 0
        return xr

    if fn(xl) * fn(xr) < 0:
        xu = xr
    else:
        xl = xr

    config.i += 1
    return bisection(xl, xu, xr)

def bisection_gui(xl, xu):
    results = []

    xr_old = 0
    config.i = 0

    while True:
        xr = (xl + xu) / 2

        if config.i != 0:
            error = abs((xr - xr_old) / xr) * 100
        else:
            error = None

        line = f"I={config.i} | XL={xl:.4f} | XU={xu:.4f} | XR={xr:.4f}"

        if error is not None:
            line += f" | ERROR= %{error:.4f}"

        results.append(line)

        if error is not None and error <= float(config.target_error):
            break

        if fn(xl) * fn(xr) < 0:
            xu = xr
        else:
            xl = xr

        xr_old = xr
        config.i += 1

    return results
