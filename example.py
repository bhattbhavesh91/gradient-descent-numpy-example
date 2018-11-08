import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 10000
    n = float(len(x))
    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        m_calc = -(2/n)*sum(x*(y-y_predicted))
        b_calc = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * m_calc
        b_curr = b_curr - learning_rate * b_calc
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))

x = np.array([1,2,3,4,5])
y = np.array([7,9,11,13,15])

gradient_descent(x,y)
