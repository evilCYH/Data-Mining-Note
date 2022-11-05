# -*- encoding: utf-8 -*-",
"""
@Author          :   陈宇宏
@Class           :   信管2003
@Student Number  :   202011239
"""

from pulp import *

def getresult(c, con):
    prob = LpProblem('myPro', LpMaximize)
    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)
    x3 = LpVariable("x3", lowBound=0)
    x4 = LpVariable("x4", lowBound=0)
    x5 = LpVariable("x5", lowBound=0)
    x6 = LpVariable("x6", lowBound=0)
    x7 = LpVariable("x7", lowBound=0)
    x8 = LpVariable("x8", lowBound=0)
    x9 = LpVariable("x9", lowBound=0)
    X = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
    z = 0
    for i in range(len(X)):
        z += X[i] * c[i]
    prob += z
    prob += x1 + x2 + x3 <= con[0]
    prob += x4 + x5 + x6 <= con[1]
    prob += x7 + x8 + x9 <= con[2]
    prob += 0.152 * x1 + 0.17 * x2 + 0.185 * x3 + 0.32 * x4 + 0.41 * x5 + 0.54 * x6 + 0.6 * x7 + 0.745 * x8 + 0.86 * x9 <= \
            con[3]
    prob += x3 <= con[4]
    prob += x6 <= con[5]
    prob += 0.03 * (x1 + x2 + x3) + 0.03 * 1.5 * (x4 + x5 + x6) + 0.08 * 3 * (x7 + x8 + x9) <= con[6]
    prob += 0.00456 * x1 + 0.0051 * x2 + 0.00555 * x3 + 0.0096 * x4 + 0.0123 * x5 + 0.0162 * x6 + 0.048 * x7 + 0.0596 * x8 + 0.0688 * x9 <= \
            con[7]
    # print('确认线性规划是否有解:', prob)
    status = prob.solve()
    print('Z最大值为:', value(prob.objective))
    for i in prob.variables():
        print(i.name + "=" + str(i.varValue))


if __name__ == '__main__':
    c = [0.18 * 0.06, 0.21 * 0.07, 0.23 * 0.1, 0.38 * 0.07, 0.48 * 0.06, 0.65 * 0.08, 0.82 * 0.06, 0.88 * 0.06,
         0.92 * 0.06]
    con = [50000, 60000, 10000, 20000, 20000, 22000, 3000, 1600]
    getresult(c, con)
