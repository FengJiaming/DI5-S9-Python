from Fourmi import *
from parameterParser import *
from matplotlib.image import imsave

if __name__ == '__main__':

    print("La peinture commence")
    # Pour extraire les paramètres dans le fichier de configuration xml
    parser = parameterParser("fourmis.xml")
    fourmis = parser.parseElement()
    iteration = parser.getIteration()

    list_fourmis = []

    for f in fourmis:
        origin_position = np.random.randint(1, width-1, 2)
        orientation = np.random.randint(1, 9)

        colors = f.getElementsByTagName('couleur_deposee')[0]
        colors = colors.childNodes[0].data.split(',')
        for i in range(0, len(colors)):
            colors[i] = int(colors[i].strip())

        scolors = f.getElementsByTagName('couleur_suivi')[0]
        scolors = scolors.childNodes[0].data.split(',')
        for i in range(0, len(scolors)):
            scolors[i] = int(scolors[i].strip())

        proba = f.getElementsByTagName('proba')[0]
        proba = proba.childNodes[0].data.split(',')
        for i in range(0, len(proba)):
            proba[i] = float(proba[i].strip())

        dtype = f.getElementsByTagName('type')[0]
        dtype = int(dtype.childNodes[0].data)

        ps = f.getElementsByTagName('proba_suivi')[0]
        ps = float(ps.childNodes[0].data)

        ant = Fourmi(origin_position, 1, colors, scolors, proba, dtype, ps, orientation)
        list_fourmis.append(ant)

    for i in range(1, iteration):
        for fourmi in list_fourmis:
            fourmi.deplacer()

    imsave('fourmis.png', pic)
    print("Peinture terminée")
