import math
import random

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


    def discretize(self, fractal_points, m):
        num = len(fractal_points)
        if m not in range(num // 100, math.sqrt(num)):
            # Terminate function and signal an error state
            raise ValueError(f"Invalid value for 'm' {m}")

        # 'm' has a correct value here
        # Find a distribution frequency of points
        result = np.zeros(m)  # At the beginning, no points processed
        for point in fractal_points:
            x_bin = point[0] / m   # X coord of bin
            y_bin = point[1] / m   # Y coord of bin
            result[x_bin, y_bin] += 1
            # TODO Check for index errors!
        return result


    
