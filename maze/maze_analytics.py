"""
maze_analytics.py

This module provides functions to compute basic descriptive analytics such as mean, median, mode, count, range,
minimum, and maximum from a list of numbers.

Source reference for statistical methods: https://docs.python.org/3/library/statistics.html
"""

import statistics

def calc_mean(scores):
    """Calculate the mean (average) of the scores.
    
    Source: https://docs.python.org/3/library/statistics.html#statistics.mean
    """
    try:
        return statistics.mean(scores)
    except Exception as e:
        raise ValueError("Error calculating mean: " + str(e))


def calc_median(scores):
    """Calculate the median of the scores.
    
    Source: https://docs.python.org/3/library/statistics.html#statistics.median
    """
    try:
        return statistics.median(scores)
    except Exception as e:
        raise ValueError("Error calculating median: " + str(e))


def calc_mode(scores):
    """Calculate the mode of the scores.
    
    Source: https://docs.python.org/3/library/statistics.html#statistics.mode
    """
    try:
        return statistics.mode(scores)
    except statistics.StatisticsError:
        return "No unique mode found"


def calc_count(scores):
    """Return the count (number of games played).
    
    This is a simple count function.
    """
    return len(scores)


def calc_min(scores):
    """Return the minimum score.
    
    Source: Python built-in min() function.
    """
    try:
        return min(scores)
    except Exception as e:
        raise ValueError("Error finding minimum: " + str(e))


def calc_max(scores):
    """Return the maximum score.
    
    Source: Python built-in max() function.
    """
    try:
        return max(scores)
    except Exception as e:
        raise ValueError("Error finding maximum: " + str(e))


def calc_range(scores):
    """Calculate the range (max - min) of the scores.
    
    Combines calc_min and calc_max.
    """
    try:
        return calc_max(scores) - calc_min(scores)
    except Exception as e:
        raise ValueError("Error calculating range: " + str(e))
