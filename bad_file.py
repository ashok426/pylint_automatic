# This module intentionally has style issues to test pylint.

def add_numbers(a, b):
    # Missing docstring, non-typed params/return, prints instead of returning
    c = a + b
    print("sum is", c)


class user:  # class name should be CapWords (Invalid name "user")
    def __init__(self, name, age=0):
        self.Name = name  # attribute name should be snake_case
        self.age = age

    def greet(self):
        print("hi " + self.Name)


def main():
    x = 1  # could be const, unused return from add_numbers
    y = 2
    add_numbers(x, y)
    u = user("ashok")
    u.greet()
    try:
        1 / 0
    except:  # bare except (should catch specific exceptions)
        pass


if __name__ == "__main__":
    main()
