### I don't think this is anything other than mere guidelines we (the publishers of this) agreed on to implement in this project so we're just doccumenting our thoughts so we can follow the same style of code while working.
> #### *So, in other words if you ever happen to come across this: Basically don't really mind this readme file unless you're thinking of contributing ツ*

---

## **Basic Guidelines**
+ #### Installing SymPy

`SymPy` is a Python library for symbolic mathematics. While you might not really use it, it's already used in the code.<br>
So the thing is, if you don't have the library installed, it will throw an error.<br>
Basically open your IDE terminal, and just write `pip install sympy`.<br>
Or if it for whatever reason doesn't work, try `py -m pip install sympy`.
> If it didn't throw an error, you have `SymPy` already installed -> ignore this.
---

+ #### `global new_eq, i, target_error`

  The whole program probably revolves around these three variables. You will most definitely need them in your function.<br>
  So to avoid any confusion, always insert `global new_eq, i, target_error` at the start of your function.

  ---

+ #### Resetting the iteration counter<br>

    There are several functions which are depending on the `i` variable which is a global one.<br>
    So always make sure to just reset the variable back to zero when you are done to avoid changing the original variable.
  ```
      if i != 0 and error <= target_error:
        i = 0    <------ 
        return xi_1
  ```
  ---
+ #### Functions layout<br>

  Nothing to be said here other than put the functions where they belong, if it's a functions that is gonna be needed for calculations then put it in its section<br>
  If it's a function that is for one of the root finding methods, put it there.

  ---
