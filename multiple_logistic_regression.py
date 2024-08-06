import numpy as n
import math as m
# in this project I want to make a system that wil output the possible outcome as 0 or 1 i .g a patient having cancer
x = [[1, 2, 3, 3],
     [2, 3, 3, 3],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]
y = [0, 0, 1, 1]
z = [[1, 2, 3, 3],
     [2, 3, 3, 3],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]


def average(number):
    try:
        output = 0
        for i in number:
            output += i
        output = output / len(number)
        return output
    except TypeError:
        return number


def loss_function(the_question, the_answer, w, b):
    f = 0
    for i in range(len(the_answer)):
        if the_answer[i] == 1:
            f += (m.log(1 / float("{:.5f}".format(1 + (m.e ** -(n.dot(w, the_question[i]) + b))))))
        elif float("{:.5f}".format(1 / (1 + (m.e ** -(n.dot(w, the_question[i]) + b))))) == 1:
            f += (m.log(1.1 - float("{:.5f}".format(1 / (1 + (m.e ** -(n.dot(w, the_question[i]) + b)))))))
        else:
            f += (m.log(1 - float("{:.5f}".format(1 / (1 + (m.e ** -(n.dot(w, the_question[i]) + b)))))))
    f = f * -(1 / len(the_answer))
    return f


def logistic_alpha_w(the_question, the_answer, w, b, colum):
    f = 0
    for i in range(len(the_answer)):
        f += ((1 / float("{:.5f}".format((1 + (m.e ** -(n.dot(w, the_question[i]) + b)))))) - the_answer[i]) * \
             the_question[i][colum]
    f = f * -(1 / len(the_answer))
    a = 0.1 * f
    return a


def logistic_alpha_b(the_question, the_answer, w, b):
    f = 0
    for i in range(len(the_answer)):
        f += ((1 / float("{:.5f}".format(1 + (m.e ** -(n.dot(w, the_question[i]) + b))))) - the_answer[i])
    f = (f * -(1 / len(the_answer)))
    a_b = 0.1 * f
    return a_b


def logistic_function_gradiant_decent(the_question, the_answer):
    b = 0
    f = f2 = f1 = f3 = 1
    w = []
    for i in range(len(the_question[0])):
        w.append(1)
    while f != 0:
        f4 = f3
        f3 = f2
        f2 = f1
        f1 = f
        f = loss_function(the_question, the_answer, w, b)
        if f != 0:
            b = b - logistic_alpha_b(the_question, the_answer, w, b)
            for i in range(len(w)):
                a = w[i] - logistic_alpha_w(the_question, the_answer, w, b, i)
                w.pop(i)
                w.insert(i, float("{:.5f}".format(a)))
                print(f)
        if f == f1 and f1 == f2 and f2 == f3 and f3 == f4:
            break
    return w, b


def logistic_regression(the_example, the_answer, the_question):
    a = []
    final = 0
    output = ""
    w, b = logistic_function_gradiant_decent(the_example, the_answer)
    q = -b
    for i in range(len(the_question[0])):
        a.append(1)
    for i in w:
        q = q / i
    f = -b / q
    for j in the_question:
        o = n.dot(a, j)
        print(o, f)
        if o >= f:
            final = 1
        if o < f:
            final = 0
        output += str(final) + f"{j}" + ", "
    return output


print(logistic_regression(x, y, z))
