def readFile():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    #content = [x.strip() for x in content]
    data = []
    for i in range(len(content)):
        split_line = content[i].split()
        point = []
        point = [float(split_line[0]), float(split_line[1]), float(split_line[2])]
        data.append(point)
    return data


def plot(x_values, y_values):
    plt.plot(x_values,y_values, '-b', markersize = 1)
    plt.xlabel(r'$\tau$')
    #plt.ylabel(r'$\omega$')
    plt.ylabel('Average Mutual Information')
    #plt.ylabel('Average Mutual Information')
    plt.savefig('problem3fnn.png')
    plt.clf()
