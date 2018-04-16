import numpy as np
from line_profiler import LineProfiler

"""
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    22                                           def contains_duplicates(vec: np.ndarray) -> bool:
    23         1         11.0     11.0      0.0      vec_len: int = np.alen(vec)
    24                                           
    25     10000      10579.0      1.1      0.0      for i in range(vec_len - 1):
    26      9999      14271.0      1.4      0.0          i_scalar = vec[i]
    27  50004999   45611617.0      0.9     42.6          for j in range(i + 1, vec_len):
    28  49995000   61541735.0      1.2     57.4              if i_scalar == vec[j]:
    29                                                           return True
    30                                           
    31         1          2.0      2.0      0.0      return False
"""

"""
O(N*(N/2))
"""


def contains_duplicates(vec: np.ndarray) -> bool:
    vec_len: int = np.alen(vec)

    for i in range(vec_len - 1):
        i_scalar = vec[i]
        for j in range(i + 1, vec_len):
            if i_scalar == vec[j]:
                return True

    return False


if __name__ == '__main__':
    vec = np.arange(1, 10001)

    p = LineProfiler(contains_duplicates)
    p.enable()

    # %time -> Wall time: 6.5 s
    contains_duplicates(vec)
    p.print_stats()
