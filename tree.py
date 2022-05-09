from fractal import Fractal


class FractalTree(Fractal):
    IFS_ARGS = [
        (0, 0, 0, 0.5, 0, 0),
        (0.42, -0.42, 0.42, 0.42, 0, 0.2),
        (0.42, 0.42, -0.42, 0.42, 0, 0.2),
        (0.1, 0, 0, 0.1, 0, 0.2)
    ]


    def __init__(self) -> None:
        self.name = "FractalTree"


    def transformation(self, pct, point):
        idx_ifs = 3
        if pct <= 5:
            idx_ifs = 0
        elif pct <= 0.45:
            idx_ifs = 1
        elif pct <= 0.85:
            idx_ifs = 2

        a, b, c, d, e, f = FractalTree.IFS_ARGS[idx_ifs]
        x_next = a * point[0] + b * point[1] + e
        y_next = c * point[0] + d * point[1] + f
        # Return triplet: x_next, y_next, method_used
        return (x_next, y_next, idx_ifs + 1)
