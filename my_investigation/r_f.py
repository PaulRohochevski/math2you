"""
https://ru.wikipedia.org/wiki/F-%D1%82%D0%B5%D1%81%D1%82
"""
import numpy as np


def get_r2(x: np.ndarray, y: np.ndarray) -> np.float64:
    n: int = np.alen(x)

    sum_x: np.int32 = np.sum(x)
    sum_y: np.float64 = np.sum(y)

    x_ = sum_x / n
    y_ = sum_y / n

    xi_x_ = x - x_
    yi_y_ = y - y_

    r_xy = np.sum(xi_x_ * yi_y_) / np.sqrt(np.sum(np.power(xi_x_, 2)) * np.sum(np.power(yi_y_, 2)))

    return np.power(r_xy, 2)


def get_f(r2: np.float64, n: int, k: int) -> np.float64:
    return np.float64((r2 / (k - 1)) / ((1 - r2) / (n - k)))
