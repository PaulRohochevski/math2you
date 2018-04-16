import numpy as np


def find_factors(num: np.uint64) -> np.ndarray:
    if not isinstance(num, np.uint64):
        raise TypeError(f"Expected type 'np.uint64', got '{type(num).__name__}' instead.")

    factors_vec: np.ndarray = np.array([], dtype=np.uint64)

    # Constants
    zero: np.uint64 = np.uint64(0)
    one: np.uint64 = np.uint64(1)
    two: np.uint64 = np.uint64(2)

    while np.remainder(num, two) == zero:
        factors_vec = np.append(factors_vec, two)
        num = np.uint64(num / two)

    i: np.uint64 = np.uint64(3)
    max_factor: np.uint64 = np.uint64(np.sqrt(num))

    while i <= max_factor:
        while np.remainder(num, i) == zero:
            factors_vec = np.append(factors_vec, i)
            num = np.uint64(num / i)
            max_factor = np.sqrt(num)

        i += two

    if num > one:
        factors_vec = np.append(factors_vec, num)

    return factors_vec


if __name__ == '__main__':
    # 189 ms ± 1.84 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    a = np.uint64(18446744073709551615)
    # %timeit find_factors(a)

    # 53.7 µs ± 613 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    b = np.uint64(100)
    # %timeit find_factors(b)

    # 90.4 µs ± 1.4 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    c = np.uint64(10000)
    # %timeit find_factors(c)

    # 128 µs ± 717 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    d = np.uint64(1000000)
    # %timeit find_factors(d)

    # 162 µs ± 1.12 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    e = np.uint64(100000000)
    # %timeit find_factors(e)

    # 199 µs ± 4.28 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    f = np.uint64(10000000000)
    # %timeit find_factors(f)

    # 237 µs ± 4.97 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    g = np.uint64(1000000000000)
    # %timeit find_factors(g)

    # 275 µs ± 5.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    h = np.uint64(100000000000000)
    # %timeit find_factors(h)

    # 308 µs ± 6.66 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    i = np.uint64(10000000000000000)
    # %timeit find_factors(i)

    # 345 µs ± 4.96 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    j = np.uint64(1000000000000000000)
    # %timeit find_factors(j)
