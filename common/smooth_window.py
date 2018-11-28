import numpy as np


def smooth(arr: np.ndarray, window_len: int = 11, window: str = 'hanning') -> np.ndarray:
    """
    Smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.

    input:
        x: the input signal
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal

    see also:
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter
    """

    assert arr.ndim == 1, "Smooth only accepts 1 dimension arrays"
    assert arr.size > window_len, "Input vector needs to be bigger than window size"
    assert window_len > 3, "Window length < 3. Nothing to do"
    assert window in ['flat', 'hanning', 'hamming', 'bartlett',
                      'blackman'], "Window should be 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"

    s = np.r_[arr[window_len - 1:0:-1], arr, arr[-2:-window_len - 1:-1]]

    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = eval('np.{}(window_len)'.format(window))

    y = np.convolve(w / w.sum(), s, mode='valid')
    return y[np.int(np.ceil((window_len / 2 - 1))):-np.int(np.floor((window_len / 2)))]


def get_odd_window_len_as_percent_from_arr_len(arr: np.ndarray, percent: np.double) -> np.int:
    prn: np.double = percent / np.double(100)
    l: np.int = np.int(np.ceil(np.alen(arr) * prn))
    return l if l % 2 == 1 else l - 1
