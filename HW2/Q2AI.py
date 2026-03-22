import numpy as np
import matplotlib.pyplot as plt


# 定义原函数
def f(x):
    return (1 - np.cos(x)) / (x ** 2)


# 解析求一阶导数
def f_prime(x):
    return (x * np.sin(x) - 2 * (1 - np.cos(x))) / (x ** 3)


# 解析求二阶导数
def f_double_prime(x):
    return (x ** 2 * np.cos(x) - 4 * x * np.sin(x) + 6 - 6 * np.cos(x)) / (x ** 4)


# 中心差分近似二阶导数
def central_difference_second_derivative(func, x, h):
    return (func(x + h) - 2 * func(x) + func(x - h)) / (h ** 2)


# (a) 计算解析二阶导数并代入x = 0.004
x = 0.004
analytical_result = f_double_prime(x)
print(f"解析计算的二阶导数在x = {x}的值: {analytical_result}")

# (b) 绘制双对数图
h_values = np.array([10 ** (-i) for i in range(1, 7)])
errors = []
for h in h_values:
    approx_result = central_difference_second_derivative(f, x, h)
    error = np.abs(approx_result - analytical_result)
    errors.append(error)
plt.loglog(h_values, errors, 'bo-', label='原函数中心差分误差')

# (c) 定义改写后的函数
def f_rewritten(x):
    return 2 * (np.sin(x / 2) ** 2) / (x ** 2)


errors_rewritten = []
for h in h_values:
    approx_result_rewritten = central_difference_second_derivative(f_rewritten, x, h)
    error_rewritten = np.abs(approx_result_rewritten - analytical_result)
    errors_rewritten.append(error_rewritten)
plt.loglog(h_values, errors_rewritten,'ro-', label='改写后函数中心差分误差')

plt.xlabel('log10(h)')
plt.ylabel('log10(绝对误差)')
plt.title('二阶导数中心差分近似的绝对误差')
plt.legend()
plt.show()
