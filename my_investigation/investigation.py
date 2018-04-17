from dateutil.relativedelta import relativedelta
from abc import ABC, abstractmethod
from collections import namedtuple
import numpy as np
import datetime


class Investigation(ABC):
    Dates = namedtuple('Dates', ['x_values', 'x_labels'])

    @staticmethod
    def _get_dates(first_month: datetime.date, months_amount: int) -> namedtuple:
        Investigation._check_dtype(first_month, datetime.date)
        Investigation._check_dtype(months_amount, int)
        x_values: list = [first_month + relativedelta(months=i) for i in range(months_amount)]
        x_labels: list = [datetime.datetime.strftime(first_month + relativedelta(months=i), '%b %Y') for i in
                          range(months_amount)]

        return Investigation.Dates(x_values, x_labels)

    @staticmethod
    def _check_dtype(value: object, expected_type: type) -> None:
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected type '{expected_type.__name__}', got '{type(value).__name__}' instead.")

    @abstractmethod
    def add_vec(self, vec: np.ndarray) -> None:
        pass

    @abstractmethod
    def add_scalar(self, val: np.float64) -> None:
        pass
