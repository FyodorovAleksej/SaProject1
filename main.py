from functools import reduce

import matplotlib.pyplot as plt
import numpy as np

def sumProizv(xCollection, yCollection):
    return reduce(lambda x, y: x + y, [xCollection[i] * yCollection[i] for i in range(0, len(xCollection) if (len(xCollection) <= len(yCollection)) else len(yCollection))])

def sumAll(collection):
    return reduce(lambda x, y: x + y, collection)

def sumQuard(collection):
    return sumAll(map(lambda x: x**2, collection))

if __name__ == "__main__":
    file = open("./data.txt")
    rows = file.readlines()
    rawdata = [i.split(",") for i in rows]
    coordinate1 = [float(i[0]) for i in rawdata]
    coordinate2 = [float(i[2]) for i in rawdata]
    array1 = np.array(coordinate1)
    array2 = np.array(coordinate2)
    file.close()
    correlation = np.corrcoef(coordinate1, coordinate2)[0][1]
    print("correlation = " + str(correlation))
    if 0.91 <= abs(correlation) <= 1.0:
        print("Very strong")
    elif 0.81 <= abs(correlation) <= 0.9:
        print("Strong enough")
    elif 0.65 <= abs(correlation) <= 0.8:
        print("Strong")
    elif 0.45 <= abs(correlation) <= 0.64:
        print("Moderate")
    elif 0.25 <= abs(correlation) <= 0.44:
        print("Weak")
    else:
        print("Very weak")

    if correlation >= 0:
        print("Direct")
    else:
        print("Reverse")

    print("\n------------------\n")
    length = len(coordinate1) if (len(coordinate1) <= len(coordinate2)) else len(coordinate2)
    tStudent = correlation * np.sqrt(length - 2)/np.sqrt(1 - correlation ** 2)
    print("t Student = " + str(tStudent))

    # change to your
    tTabl = 1.9666125

    if (tStudent > tTabl):
        print("t Student > t table - depending is important")
    else:
        print("t Student < t table - depending is unimportant")

    a = (length * sumProizv(coordinate1, coordinate2) - sumAll(coordinate1) * sumAll(coordinate2))/(length * sumQuard(coordinate1) - sumAll(coordinate1)**2)
    b = (sumAll(coordinate2)*sumQuard(coordinate1) - sumAll(coordinate1)*sumProizv(coordinate1, coordinate2))/(length*sumQuard(coordinate1) - sumAll(coordinate1)**2)

    print("A = " + str(a))
    print("B = " + str(b))


    x = coordinate1
    print(x)
    y = [a * i + b for i in x]
    print(y)
    plt.plot(x, y)
    plt.grid(True)
    for i in range(0, length):
        plt.annotate(".", xy=(coordinate1[i], coordinate2[i]))
    plt.savefig('pic_1_5_1', fmt='pdf')
    plt.savefig('pic_1_5_1', fmt='png')
    plt.show()