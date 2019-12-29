import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.misc
from PIL import Image
import sys

##########################  NumPy  #######################
# Créer un tableau de dimension 3 avec un shape de (4, 3, 2)
# remplit avec des nombres aléatoires.
print("--------Numpy--------")
print("Question 1: ")
ran = np.random.rand(4, 3, 2)
print (ran)
# Afficherez les attributs du tableau : ndim, shape, size, dtype, itemsize, data.
print('ndim:', ran.ndim, 'shape:', ran.shape, 'size:', ran.size, 'dtype:', ran.dtype,
      'itemsize:', ran.itemsize, 'data:', ran.data)

# Créer 2 matrices 3x3
# de 0 à 8
print("Question 2: ")
matr_a = np.arange(9).reshape(3,3)
print(matr_a)
# de 2 à 10
matr_b = np.arange(2,11).reshape(3,3)
print(matr_b)
# le produit des 2 matrices (*)
print("Le produit des 2 matrice(*):" )
print(matr_a @ matr_b)
# le produit des 2 matrices (dot)
print("Le produit des 2 matrice(dot):")
print(matr_a.dot(matr_b))
# elementwise product
print("Elementwise product: ")
print(matr_a * matr_b)
# Transposer une matrice
print("Transposer une matrice: ")
print(np.transpose(matr_a))

# Calculer le déterminant et l’inverse d’une matrice.
print("Question 3: ")
a = np.array(([-2,2,-3],[-1,1,3],[2,0,-1]))
print("det= " + str(np.linalg.det(a)))
# Résoudre un système d’équations linéaires.
print("Résoudre un système d’équations linéaires:")
print(np.linalg.inv(a))
# Calculer les valeurs et vecteurs propres d’une matrice.
print("Le valeur propre=" + str(np.linalg.eigvals(a)))
print("Les vecteurs propres:")
print(np.linalg.eigh(a))



##########################  SciPy  #######################
# Approcher un ensemble de points par une courbe

def func(x, a, b, c):
  return a * np.exp(-b * x) + c

print("\n--------SciPy--------")
print("Question 4:")
# Define the data to be fit with some noise
xdata = np.linspace(0, 4, 15)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
print(xdata, ydata)
plt.plot(xdata, ydata, 'b-', label='data')

# Fit for the parameters a, b, c of the function func:
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Lire une image jpeg et afficher l’image originale et réduite en taille.
# ouverture du fichier image
print("Question 5:")
ImageFile = 'flocon-neige.jpg'
try:
  img = Image.open(ImageFile)
except IOError:
  print ('Erreur sur ouverture du fichier ' + ImageFile)
  sys.exit(1)
# affichage des caractéristiques de l'image
print (img.format,img.size, img.mode)
# affichage de l'image
img.show()
original_image = np.array(img)
plt.subplot(211)
plt.imshow(original_image)

i_width = 512
i_height = 288
# Resize the image from 1024 * 576 to 512 * 288
# reduced_image = scipy.misc.resize(original_image, (i_height, i_width))
reduced_image = img.resize((i_width, i_height), Image.ANTIALIAS)
plt.subplot(212)
plt.imshow(reduced_image)
plt.show()