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
from decimal import Decimal
import time
import sys


def stdlib(depth):
    """
    Calculate Pi using the math.pi from Python standard library

    :param depth:
    :return:
    """
    num_a = Decimal(1.0)
    num_b = Decimal(1.0 / math.sqrt(2))
    num_t = Decimal(1.0) / Decimal(4.0)
    num_p = Decimal(1.0)

    for item in range(depth):
        num_at = Decimal((num_a + num_b) / 2)
        num_bt = Decimal(math.sqrt(num_a * num_b))
        num_tt = Decimal(num_t - num_p * (num_a - num_at) ** 2)
        num_pt = Decimal(2 * num_p)

        num_a = num_at
        num_b = num_bt
        num_t = num_tt
        num_p = num_pt

    num_pi = (num_a + num_b) ** 2 / (4 * num_t)

    return str(num_pi)


def bbp(depth):
    """
    Calculate Pi using the Bailey–Borwein–Plouffe formula
    http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula

    :param depth:
    :return:
    """
    num_pi = Decimal(0)
    num_k = 0
    while num_k < depth:
        num_pi += (Decimal(1) / (16 ** num_k)) * (
            (Decimal(4) / (8 * k + 1)) -
            (Decimal(2) / (8 * k + 4)) -
            (Decimal(1) / (8 * k + 5)) -
            (Decimal(1) / (8 * k + 6))
        )
        num_k += 1
    return str(num_pi)


def bellard(depth):
    """
    New school Pi calculation method discovered in 1997 by Fabrice Bellard in
    1997. Usually clocks in 43% faster than the BBP formula.

    http://en.wikipedia.org/wiki/Bellard%27s_formula

    :param depth:
    :return:
    """
    num_pi = Decimal(0)
    num_k = 0
    while num_k < depth:
        num_pi += (Decimal(-1) ** num_k / (1024 ** num_k)) * (
            Decimal(256) / (10 * num_k + 1) +
            Decimal(1) / (10 * num_k + 9) -
            Decimal(64) / (10 * num_k + 3) -
            Decimal(32) / (4 * num_k + 1) -
            Decimal(4) / (10 * num_k + 5) -
            Decimal(4) / (10 * num_k + 7) -
            Decimal(1) / (4 * num_k + 3)
        )
        num_k += 1
    num_pi = num_pi * 1 / (2 ** 6)
    return str(num_pi)


def chudnovsky(depth):
    """
    World record holding formula for calculating 5 trillion digits of Pi in
    August 2010. It's a heavy hitter on CPU. This one is about quality over
    quantity.

    http://en.wikipedia.org/wiki/Chudnovsky_algorithm

    :param depth:
    :return:
    """
    num_pi = Decimal(0)
    num_k = 0
    while num_k < depth:
        num_pi += (Decimal(-1) ** num_k) * (
            Decimal(math.factorial(6 * num_k)) /
            (
                (math.factorial(num_k) ** 3) * (math.factorial(3 * num_k))
            ) * (13591409 + 545140134 * num_k) /
            (640320 ** (3 * num_k))
        )
        num_k += 1
    num_pi = num_pi * Decimal(10005).sqrt() / 4270934400
    num_pi **= -1
    return num_pi


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

        for reps in repslist:
            ret = func(*pargs, **kargs)
        elapsed = self.timer() - start

        return (elapsed, ret)

    def bestof(self, reps, func, *pargs, **kargs):
        """best of method"""

        best = 2 ** 32

        for reps in range(reps):
            start = self.timer()
            ret = func(*pargs, **kargs)
            elapsed = self.timer() - start
            if elapsed < best:
                best = elapsed

        return (best, ret)

    def bestoftotal(self, reps1, reps2, func, *pargs, **kargs):
        """best of total method"""

        return self.bestof(reps1, self.total, reps2, func, *pargs, **kargs)

if __name__ == "__main__":

    n = 1000

    for test in (stdlib, bbp, bellard, chudnovsky):
        timer2 = Timer2Class(test, n, _reps1=1, _reps=3)
        print timer2.bestoftotal()