from my_investigation.salary_by_month import SalaryByMonth
from my_investigation.cpi_by_month import CPIByMonth
from sklearn.linear_model import LinearRegression
from my_investigation.r_f import get_r2, get_f
from sklearn.metrics import mean_squared_error
from my_investigation.datasets.salary import *
from my_investigation.datasets.cpi import *
import matplotlib.pyplot as plt
import datetime

cpi: CPIByMonth = CPIByMonth(datetime.date(2009, 12, 1), cpi_dec_2009)
salary: SalaryByMonth = SalaryByMonth(datetime.date(2009, 12, 1), salary_dec_2009)
cpi.add_vec(np.concatenate((cpi_2010, cpi_2011, cpi_2012, cpi_2013, cpi_2014, cpi_2015, cpi_2016, cpi_2017,
                            cpi_2018), axis=0))
salary.add_vec(np.concatenate((salary_2010, salary_2011, salary_2012, salary_2013, salary_2014, salary_2015,
                               salary_2016, salary_2017, salary_2018), axis=0))
# lr.coef_ -> 1.68944523
# lr: LinearRegression = LinearRegression(fit_intercept=True, normalize=True, copy_X=True)

# lr.coef_ -> 1.49375721
lr: LinearRegression = LinearRegression(fit_intercept=False, normalize=False, copy_X=True)

lr.fit(cpi.cpi.reshape(-1, 1), salary.salary.reshape(-1, 1))
# x_test = np.linspace(100, 600, 21).reshape(-1, 1)
x_test = cpi.cpi.reshape(-1, 1)
y_pred = lr.predict(x_test)
r2 = get_r2(cpi.cpi, salary.salary)
f = get_f(r2, np.alen(cpi.cpi), 2)

# Observed vs predict
fig = plt.figure(figsize=(30.0, 10.8))
plt.plot(cpi.cpi, salary.salary, '-', linewidth=2, color='green', label='Empirical data')
plt.plot(cpi.cpi, salary.salary, 'o', linewidth=6, color='red')
plt.plot(x_test, y_pred, '--', linewidth=4, color='blue', label='Predict data')
plt.grid(True)
plt.title('CPI versus Salary')
plt.ylabel('Salary (Percentage)')
plt.xlabel('CPI (Percentage)')
plt.legend(bbox_to_anchor=(0.15, 0.8), fontsize='xx-large')
plt.text(100, 630, f"R^2 = {np.round(lr.score(x_test, salary.salary.reshape(-1,1)), decimals=4)}", fontsize=20)
# https://en.wikipedia.org/wiki/Mean_squared_error
plt.text(100, 585, f"Mean squared error = "
                   f"{np.round(mean_squared_error(salary.salary.reshape(-1,1), y_pred), decimals=4)}", fontsize=20)
plt.text(100, 440, f"My calculations:\nR^2 = {np.round(r2, decimals=4)}\nF = {np.round(f ,decimals=4)}", fontsize=20)
plt.xticks(np.linspace(100, 500, 17))
plt.yticks(np.linspace(100, 900, 17))
fig.savefig('predict_cpi_salary.png')
