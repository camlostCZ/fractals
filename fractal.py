import random


class Fractal:
    def __init__(self) -> None:
        self.name = "GeneralFractal"


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


    def generate_points(self, num: int, x_start: float, y_start: float):
        """
        Generate a sequence of points of a fractal.

        Args:
            num (int): Number of points in the sequence; has to be in <NUM_MIN, NUM_MAX)
            x_start (float): X coordinate of the starting point
            y_start (float): Y coordinate of the starting point

        Yields:
            tuple(int, int, int): Coordinates and index of transformation used
        """        
        x_next, y_next = (x_start, y_start)
        for i in range(num):
            fortune = random.randint(0, 100)
            x_next, y_next, fn = self.transformation(fortune, (x_next, y_next))
            yield (x_next, y_next, fn)
