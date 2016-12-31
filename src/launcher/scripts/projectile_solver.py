import numpy as np
from scipy.optimize import *
from math import sin

"""
Retourne la vitesse, l'angle horizontal (teta) et l'angle vertical (phi)
qu'on doit donner au lanceur selon la position x, y du robot et la cible (target) a viser.

Le z est la hauteur ou se trouve le point de lancer de la balle sur le robot
(supposement toujours le meme)
"""
def findvelocityandangle(xRob, yRob, zRob, target):

    # acceleration gravitationnelle
    g = 9.80665

    # 1. trouver l'angle horizontal
    # FYI : droite et gauche selon le dessin sur trello (table modelisation lancer de balle)

    # si on est enligne directement avec la cible
    if yRob - target.y == 0:
        teta = 0

    # si la cible est a droite du robot
    elif yRob - target.y < 0:
        teta = np.arctan(xRob / (target.y - yRob))

        # on convertit l'angle rad en degres
    # si la cible est a gauche du robot
    else:
        # ou utilise arctan et on convertit en degres
        teta = np.arctan(xRob/(yRob - target.y))


    # 2. trouver la distance directe entre le robot et la cible par pythagore
    d = np.sqrt((target.x - xRob)**2 + (target.y - yRob)**2) * 2


    # 3. trouver l'angle vertical du lanceur de balles ainsi que la vitesse a donner a la balle
    # pour que la hauteur maximale de la trajectoire du projectile soit le milieu de l'anneau cible
    # (x sera l'angle et y sera la vitesse)


    # METHODE 1
    # les deux equations a resoudre (resoudre ces deux equations me donne une erreur)
    # equations1 = [
    #  Eq(y**2 * (sin(x)) / (2*g), target.z),
    #  Eq(g * d / y**2, sin(2 * x))]
    #
    # equations = [
    #     Eq(y = -(2*g * (target.z - zRob)/sin(x) ), 0),
    #     Eq(xRob + (y**2 * sin(x) * cos(x) / g), d)]
    #
    # resultats = nsolve(equations, [x, y], [10, 23])  # le [10, 23] est genre un guess...


    # METHODE 2
    # semble fonctionner mais depend beaucoup des valeurs entre crochets dans le fsolve
    def equations(z):
        v0 = z[0]
        phi = z[1]

        F = np.zeros(2)
        F[0] = ((v0**2) * (sin(phi))**2) - (2 * g * (target.z - zRob))
        F[1] = (v0**2 * sin(2*phi)) - (g * d)
        # F[1] = xRob + (v0**2 * sin(phi) * cos(phi) / g) - d
        return F

    # Les valeurs entre crochet representent un guess initial des deux valeurs...
    v0, phi = fsolve(equations, [4, np.pi / 4])

    return v0, phi, teta
