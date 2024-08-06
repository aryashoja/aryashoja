# implanting gradiant decant
x = [1, 2, 3, 4, 5]
y = [4, 8, 12, 16, 20]
z = [1, 2, 3, 4, 5]


def linear_regression_cost_function(the_question, the_answer, weight, bias):
    counter = f = 0
    for i in the_question:
        counter += 1
        counter1 = 1
        for j in the_answer:
            if counter == counter1:
                f += (((i * weight + bias) - j) ** 2) * (1 / (2 * len(x)))
            counter1 += 1
    return f


def alpha_w(the_question, the_answer, w, b):
    counter = f = 0
    a = 0.1
    for i in the_question:
        counter += 1
        counter1 = 1
        for j in the_answer:
            if counter == counter1:
                f += ((i * w + b) - j) * i * (1 / len(x))
            counter1 += 1
    a = f * a
    return a


def alpha_b(the_question, the_answer, w, b):
    counter = f = 0
    a = 0.1
    for i in the_question:
        counter += 1
        counter1 = 1
        for j in the_answer:
            if counter == counter1:
                f += ((i * w + b) - j) * (1 / len(x))
            counter1 += 1
    a = f * a
    return a


def linear_regression_formula(the_question, the_answer):
    counter = 0
    w = b = 0
    f, f1 = linear_regression_cost_function(the_question, the_answer, w, b), 0
    while True:
        w1 = w - alpha_w(the_question, the_answer, w, b)
        b = b - alpha_b(the_question, the_answer, w, b)
        w = w1
        f2 = f1
        f1 = f
        f = linear_regression_cost_function(the_question, the_answer, w, b)
        counter = counter + 1
        if f == f1 and f1 == f2:
            break
    return w, b


def linear_regression(the_example, the_answer, the_question):
    output = ""
    w, b = linear_regression_formula(the_example, the_answer)
    try:
        for i in the_question:
            output += "(" + "{:.2f}".format(float(i) * float(w) + float(b)) + ") "
        return output
    except TypeError:
        output += "(" + "{:.2f}".format(float(the_question) * float(w) + float(b)) + ") "
        return output


print(linear_regression(x, y, z))
