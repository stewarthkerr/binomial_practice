#!/usr/bin/env python
"""
Calculates binomial coefficients, returning either natural log or the integer"
"""

import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="n in choose(n,k)")
parser.add_argument("-k", type=int, help="k in choose(n,k)")
parser.add_argument("-l", "--log", action="store_true", help="flag to calculate log")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

#This is the flag for either log or integer output
op_flag = "log" if args.log else "coeff"

# test argument problems:
if not args.test and __name__ == '__main__':
    if args.n is None or args.k is None:
        raise Exception("-n and -k must be specified")
    if args.n<0:
        raise Exception("n must be non-negative")
    if args.k<0:
        raise Exception("k must be non-negative")
    if args.k > args.n:
        raise Exception("k must be less than or equal to n")
    # no error if file imported as module

def choose(n, k = 0, output = op_flag):
    """Calculates choose(n,k) for any integers 0 <= k <= n
    If output = "coeff", then choose returns the binomial coefficient itself
    If output = "log", then choose returns the log of the binomial coefficient

    Examples:
    >>> choose(5,2,"log")
    2.3025850929940455
    >>> choose(5,5,"log")
    0.0
    >>> choose(5,5,"coeff")
    1
    >>> choose(5,2,"coeff")
    10
    """

    assert type(n)==int, "n must be an integer"
    assert type(k)==int, "k must be an integer"
    assert n >= 0, "n must be non-negative"
    assert k >= 0, "k must be non-negative"
    assert k <= n, "k must be less than or equal to n"
    assert output == "coeff" or output == "log", 'output must be "coeff" or "log"'

    logchoose = logfactorial(n,k) - logfactorial(n-k)

    if (output == "coeff"):
        outv = int(round(math.exp(logchoose),0))
    else:
        outv = float(logchoose)

    return outv

def logfactorial(n, k = 0):
    """Calculates log(n!) for any integer n>0

    Examples:
    >>> logfactorial(4)
    3.1780538303479453
    >>> logfactorial(5,2)
    4.0943445622221
    >>> logfactorial(5,5)
    0
    >>> logfactorial(5,6)
    0
    """

    assert type(n)==int, "n must be an integer"
    assert n >= 0, "n must be non-negative"
    assert type(k)== int, "k must be an integer"
    assert k >= 0, "k must be non-negative"

    logfac = 0
    for i in range(k+1,n+1):
        logfac += math.log(i)
    return(logfac)

def runTests():
    print("Testing the module...")
    import doctest
    doctest.testmod()
    print("done with tests.")

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        print("Output:",choose(args.n,args.k))
