import math as m
# in this project I want to make a system that wil output the possible outcome as 0 or 1 i .g a patient having cancer
x = [1, 2, 3, 4, 5]
y = [0, 0, 1, 1, 1]
z = [1.5, 4.5, 4, 3, 2.5, 2.4, 20]


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
            f += (m.log(1 / (1 + (m.e ** -(w * the_question[i] + b)))))
        else:
            f += (m.log(1.1 - (1 / (1 + (m.e ** -(w * the_question[i] + b))))))
    f = f * -(1 / len(the_answer))
    return f


def logistic_alpha_w(the_question, the_answer, w, b):
    f = 0
    for i in range(len(the_answer)):
        f += ((1 / (1 + (m.e ** -(w * the_question[i] + b)))) - the_answer[i]) * the_question[i]
    f = float("{:.5f}".format(f * (1 / len(the_answer))))
    a = 2 * f
    return a


def logistic_alpha_b(the_question, the_answer, w, b):
    f = 0
    for i in range(len(the_answer)):
        f += ((1 / (1 + (m.e ** -(w * the_question[i] + b)))) - the_answer[i])
    f = float("{:.5f}".format(f * (1 / len(the_answer))))
    a_b = 2 * f
    return a_b


def logistic_function_gradiant_decent(the_question, the_answer):
    b = 0
    w = f = f2 = f1 = 1
    while f != 0:
        f3 = f2
        f2 = f1
        f1 = f
        f = loss_function(the_question, the_answer, w, b)
        if f != 0:
            w_s = w - logistic_alpha_w(the_question, the_answer, w, b)
            b = b - logistic_alpha_b(the_question, the_answer, w, b)
            w = w_s
        if f == f1 and f1 == f2 and f2 == f3:
            break
    return w, b


def logistic_regression(the_example, the_answer, the_question):
    output = ""
    w, b = logistic_function_gradiant_decent(the_example, the_answer)
    for i in the_question:
        f = -b / w
        if i >= f:
            o = 1
        else:
            o = 0
        output += str(o) + f"({i})" + ", "
    return output


print(logistic_regression(x, y, z))
