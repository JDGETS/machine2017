#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests all the digital outputs
Arguments: gpio01

"""

import sys
import time

import pigpio


def activatePoleClimber(pi):
    print "Activate Climber"
    pi.write(5, 1)
    time.sleep(5)
    pi.write(5, 0)
    pi.close()


def activateAscBalle(pi):
    print "Activate Balle"
    pi.write(6, 1)
    time.sleep(5)
    pi.write(6, 0)
    pi.close()


def activateAimant(pi):
    print "Activate Aimant"
    pi.write(13, 1)
    time.sleep(5)
    pi.write(13, 0)
    pi.close()

def activateMoteurGauche(pi):
    print "Activate Mot Gauche"
    pi.write(20, 1)
    time.sleep(5)
    pi.write(20, 0)
    pi.close()

def activateMoteurDroit(pi):
    print "Activate Mot Droit"
    pi.write(21, 1)
    time.sleep(5)
    pi.write(21, 0)
    pi.close()


def main(pi, argv):
    print argv
    dispatcher = {'gpio5': activatePoleClimber,
                  'gpio6': activateAscBalle,
                  'gpio13': activateAimant,
                  'gpio20': activateMoteurGauche,
                  'gpio21': activateMoteurDroit}

    dispatcher[argv[0]](pi)


if __name__ == '__main__':
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)#!/usr/bin/python
    pi = pigpio.pi()
    main(pi, sys.argv[1:])

