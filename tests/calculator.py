"""
    Basic Calculator using betterpy.
    Testing file.
"""

from betterpython import *


class Test:

    def __init__(self, operation: str, first: int, second: int) -> None:
        """Testing class for Betterpy."""

        self.first = int(first)
        self.second = int(second)

        def raise_bad_operation() -> None:
            raise ValueError('Bad operation was provided. The only possible values is add/sub/mul/div.')

        switch(operation, {
            'add': self.addition,
            'sub': self.subtraction,
            'mul': self.multiplie,
            'div': self.divide,
            Else: raise_bad_operation
        })

    def addition(self) -> None:
        result = self.first + self.second
        self.insert_solution('+', result)

    def subtraction(self) -> None:
        result = self.first - self.second
        self.insert_solution('-', result)

    def multiplie(self) -> None:
        result = self.first * self.second
        self.insert_solution('x', result)

    def divide(self) -> None:
        result = self.first / self.second
        self.insert_solution('/', result)

    def insert_solution(self, symbol: str, result: int) -> None:
        print(self.first, symbol, self.second, '=', result)


def main() -> None:
    Test(*(arguments[1:]))

if ismain(__name__):
    main()
