"""
fct.py

Tool which can generate one of several fractals based on
command line arguments.

See help() for usage (or run the tool without any arguments).

Requires: Python 3.10+ ('match case' feature)
"""

import sys

from sierpinski import SierpinskiTriangle
from tree import FractalTree


def help() -> str:
    return """
    Usage:
        fct.py (tree|triangle) <action> <filename>
    """


def main() -> None:
    print("Fractals")
    match sys.argv:
        case [_, "tree", action, filename]:
            print(f"called {action} with {filename}")
            fr = FractalTree()
            pass
        case [_, "triangle", action, filename]:
            print(f"called {action} with {filename}")
            fr = SierpinskiTriangle()
            pass
        case _:
            print("Error: Invalid arguments. \n")
            print(help())
            return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
