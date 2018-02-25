import matplotlib.pyplot as plt

pointsList = []
xnList = []
xn1List = []
m = 20
x0 = 0.2
R = 2.5

def iterate(m, x0, n, R):
    pointsList.append(x0)
    #xnList.append(x0)
    def iter(m, xn, n, R):
        if m != n:
            xn1 = (R*xn)*(1-xn)
            pointsList.append(xn1)
            xn1List.append(xn1)
            xnList.append(xn)
            #print(xn1)
            iter(m,xn1, n+1, R)
    iter(m, x0, n, R)

def printPoints(pointsList):
    for i in range(len(pointsList)):
        print(pointsList[i])


def plot_xn_vs_n(pointsList, m):
    n_list = range(0,m+1)
    plt.xlim(-5, m+1)
    maxval = max(pointsList)
    plt.ylim(0, maxval + 0.2*maxval)
    plt.plot(n_list, pointsList, "ob")
    plt.savefig('xn_vs_n.png')
    plt.show()

def plot_xn1_vs_xn(xn1List, xnList):
    plt.xlim(x0 - 0.2*x0, max(xnList)+max(xnList)*0.2)
    plt.ylim(xn1List[0]-0.2*xn1List[0],max(xn1List)+max(xn1List)*0.2)
    plt.plot(xnList, xn1List, "ob")
    plt.savefig('xn1_vs_xn.png')





iterate(m, x0, 0, R)
plot_xn_vs_n(pointsList, m)
plt.clf()
#del xnList[-1]
#printPoints(xnList)
#print("\n")
#printPoints(xn1List)
plot_xn1_vs_xn(xn1List, xnList)
#printPoints(pointsList)
