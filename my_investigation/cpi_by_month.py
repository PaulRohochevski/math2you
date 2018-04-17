from my_investigation.investigation import Investigation
from collections import namedtuple
import numpy as np
import datetime


class CPIByMonth(Investigation):
    """
    Consumer price index by month in percentage related to December 2009.
    """

    def __init__(self, first_month: datetime.date, first_month_val: np.float64) -> None:
        """
        Check data types.
        Processing first value.
        :raises TypeError: if got unexpected data type.
        :param first_month: start month (usually the first day of the month).
        :param first_month_val: value related to first month in appropriate format.
        :return: void.
        """
        self._check_dtype(first_month, datetime.date)
        self._check_dtype(first_month_val, np.float64)
        self.__first_month: datetime.date = first_month
        self.__first_month_val: np.float64 = first_month_val
        self.__cpi_vec: np.ndarray = np.array([self.__first_month_val], dtype=np.float64)

    @property
    def cpi(self) -> np.ndarray:
        """
        Make a copy of cpi vector and returns it.
        :return: numpy ndarray.
        """
        return self.__cpi_vec.copy()

    @property
    def dates(self) -> namedtuple:
        """
        Return dates values and dates labels inside 'Dates' namedtuple.
        :return: 'Dates' namedtuple.
        """
        return self._get_dates(self.__first_month, np.alen(self.__cpi_vec))

    def add_vec(self, vec: np.ndarray) -> None:
        """
        Check data type.
        Vector processing:
            1) Divide vector's values by 100.
            2) Insert last value from cpi vector.
            3) Convert data into percentage view related to first value from current vector.
            4) Delete first value from current vector.
            5) Concatenate previous and current vector.
        :raises TypeError: if got unexpected data type.
        :param vec: numpy ndarray in appropriate format.
        :return: void.
        """
        self._check_dtype(vec, np.ndarray)
        vec = vec.copy()
        vec = vec / np.float64(100)
        vec = np.insert(vec, 0, self.__cpi_vec[-1:])
        vec = np.cumprod(vec, axis=0)
        vec = np.delete(vec, 0)
        self.__cpi_vec = np.concatenate((self.__cpi_vec, vec), axis=0)

    def add_scalar(self, scalar: np.float64) -> None:
        """
        Check data type.
        Scalar processing:
            1) Divide scalar value by 100.
            2) Convert data into percentage view related to last value from cpi vector.
            3) Append scalar value into cpi vector.
        :raises TypeError: if got unexpected data type.
        :param scalar: numpy float64 in appropriate format.
        :return: void.
        """
        self._check_dtype(scalar, np.float64)
        scalar = scalar / np.float64(100)
        scalar = self.__cpi_vec[-1:] * scalar
        self.__cpi_vec = np.append(self.__cpi_vec, scalar)
