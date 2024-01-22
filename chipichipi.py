
try:
    try:
        print("Begin")
        print(l[10])
        print(10/0)
        print("End")
    except NameError:
        print("Error Name")
    except ZeroDivisionError:
        print("Div zero")
    except (indexError, TypeError) as error:
        print("Fatal error:", error)
except:
    print("Fatal Error!")
finally:
    print("Save Data")

    class MyTypeError(Exception):
        def __init__(self, var=None):
            self.var = var
        def __str__(self):
            return f"Type [var] is {type(self.var)}"



def checker(st):
    if type(st) != str:
        raise TypeError(f"Type [st] is {type(st)}!!")
    else:
        return st
var1 = Mama
var2 = 10.3
try:
    print(checker(var2))
except MyTypeError as error:
    print(error)