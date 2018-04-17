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
    plt.plot(cpi.dates.x_values, cpi.cpi, linewidth=4)
    plt.plot(salary.dates.x_values, salary.salary, linewidth=4)
    plt.grid(True)
    plt.title('Consumer price index and salary')
    plt.ylabel('Percentage')
    plt.xlabel('Dates')
    plt.xticks(cpi.dates.x_values, cpi.dates.x_labels, rotation=45)
    plt.yticks(np.linspace(50, 900, 18))
    plt.legend(('CPI', 'Salary'), bbox_to_anchor=(0.15, 0.8), fontsize='xx-large')
    fig.savefig('cpi_and_salary.png')
    fig.clear()

    # Second figure
    plt.plot(cpi.dates.x_values, salary.salary / cpi.cpi, '-', linewidth=2, color='green')
    plt.plot(cpi.dates.x_values, salary.salary / cpi.cpi, 'o', linewidth=6, color='red')
    plt.grid(True)
    plt.title('Salary percentage / CPI percentage versus dates')
    plt.ylabel('Salary percentage / CPI percentage')
    plt.xlabel('Dates')
    plt.xticks(cpi.dates.x_values, cpi.dates.x_labels, rotation=45)
    plt.yticks(np.linspace(0.8, 2, 25))
    fig.savefig('salary_div_cpi.png')
    fig.clear()

    # Third figure
    plt.plot(cpi.cpi, salary.salary, '-', linewidth=2, color='green')
    plt.plot(cpi.cpi, salary.salary, 'o', linewidth=6, color='red')
    plt.grid(True)
    plt.title('CPI versus Salary')
    plt.ylabel('Salary (Percentage)')
    plt.xlabel('CPI (Percentage)')
    plt.xticks(np.linspace(100, 500, 17))
    plt.yticks(np.linspace(100, 900, 17))
    fig.savefig('cpi_salary.png')
