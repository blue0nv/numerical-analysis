import tkinter as tk
import config
import functions

root = tk.Tk()
root.title("Root Finder")
root.geometry("600x500")

tk.Label(root, text="Enter the equation: ").grid(row=0, column=0)
eq_entry = tk.Entry(root)
eq_entry.grid(row=0, column=1)

tk.Label(root, text="Enter the acceptable error percentage: ").grid(row=1, column=0)
error_entry = tk.Entry(root)
error_entry.grid(row=1, column=1)

status_label = tk.Label(root, text="")
status_label.grid(row=1, column=2, padx=50)

def hide_radio():
    radio_frame.grid_forget()
    calculate_btn.grid_forget()
    method_frame.grid_forget()

def confirm():
    eq_text = eq_entry.get()
    config.target_eq = eq_entry.get()
    target_error = error_entry.get()
    config.target_error = error_entry.get()
    is_valid = functions.input_validator(target_error, eq_text, status_label)
    hide_result()

    if is_valid:
        radio_frame.grid(row=5, column=0, columnspan=2, pady=10)
        method_frame.grid(row=7, column=0, columnspan=4, pady=10)
    else:
        hide_radio()

def hide_all_inputs():
    for widget in method_frame.winfo_children():
        widget.grid_forget()

def update_method_inputs():
    hide_all_inputs()
    hide_result()
    another_status_bs.config(text="")

    m = method.get()

    if m in ["bisection", "fp"]:
        xl_label.grid(row=0, column=0)
        xl_entry.grid(row=0, column=1)

        xu_label.grid(row=0, column=2)
        xu_entry.grid(row=0, column=3)

    elif m in ["newton", "secant"]:
        x0_label.grid(row=0, column=0)
        x0_entry.grid(row=0, column=1)

    else:
        x0_label.grid(row=0, column=0)
        x0_entry.grid(row=0, column=1)

        gx_label.grid(row=0, column=2, padx=5)
        gx_entry.grid(row=0, column=3)

    tk.Label(method_frame, text="").grid(row=1, column=0)
    tk.Label(method_frame, text="").grid(row=2, column=0)
    calculate_btn.grid(row=2, column=1, padx=50)
    another_status_bs.grid(row=2, column=2)

def call_method():
    m = method.get()
    match m:
        case "bisection":
                xl = xl_entry.get()
                xu = xu_entry.get()

                if functions.num_validator(xl) and functions.num_validator(xu):
                    another_status_bs.config(text="Valid", fg="green")

                    xl = float(xl)
                    xu = float(xu)

                    if functions.fn(xl) * functions.fn(xu) < 0:

                        result = functions.bisection_gui(xl, xu)

                        result_text.delete("1.0", tk.END)

                        for line in result:
                            result_text.insert(tk.END, line + "\n")

                    else:
                        result_text.delete("1.0", tk.END)
                        result_text.insert(tk.END, "Not solvable")
                    
                    show_result()

                else:
                    another_status_bs.config(text="Invalid", fg="red")
        case "fp":
                xl = xl_entry.get()
                xu = xu_entry.get()

                if functions.num_validator(xl) and functions.num_validator(xu):
                   another_status_bs.config(text="Valid", fg="green")

                   xl = float(xl)
                   xu = float(xu)

                   if functions.fn(xl) * functions.fn(xu) < 0:

                        result = functions.false_position_gui(xl, xu)

                        result_text.delete("1.0", tk.END)

                        for line in result:
                            result_text.insert(tk.END, line + "\n")

                    else:
                        result_text.delete("1.0", tk.END)
                        result_text.insert(tk.END, "Not solvable")
                    show_result()

                else:
                    another_status_bs.config(text="Invalid", fg="red")           

        case "newton" | "secant":
            x0 = x0_entry.get()
            if functions.num_validator(x0):
                another_status_bs.config(text="Valid", fg="green")
                return True
            else:
                another_status_bs.config(text="Invalid", fg="red")
                return False
                
        case "sfp":
            x0 = x0_entry.get()
            gx = gx_entry.get()
            if functions.num_validator(x0) and functions.sfp_input(gx):
                another_status_bs.config(text="Valid", fg="green")
                return True
            else:
                another_status_bs.config(text="Invalid", fg="red")
                return False
    return None

def show_result():
    result_frame.grid(row=12, column=0)
    result_text.grid(row=0, column=0, columnspan=4, pady=10)

def hide_result():
    result_text.delete("1.0", tk.END)
    result_frame.grid_forget()

tk.Label(root, text="").grid(row=3, column=0)
tk.Label(root, text="").grid(row=4, column=0)
tk.Button(root, text="Validate", command=confirm).grid(row=4, column=1)

tk.Label(root, text="").grid(row=5, column=0)
tk.Label(root, text="").grid(row=6, column=0)

method_frame = tk.Frame(root)
method_frame.grid(row=11, column=0, columnspan=4, pady=10)

xl_label = tk.Label(method_frame, text="XL:")
xl_entry = tk.Entry(method_frame)

xu_label = tk.Label(method_frame, text="XU:")
xu_entry = tk.Entry(method_frame)

x0_label = tk.Label(method_frame, text="Initial Guess (X0):")
x0_entry = tk.Entry(method_frame)

gx_label = tk.Label(method_frame, text="Arranged Function (G(X):")
gx_entry = tk.Entry(method_frame)

calculate_btn = tk.Button(method_frame, text="Calculate", command=call_method)
another_status_bs = tk.Label(method_frame, text="")

radio_frame = tk.Frame(root)

method = tk.StringVar()

tk.Radiobutton(radio_frame, text="Bisection", variable=method, value="bisection", command=update_method_inputs)\
    .grid(row=0, column=0, sticky='w')

tk.Radiobutton(radio_frame, text="Secant", variable=method, value="secant", command=update_method_inputs)\
    .grid(row=1, column=0, sticky='w')

tk.Radiobutton(radio_frame, text="Newton", variable=method, value="newton", command=update_method_inputs)\
    .grid(row=2, column=0, sticky='w')

tk.Radiobutton(radio_frame, text="Simple Fixed Point", variable=method, value="sfp", command=update_method_inputs)\
    .grid(row=3, column=0, sticky='w')

tk.Radiobutton(radio_frame, text="False Position", variable=method, value="fp", command=update_method_inputs)\
    .grid(row=4, column=0, sticky='w')

result_frame = tk.Frame(root)
result_text = tk.Text(result_frame, height=10, width=60)

root.mainloop()
