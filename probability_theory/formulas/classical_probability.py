from _utils.formula import Formula
import numpy as np
from sympy import *

init_session()


class ClassicalProbability(Formula):
    def __init__(self, event: str, m: np.int64, n: np.int64):
        self.__value: np.float64 = m / n
        self.__event: str = event
        self.__m: np.int64 = m
        self.__n: np.int64 = n
        self.__probability_of_event: Symbol = Symbol(f'P({event})')
        self.__m_value: Symbol = Symbol(str(m))
        self.__n_value: Symbol = Symbol(str(n))
        self.__m_symbol: Symbol = Symbol('m')
        self.__n_symbol: Symbol = Symbol('n')

    def formula(self):
        left: Eq = Eq(self.__probability_of_event, self.__m_symbol / self.__n_symbol)
        right: Eq = Eq(self.__m_value / self.__n_value, self.value)
        return Eq(left, right)

    @property
    def value(self):
        return self.__value

    # TODO: Remove???
    def __repr__(self):
        return "ClassicalProbability('{}', np.int64({}), np.int64({}))".format(self.__event, self.__m, self.__n)

if __name__ == '__main__':
    a = ClassicalProbability('A', np.int64(1), np.int64(2))
    repr(a)
