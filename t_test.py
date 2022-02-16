import numpy as np
from collections import namedtuple
from scipy.stats import t
MySimpleTtestResults = namedtuple('MySimpleTtestResults', 
                                  ['is_rejected', 'pvalue'])

def my_simple_t_test(sample: list, mu_0: float, alpha: float = 0.05):


    is_rejected = None
    pvalue = None

    n = len(sample)
    sample_mean = sum(sample) / n
    df = n - 1
    sum_of_squares = 0
    for ev in sample:
        sum_of_squares += (ev - sample_mean) ** 2
    se = ((sum_of_squares) / (len(sample) - 1)) ** (1 / 2)
    t_stat = (sample_mean - mu_0) / (se / n ** (1 / 2))
    pvalue = (1 - t.cdf(abs(t_stat), df)) * 2
    if pvalue > alpha:
        is_rejected = False
    else:
        is_rejected = True


    return MySimpleTtestResults(is_rejected, pvalue)
