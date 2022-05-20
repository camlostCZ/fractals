# Example: fct.py tree generate 4000
# Usage:   See help() bellow

"""
fct.py

Tool which can generate one of several fractals based on
command line arguments.

See help() for usage (or run the tool without any arguments).

Requires: Python 3.10+ ('match case' feature)
"""

import re
import sys

import matplotlib.pyplot as plt

from sierpinski import SierpinskiTriangle
from tree import FractalTree

# Cmdline argument translation map
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

    ... or:
        fct.py encode <filename>              Encode points previously saved to a file
        fct.py visualise <filename>           Visualise previously saved points
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
    """
    Plot visual representation of a previously saved fractal
    and save it as a PNG file.

    Args:
        filename (str): Filename with generated points.
    """
    points = load_points(filename)
    x, y = zip(*points)
    plt.plot(x, y, "b.")
    img_filename = re.sub(r"\.[^.]+$", ".png", filename)
    plt.savefig(fname=img_filename, format="png")
    print(f"Fractal saved to {img_filename}.")


def encode(filename: str) -> None:
    """
    Read content of `filename`, replace all zeroes with a space
    and all other values with "X" (creating some ASCII art fractal
    image).
    Save the result to file named "*_encoded.txt" 
    ("sample_discret.txt" -> "sample_encoded.txt").

    Args:
        filename (str): Source file name
    """
    output_filename = re.sub(r"_discret\.[^.]+$", "_encoded.txt", filename)
    with open(output_filename, "w") as fw, open(filename) as fr:
        for each_line in fr:
            row = each_line.split(',')
            output_line = ""
            for item in row:
                # Replace all 0s with " ", other values with "X"
                ch = " " if item == "0" else "X"
                output_line += ch
            fw.write(output_line + "\n")
    print("Fractal data saved to {output_filename}.")


def main() -> None:
    print("Fractals")
    try:
        # Simple command line parser
        match sys.argv:
            case [_, fractal, "generate", number] if (
                number.isdecimal() 
                and fractal in FRACTAL_MAP.keys()):
                fr = FRACTAL_MAP[fractal]()
                fr.generate(int(number))
            case [_, fractal, "discretise", number, bins] if (
                number.isdecimal() 
                and bins.isdecimal() 
                and fractal in FRACTAL_MAP.keys()):
                fr = FRACTAL_MAP[fractal]()
                points = fr.generate(int(number))
                fr.discretise(points, int(bins))
            case [_, "encode", filename]:
                encode(filename)
            case [_, "visualise", filename]:
                visualise(filename)
            case _:
                print("Error: Invalid arguments.\n")
                print(help())
    except KeyError:
        print("Error: Invalid fractal name used.\n", file=sys.stderr)
        print(help())
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
    except ValueError as e:
        print(e, file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
