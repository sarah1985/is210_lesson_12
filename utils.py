#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides a long-running simulation task."""

import json
import time


def sleeptest(seconds):
    """Provides a long-running program test case.
    
    Args:
        seconds (number): Number of seconds to sleep.

    Examples:

        >>> sleeptest(5)
    """
    time.sleep(seconds)


def get_json(filename):
    """Helper function to open and return JSON data.

    Args:
        filename (string): Filename to open.

    Returns:
        mixed: The contents of the JSON file.

    Examples:

        >>> outfile = open('tempfile.json', 'w')
        >>> json.dump(['a', 'b', 'c'], outfile)
        >>> outfile.close()
        >>> get_json('tempfile.json')
        ['a', 'b', 'c']
    """
    fhandler = open(filename, 'r')
    try:
        data = json.load(fhandler)
    finally:
        fhandler.close()

    return data


def loop_style_one(wordfile):
    """Calculates the number of letters in the dictionary words.

    Args:
        filename (string): Name of file to load.

    Returns:
        integer: Number of letters in the dictionary words.

    Example:

        >>> outfile = open('wordfile.json', 'w')
        >>> json.dump(['a', 'b', 'c'], outfile)
        >>> outfile.close()
        >>> loop_style_one('wordfile.json')
        3
    """
    count = 0
    for word in get_json(wordfile):
        count += len(word)
    return count


def loop_style_two(wordfile):
    """Calculates the number of letters in the dictionary words.

    Args:
        filename (string): Name of file to load.

    Returns:
        integer: Number of letters in the dictionary words.

    Example:

        >>> outfile = open('wordfile.json', 'w')
        >>> json.dump(['a', 'b', 'c'], outfile)
        >>> outfile.close()
        >>> loop_style_two('wordfile.json')
        3
    """
    return sum([len(x) for x in get_json(wordfile)])
