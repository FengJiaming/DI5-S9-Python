import random
import matplotlib.pyplot as plot
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Générer des nombres aléatoires
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    print(random_list)
    return random_list


if __name__ == '__main__':
    numbersRed = random_int_list(-1, -100, 10)
    numbersBlue = random_int_list(1, 100, 10)

    # Générer un tableau en indice
    x = []
    for i in range(10):
        x.append(i)

    # Afficher la courbe de ces données dans une fenêtre matplotlib
    fig = plot.figure()

    # Définir les propriétés de l'axe
    ax = plot.gca()  # gca=get current axis
    ax.spines['bottom'].set_position(('data',0)) #The center point is at (0,0)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plot.plot(x, numbersRed, label='Red', color = 'red')
    plot.plot(x, numbersBlue, label='Blue', color = 'blue')    #,linestyle='--'

    # Modifier les noms des axes,
    plot.ylabel("Nombres aléatoires")
    plot.title("Courbe")

    # Tag values
    for x1, y1 in zip(x, numbersRed):
        plot.text(x1 - 0.2, y1 - 0.05, '%d' % y1, ha='center', va='bottom')
    for x2, y2 in zip(x, numbersBlue):
        plot.text(x2 - 0.2, y2 - 0.05, '%d' % y2, ha='center', va='bottom')

    # Ignore xticks
    plot.xticks(())

    # Legend
    plot.legend(loc='best')

    # Annotation
    x0=4
    y0=numbersRed[4]
    plot.scatter(x0,y0,s=50,color='b')
    plot.plot([x0,x0],[y0,0],'k--',lw=2.5)
    plot.annotate(r'$Random 4 =%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

    plot.show()

    # Histogramme
    plot.ylabel("Nombres aléatoires")
    plot.title("Histogramme")

    plot.bar(x, numbersRed, facecolor='red',edgecolor='white')
    plot.bar(x, numbersBlue, facecolor='blue', edgecolor='white')

    # Tag values
    for x1, y1 in zip(x, numbersRed):
        plot.text(x1 - 0.2, y1 - 0.05, '%d' % y1, ha='center', va='bottom')
    for x2, y2 in zip(x, numbersBlue):
        plot.text(x2 - 0.2, y2 - 0.05, '%d' % y2, ha='center', va='bottom')

    plot.show()

    # Camembert
    plot.title('Camembert')
    data = [1, 2, 3, 4, 5]
    text = ['A', 'B', 'C', 'D', 'E']
    plot.pie(data, labels = text, colors = ['red', 'green', 'yellow', 'blue', 'pink'], explode = [0, 0.2, 0, 0, 0], autopct = '%1.1f%%', startangle=90, pctdistance = 0.7, labeldistance = 0.4, shadow = True)

    plot.show()

    # Afficher une surface 2D dans un espace 3D
    fig = plot.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plot.show()