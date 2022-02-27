#!/usr/bin/env python
# coding: utf-8

import random
from random import seed, randint
import numpy

def monty(prizedoor, selected, change=False):
    assert prizedoor < 3
    assert prizedoor >= 0

    # Sunucu keçi olan kapılardan birini açar
    openeddr = next(i for i in range(3) if i != selected and i != prizedoor)

    # Oyuncu seçimini değiştirirse
    if change:
        selected = next(i for i in range(3) if i != selected and i != openeddr)

    # Oyuncu seçimi değiştimezse
    return selected == prizedoor


if __name__ == '__main__':
    randgame = numpy.random.randint(0,3, 1000*1000*1)

    winningdoors = [d for d in  randgame if monty(1, d)]
    print("Percentage without changing choice: ", len(winningdoors) / len(randgame))

    winningdoors = [d for d in  randgame if monty(1, d, change=True)]
    print("Percentage while changing choice: ", len(winningdoors) / len(randgame))




