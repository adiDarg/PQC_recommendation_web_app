import numpy as np


# Functions for scaling values in the format of (val,args)
def minMax(val, args):
    # args[0] = min, args[1] = max
    return (val - args[0]) / (args[1] - args[0])


def zStandard(val, args):
    # args[0] = average, #args[1] = standard deviation
    return (val - args[0]) / args[1]


def medianStandard(val, args):
    # args[0] = median, #args[1] = IQR (Inter quartile Range)
    return (val - args[0]) / args[1]


def maxAbsScaling(val, args):
    # args[0] = max
    return val / abs(args[0])


def unitVectorScaling(val, args):
    # args = samples
    return val / (sum(args)) ** 2


def softMaxScaling(val, args):
    # args = samples
    return np.exp(val) / (sum(np.exp(args)))


def sigmoid(val, args):
    return 1 / (1 + np.exp(-val))


def softRELU(val, args):
    return np.log(1 + np.exp(val)) / np.log(10)


def stableSoftmax(val, args):
    # args = samples
    args_array = np.array(args)
    max_val = np.max(args_array)

    numerator = np.exp(val - max_val)
    denominator = np.sum(np.exp(args_array - max_val))

    return numerator / denominator


def nothing(val, args):
    return val
