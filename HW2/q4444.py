# %matplotlib inline
import matplotlib.pyplot as plt
import math


def coslst(x):
    return -math.sin(x)


def cosct(x, h):
    return (math.cos(x + h) - math.cos(x - h)) / (2 * h)


def cosfw(x, h):
    return (math.cos(x + h) - math.cos(x)) / h


num = [0.1, 1, 100]
x = []
linestylefw = [['r', '-'],  ['g', '-']['b', '-']]
linestylef = [ ['r', '--'], ['g', '--'],  ['b', '--']]
for i in range(1, 17):
    x.append(i)
errct = []
errfw = []
for k in range(0, 3):
    for i in num:
        for j in x:
            m = 10 ** (-j)
            err1 = abs(cosct(i, m) - coslst(i))
            rel1 = err1 / abs(coslst(i))
            err2 = abs(cosfw(i, m) - coslst(i))
            rel2 = err2 / abs(coslst(i))
            ref1 = math.log10(rel1)
            ref2 = math.log10(rel2)
            errct.append(ref1)
            errfw.append(ref2)
        plt.plot(x, errct, color=linestylef[k][0], linestyle=linestylef[k][1], label=str(num[k]) + 'central')
        plt.plot(x, errfw, color=linestylef[k][0], linestyle=linestylef[k][1], label=str(num[k]) + 'forward')
        errct.clear()
        errfw.clear()
plt.legend()
plt.show()