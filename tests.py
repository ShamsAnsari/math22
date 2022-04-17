import itertools
from random import randrange

from main import *

def test_cross():

    for i in range(100):
        A = [randrange(-100, 100) for i in range(100)]
        B = [randrange(-100, 100) for i in range(100)]
        if cross(A, B) != list(itertools.product(A, B)):
            return False

    return True

print(test_cross())