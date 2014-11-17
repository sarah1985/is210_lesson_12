#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
is210 Section 01 Week 12

Bench marking methods

Works Cited:

    The following Pi calculation functions were sourced from the "Captian
    DeadBones Chronicles" blog posting "Computing Pi With Python".

    http://thelivingpearl.com/2013/05/28/computing-pi-with-python/

    Minor changes were made to conform with lesson plan.

"""

import math
from decimal import *
import time
import sys


def stdlib(depth):
    """
    Calculate Pi using the math.pi from Python standard library

    :param depth:
    :return:
    """
    a = Decimal(1.0)
    b = Decimal(1.0 / math.sqrt(2))
    t = Decimal(1.0) / Decimal(4.0)
    p = Decimal(1.0)

    for i in range(depth):
        at = Decimal((a + b) / 2)
        bt = Decimal(math.sqrt(a * b))
        tt = Decimal(t - p * (a - at) ** 2)
        pt = Decimal(2 * p)

        a = at
        b = bt
        t = tt
        p = pt

    pi = (a + b) ** 2 / (4 * t)

    return str(pi)


def bbp(depth):
    """
    Calculate Pi using the Bailey–Borwein–Plouffe formula
    http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula

    :param depth:
    :return:
    """
    pi = Decimal(0)
    k = 0
    while k < depth:
        pi += (Decimal(1) / (16 ** k)) * (
            (Decimal(4) / (8 * k + 1)) -
            (Decimal(2) / (8 * k + 4)) -
            (Decimal(1) / (8 * k + 5)) -
            (Decimal(1) / (8 * k + 6))
        )
        k += 1
    return str(pi)


def bellard(depth):
    """
    New school Pi calculation method discovered in 1997 by Fabrice Bellard in
    1997. Usually clocks in 43% faster than the BBP formula.

    http://en.wikipedia.org/wiki/Bellard%27s_formula

    :param depth:
    :return:
    """
    pi = Decimal(0)
    k = 0
    while k < depth:
        pi += (Decimal(-1) ** k / (1024 ** k)) * (
            Decimal(256) / (10 * k + 1) +
            Decimal(1) / (10 * k + 9) -
            Decimal(64) / (10 * k + 3) -
            Decimal(32) / (4 * k + 1) -
            Decimal(4) / (10 * k + 5) -
            Decimal(4) / (10 * k + 7) -
            Decimal(1) / (4 * k + 3)
        )
        k += 1
    pi = pi * 1 / (2 ** 6)
    return str(pi)


def chudnovsky(depth):
    """
    World record holding formula for calculating 5 trillion digits of Pi in
    August 2010. It's a heavy hitter on CPU. This one is about quality over
    quantity.

    http://en.wikipedia.org/wiki/Chudnovsky_algorithm

    :param depth:
    :return:
    """
    pi = Decimal(0)
    k = 0
    while k < depth:
        pi += (Decimal(-1) ** k) * (
            Decimal(math.factorial(6 * k)) /
            (
                (math.factorial(k) ** 3) * (math.factorial(3 * k))
            ) * (13591409 + 545140134 * k) /
            (640320 ** (3 * k))
        )
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi **= -1
    return pi


class Timer2Class(object):
    """timer class"""

    timer = time.clock if sys.platform[:3] == 'win' else time.time

    def __init__(self, func, *args, **kwargs):
        """constructor"""

        self.func = func
        self.args = args
        self.kwargs = kwargs

    def total(self, reps, func, *pargs, **kargs):
        """total method"""

        repslist = list(range(reps))
        start = self.timer()

        for i in repslist:
            ret = func(*pargs, **kargs)
        elapsed = self.timer() - start

        return (elapsed, ret)
