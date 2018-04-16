from my_investigation.investigation import Investigation
from collections import namedtuple
import numpy as np
import datetime


class SalaryByMonth(Investigation):
    """
    Middle salary by month in percentage related to December 2009.
    """

    # Threshold and division factor
    D: np.float64 = np.float64(10000)

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
        self.__first_month_val: np.float64 = first_month_val if first_month_val < self.D else first_month_val / self.D
        self.__salary_vec: np.ndarray = np.array([100], dtype=np.float64)

    @property
    def salary(self) -> np.ndarray:
        """
        Make a copy of salary vector and returns it.
        :return: numpy ndarray.
        """
        return self.__salary_vec.copy()

    @property
    def x(self) -> namedtuple:
        """
        Return x values and x labels inside 'X' namedtuple.
        :return: 'X' namedtuple.
        """
        return self._get_x(self.__first_month, np.alen(self.__salary_vec))

    def add_vec(self, vec: np.ndarray) -> None:
        """
        Check data type.
        Vector processing:
            1) Divide vector's values by 10000 if they are larger than 10000 (Emulation of the denomination).
            2) Convert data into percentage view related to first date.
            2) Concatenate previous and current vector.
        :raises TypeError: if got unexpected data type.
        :param vec: numpy ndarray in appropriate format.
        :return: void.
        """
        self._check_dtype(vec, np.ndarray)
        vec = vec.copy()
        for i in range(np.alen(vec)):
            vec[i] = vec[i] if vec[i] < self.D else vec[i] / self.D
        # Transferring data into percentage
        vec = vec / self.__first_month_val * 100
        self.__salary_vec = np.concatenate((self.__salary_vec, vec), axis=0)

    def add_scalar(self, scalar: np.float64) -> None:
        """
        Check data type.
        Scalar processing:
            1) Divide scalar value by 10000 if it is larger than 10000 (Emulation of the denomination).
            2) Convert data into percentage view related to first date.
            3) Append scalar value into salary vector.
        :raises TypeError: if got unexpected data type.
        :param scalar: numpy float64 in appropriate format.
        :return: void.
        """
        self._check_dtype(scalar, np.float64)
        scalar = scalar if scalar < self.D else scalar / self.D
        scalar = scalar / self.__first_month_val * 100
        self.__salary_vec = np.append(self.__salary_vec, scalar)
