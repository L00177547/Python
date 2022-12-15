my_string = "global"


def my_function():
    global my_string
    print(f"At the moment, my_string is: {my_string}")
    my_string = "mangled!"


my_function()
print(f"Now the global value of my_string is: {my_string}")
