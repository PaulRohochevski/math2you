from my_investigation.salary_by_month import SalaryByMonth
from my_investigation.cpi_by_month import CPIByMonth
from my_investigation.datasets.salary import *
from my_investigation.datasets.cpi import *
import matplotlib.pyplot as plt
import datetime

if __name__ == '__main__':
    cpi: CPIByMonth = CPIByMonth(datetime.date(2009, 12, 1), cpi_dec_2009)
    salary: SalaryByMonth = SalaryByMonth(datetime.date(2009, 12, 1), salary_dec_2009)
    cpi.add_vec(np.concatenate((cpi_2010, cpi_2011, cpi_2012, cpi_2013, cpi_2014, cpi_2015, cpi_2016, cpi_2017,
                                cpi_2018), axis=0))
    salary.add_vec(np.concatenate((salary_2010, salary_2011, salary_2012, salary_2013, salary_2014, salary_2015,
                                   salary_2016, salary_2017, salary_2018), axis=0))

    # First figure
    fig = plt.figure(figsize=(30.0, 10.8))
    fig.gca()
    plt.plot(cpi.x.x_values, cpi.cpi, linewidth=4)
    plt.plot(salary.x.x_values, salary.salary, linewidth=4)
    plt.grid(True)
    plt.title('Consumer price index and salary')
    plt.ylabel('Percentage')
    plt.xlabel('Dates')
    plt.xticks(cpi.x.x_values, cpi.x.x_labels, rotation=45)
    plt.yticks(np.linspace(50, 900, 18))
    plt.legend(('CPI', 'Salary'), bbox_to_anchor=(0.15, 0.8), fontsize='xx-large')
    fig.savefig('cpi_and_salary.png')
    fig.clear()

    # Second figure
    plt.plot(cpi.x.x_values, salary.salary / cpi.cpi, '-', linewidth=2, color='green')
    plt.plot(cpi.x.x_values, salary.salary / cpi.cpi, 'o', linewidth=6, color='red')
    plt.grid(True)
    plt.title('Salary versus consumer price index')
    plt.ylabel('Salary percentage / CPI percentage')
    plt.xlabel('Dates')
    plt.xticks(cpi.x.x_values, cpi.x.x_labels, rotation=45)
    plt.yticks(np.linspace(0.8, 2, 25))
    fig.savefig('salary_div_cpi.png')

    # Statistics
    y: np.ndarray = salary.salary / cpi.cpi
    n: int = np.alen(y)
    x: np.ndarray = np.linspace(1, n, n).astype(dtype=np.int32)

    sum_x: np.int32 = np.sum(x)
    sum_x_pow2: np.int32 = np.power(x, 2).sum()
    sum_x_pow3: np.int32 = np.power(x, 3).sum()
    sum_x_pow4: np.int32 = np.power(x, 4).sum()

    sum_y: np.float64 = y.sum()
    sum_y_pow2: np.float64 = np.power(y, 2).sum()
    sum_y_pow3: np.float64 = np.power(y, 3).sum()
    sum_y_pow4: np.float64 = np.power(y, 4).sum()

    sum_xy: np.float64 = np.sum(x * y)
    sum_x_pow2_y: np.float64 = np.sum(np.power(x, 2) * y)

    vec_det: np.ndarray = np.array([[n, sum_x], [sum_x, sum_x_pow2]])
    vec_det1: np.ndarray = np.array([[sum_y, sum_x], [sum_xy, sum_x_pow2]])
    vec_det2: np.ndarray = np.array([[n, sum_y], [sum_x, sum_xy]])
    det = np.linalg.det([vec_det, vec_det1, vec_det2])

    alpha0 = det[1] / det[0]
    alpha1 = det[2] / det[0]

    delta_x = np.sqrt(sum_x_pow2 / n - np.power(sum_x / n, 2))
    delta_y = np.sqrt(sum_y_pow2 / n - np.power(sum_y / n, 2))

    R_xy = (sum_xy / n - sum_x / n * sum_y / n) / delta_x * delta_y

    F_obs = (np.power(R_xy, 2) * (n - 1 - 1)) / 1 - np.power(R_xy, 2)

    vec2_det: np.ndarray = np.array([[n, sum_x, sum_x_pow2],
                                     [sum_x, sum_x_pow2, sum_x_pow3],
                                     [sum_x_pow2, sum_x_pow3, sum_x_pow4]])

    vec2_det1: np.ndarray = np.array([[sum_y, sum_x, sum_x_pow2],
                                      [sum_xy, sum_x_pow2, sum_x_pow3],
                                      [sum_x_pow2_y, sum_x_pow3, sum_x_pow4]])

    vec2_det2: np.ndarray = np.array([[n, sum_y, sum_x_pow2],
                                     [sum_x, sum_xy, sum_x_pow3],
                                     [sum_x_pow2, sum_x_pow2_y, sum_x_pow4]])

    vec2_det3: np.ndarray = np.array([[n, sum_x, sum_y],
                                     [sum_x, sum_x_pow2, sum_xy],
                                     [sum_x_pow2, sum_x_pow3, sum_x_pow2_y]])

    det2 = np.linalg.det([vec2_det, vec2_det1, vec2_det2, vec2_det3])

    alpha2_0 = det2[1] / det2[0]
    alpha2_1 = det2[2] / det2[0]
    alpha2_2 = det2[3] / det2[0]
