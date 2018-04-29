from dateutil.relativedelta import relativedelta
from abc import ABC, abstractmethod
from collections import namedtuple
import numpy as np
import datetime


class AInvestigation(ABC):
    Dates = namedtuple('Dates', ['x_values', 'x_labels'])

    @staticmethod
    def _get_dates_range(start_date: datetime.date, data_points_amount: int, by: str = 'months',
                         fmt: str = '%b %Y') -> namedtuple:
        AInvestigation._check_dtype(start_date, datetime.date)
        AInvestigation._check_dtype(data_points_amount, int)
        AInvestigation._check_dtype(by, str)
        AInvestigation._check_dtype(fmt, str)

        x_values: list = eval(f"[start_date + relativedelta({by}=i) for i in range(data_points_amount)]")
        x_labels: list = [datetime.datetime.strftime(i, fmt) for i in x_values]

        return AInvestigation.Dates(x_values, x_labels)

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
