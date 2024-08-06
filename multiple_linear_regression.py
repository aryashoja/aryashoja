# implanting vectorisation into linear regression
import numpy as np
x = [[1, 1, 1, 1],
     [2, 2, 2, 2]]
y = [2, 4]
z = [[2, 2, 2, 2],
     [1, 1, 1, 1]]
# note: write a multiple linear regression


def multiple_linear_regression_cost_function(the_question, the_answer, w, b):  
    f = 0
    for i in range(len(the_question)):
        f += (((np.dot(the_question[i], w) + b) - the_answer[i]) ** 2) * (1 / 2 * len(the_question))
    return f


def average(number):
    try:
        output = 0
        number = number
        for i in number:
            output += i
        output = output / len(number)
        return output
    except TypeError:
        return number


def alpha_w(the_question, the_answer, w, b, colum):
    alpha = 0.1
    f = 0
    for i in range(len(the_question)):
        f += (((np.dot(the_question[i], w) + b) - the_answer[i]) * the_question[i][colum]) * (1 / len(the_question))
        print(the_question[i], w, (np.dot(the_question[i], w) + b), the_answer[i], the_question[i][colum])
    f = float("{:.5f}".format(f))
    a = f * alpha
    return a


def alpha_b(the_question, the_answer, w, b):
    alpha = 0.1
    f = 0
    for i in range(len(the_question)):
        f += ((np.dot(the_question[i], w) + b) - the_answer[i]) * (1 / len(the_question))
    f = float("{:.5f}".format(f))
    a = f * alpha
    print(a)
    return a


def multiple_linear_regression_formula(the_question, the_answer):
    f = w1 = b1 = f1 = 1
    b = 0
    w = []
    for i in range(len(the_question[0])):
        w.append(1)
    while f != 0:
        f2 = f1
        f1 = f
        f = multiple_linear_regression_cost_function(the_question, the_answer, w, b)
        w1 = w
        b1 = b
        b2 = b - alpha_b(the_question, the_answer, w, b)
        for i in range(len(w)):
            a = w[i] - alpha_w(the_question, the_answer, w, b, i)
            w.pop(i)
            w.insert(i, float("{:.5f}".format(a)))
        b = float("{:.5f}".format(b2))
        if f == f1 and f1 == f2 and f == f2:
            break
    return w1, b1


def multiple_linear_regression(the_example_question, the_example_answer, the_question):
    the_final_answer = ""
    w, b = multiple_linear_regression_formula(the_example_question, the_example_answer)
    for i in range(len(the_question)):
        vessel = np.dot(the_question[i], w) + b
        the_final_answer += f"({vessel}) "
    return the_final_answer


print(multiple_linear_regression(x, y, z))
