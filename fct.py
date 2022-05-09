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


NUM_MIN = 2500  # Min. number of points generated (inclusive)
NUM_MAX = 6400  # Max. number of points generated (inclusive)


def help() -> str:
    return """
    Usage:
        fct.py (tree|triangle) <action> <filename>
    """


def discretise(fractal_points, m: int):
    num = len(fractal_points)
    if m not in range(num // 100, math.sqrt(num)):
        # Terminate function and signal an error state
        raise ValueError(f"Invalid value for 'm' {m}")

    # 'm' has a correct value here
    # Find a distribution frequency of points
    x_coords = []
    y_coords = []
    for each_point in fractal_points:
        x_coords.append(each_point[0])
        y_coords.append(each_point[1])
    result = np.histogram2d(x_coords, y_coords, bins=m, density=False)
    return result


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
    

def generate(fract: Fractal, num: int) -> None:
    # Raise an exception in case of an invalid value
    if num not in range(NUM_MIN, NUM_MAX + 1):
        # Terminate function and signal an error state
        raise ValueError(
            f"Number of points has to be in the interval <{NUM_MIN}, {NUM_MAX}>"
        )
    
    points = fract.generate_points(num, 0.0, 0.0)
    filename = f"{fract.name}_{num}.txt"
    with open(filename, "w") as f:
        for each_point in points:
            x, y = each_point
            f.write(f"{x},{y}\n")


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
