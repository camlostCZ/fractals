# Usage:   fct.py (tree|triangle) (generate|discretise|encode|visualise)
# Example: fct.py tree generate 4000

"""
fct.py

Tool which can generate one of several fractals based on
command line arguments.

See help() for usage (or run the tool without any arguments).

Requires: Python 3.10+ ('match case' feature)
"""

import math
import re
import sys

import numpy as np

from fractal import Fractal
from sierpinski import SierpinskiTriangle
from tree import FractalTree

FRACTAL_MAP = {
    "tree": FractalTree,
    "triangle": SierpinskiTriangle
}


def help() -> str:
    return """
    Usage:
        fct.py (tree|triangle) <action>

            action:
                - generate <number>           Generate fractal points
                - discretise <number> <bins>  Discretize fractal points
                - encode                      Encode points previously saved to a file
                - visualise                   Visualise previously saved points
    """


def load_points(filename: str) -> list[tuple[float, float]]:
    """
    Load list of point from a file

    Args:
        filename (str): Source file name

    Returns:
        list[tuple[float, float]]: List of points, i.e. their coordinates
    """
    points = [] # List of fractal points
    with open(filename) as f:
        for each_line in f:
            parts = each_line.split(',')
            if len(parts) != 2:
                # Skip invalid lines silently
                pass
            else:
                x = float(parts[0])
                y = float(parts[1])
                points.append((x, y))
    return points
    

def visualise(filename: str) -> None:
    points = load_points(filename)
    img_filename = re.sub(r"\.[^.]+$", ".png", filename)
    # TODO Draw a fractal using matplotlib.pyplot.scatter()


def encode(filename: str) -> None:
    """
    Read content of `filename`, replace all zeroes with a space
    and all other values with "X" (creating some ASCII art fractal
    image).
    Save the result to file named "*_encoded.txt" 
    ("sample.txt" -> "sample_encoded.txt").

    Args:
        filename (str): Source file name
    """
    output_filename = re.sub(r"\.[^.]+$", "_encoded.txt", filename)
    with open(output_filename, "w") as fw, open(filename) as fr:
        for each_line in fr:
            row = each_line.split(',')
            output_line = ""
            for item in row:
                # Replace all 0s with " ", other values with "X"
                ch = " " if item == "0" else "X"
                output_line += ch
            fw.write(output_line + "\n")


def main() -> None:
    print("Fractals")
    try:
        match sys.argv:
            case [_, fractal, "generate", number] if number.isdecimal():
                fr = FRACTAL_MAP[fractal]()
                fr.generate(int(number))
            case [_, fractal, "discretise", number, bins] if number.isdecimal() and bins.isdecimal():
                fr = FRACTAL_MAP[fractal]()
                points = fr.generate(int(number))
                fr.discretise(points, int(bins))
            case [_, fractal, "encode"]:
                fr = FRACTAL_MAP[fractal]()
            case [_, fractal, "visualise"]:
                fr = FRACTAL_MAP[fractal]()
            case _:
                print("Error: Invalid arguments. \n")
                print(help())
    except KeyError:
        print("Error: Invalid fractal name used.\n", file=sys.stderr)
        print(help())
    except ValueError as e:
        print(e, file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
