import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x,y):

    #number of points
    n= np.size(x)

    #mean of x and y
    m_x, m_y = np.mean(x),np.mean(y)

    #calculate cross-deviation and deviation of x
    xy = np.sum(y*x) - n*m_y*m_x
    xx = np.sum(x*x) - n*m_x*m_x

    #regression coefficients
    b1 = xy/xx
    b0 = m_y - b1 * m_x

    return(b0,b1)


def regression_line(x,y,b):

    #plotting actual points as scatter plot
    plt.scatter(x,y,color = "b",marker = "o",s = 10)

    #predicted response
    y_pred = b[0] + b[1] * x

    #plotting regression line
    plt.plot(x,y_pred,color = "g")

    #label
    plt.xlabel('age')
    plt.ylabel('Population having mobile')

    #funtion to show plot
    plt.show()


def main():
    #observation
    x = np.array(([10,20,30,40,50,60,70,80,90,100]))
    y = np.array(([40,80,90,82,65,50,5,30,15,5]))

    #est.coef
    b = estimate_coef(x,y)
    print("Estimated coefficients:\nb_0 = {}  \
        \nb_1 = {}".format(b[0], b[1]))

    #plot regression line
    regression_line(x,y,b)


if __name__ == "__main__":
    main()



