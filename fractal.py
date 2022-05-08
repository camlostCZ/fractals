import math
import random
import re

import numpy as np


NUM_MIN = 2500  # Min. number of points generated (inclusive)
NUM_MAX = 6400  # Max. number of points generated (inclusive)


class Fractal:
    def transformation(self, pct, point):
        """
        Compute coordinates of next point based on current 'point'
        and the probability distribution 'pct'.

        Note:
            This general implementation does nothing important.
            Should be overridden in class children.

        Args:
            pct (int): Probability distribution
            point (tuple(int, int)): Point coordinates

        Returns:
            tuple(int, int, int): Coordinates and index of transformation used
        """
        return point + (0, )


    def generate(self, num, x_start, y_start):
        """
        Generate a sequence of points of a fractal.

        Args:
            num (int): Number of points in the sequence; has to be in <NUM_MIN, NUM_MAX)
            x_start (_type_): X coordinate of the starting point
            y_start (_type_): Y coordinate of the starting point

        Raises:
            ValueError: Raised if an invalid 'num' specified

        Yields:
            tuple(int, int, int): Coordinates and index of transformation used
        """
        # Raise an exception in case of an invalid value
        if num not in range(NUM_MIN, NUM_MAX + 1):
            # Terminate function and signal an error state
            raise ValueError(f"Number of points has to be in the interval <{NUM_MIN}, {NUM_MAX}>")
        
        # Now, we can be sure the number is in the interval
        x_next, y_next = (x_start, y_start)
        for i in range(num):
            fortune = random.randint(0, 100)
            x_next, y_next = self.transformation(fortune, (x_next, y_next))
            yield (x_next, y_next, fortune)


    def discretise(self, fractal_points, m: int):
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


    def _load_points(self, filename: str) -> list[tuple[float, float]]:
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
    

    def visualise(self, filename: str) -> None:
        points = self._load_points(filename)
        img_filename = re.sub(r"\.[^.]+$", ".png", filename)
        # TODO Draw a fractal using matplotlib.pyplot.scatter()


    def encode(self, filename: str) -> None:
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
