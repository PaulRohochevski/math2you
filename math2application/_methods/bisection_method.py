from typing import Tuple


class BisectionMethod(object):

    @staticmethod
    def calculate(func, interval: Tuple[int or float, int or float], epsilon: float) -> Tuple[float, int]:
        # Interval values
        a, b = interval

        if func(a) * func(b) > 0:
            raise ValueError("No roots found for function [{}] on INTERVAL {}".format(func, interval))

        else:
            midpoint: float = None
            cnt: int = 0

            while abs(a - b) >= epsilon:
                midpoint = (a + b) / 2.

                if func(a) * func(midpoint) > 0:
                    a = midpoint

                else:
                    b = midpoint

                cnt += 1

            return midpoint, cnt


if __name__ == '__main__':
    FUNC = lambda x: x ** 2 - 7
    INTERVAL = (-1, 3)
    EPSILON = 0.0001

    res = BisectionMethod.calculate(FUNC, INTERVAL, EPSILON)
    print(res)  # -> (2.6456298828125, 15)
