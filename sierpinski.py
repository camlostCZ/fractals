from fractal import Fractal


class SierpinskiTriangle(Fractal):
    IFS_ARGS = [
        (0.5, 0, 0, 0.5, 1, 1),
        (0.5, 0, 0, 0.5, 1, 50),
        (0.5, 0, 0, 0.5, 50, 50)
    ]


    def __init__(self) -> None:
        self.name = "SierpinskiTriangle"


    def transformation(self, pct, point):
        idx_ifs = 2
        if pct <= 33:
            idx_ifx = 0
        elif pct <= 66:
            idx_ifs = 1

        a, b, c, d, e, f = SierpinskiTriangle.IFS_ARGS[idx_ifs]
        x_next = a * point[0] + b * point[1] + e
        y_next = c * point[0] + d * point[1] + f
        # Return triplet: x_next, y_next, method_used
        return (x_next, y_next, idx_ifs + 1)
