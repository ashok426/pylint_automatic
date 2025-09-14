"""Tiny demo module to exercise pylint and pass common checks."""

from __future__ import annotations


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


class User:
    """Simple user model with greeting and age helpers."""

    def __init__(self, name: str, age: int = 0) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Return a greeting string."""
        return f"hi {self.name}"

    def is_adult(self) -> bool:
        """Return True if age is 18 or above."""
        return self.age >= 18


def main() -> None:
    """Entry point used when running this file directly."""
    num1 = 1
    num2 = 2
    total = add_numbers(num1, num2)
    print("sum is", total)

    user = User("ashok")
    print(user.greet())

    try:
        _ = 1 / 0  # noqa: PLR2004 (if you use ruff), kept to show handled exception
    except ZeroDivisionError:
        # We deliberately swallow this for the demo; in real code, log it.
        pass


if __name__ == "__main__":
    main()
