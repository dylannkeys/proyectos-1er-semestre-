import random
import string
import sys
import subprocess

def ns(r):
    while r!="n" and r!="s":
        r=input("Escriba solo \'n\' o \'s\' según su opción: ")
    return r 