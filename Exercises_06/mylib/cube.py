cube_text = "Yo, time to cube stuff!"


def cube(x):
    return x * x * x


if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")
    print(cube(10))
else:
    print(f"This module is called {__name__} and is being called by another script")

