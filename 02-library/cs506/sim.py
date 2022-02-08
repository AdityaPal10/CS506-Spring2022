import numpy as np
from scipy import spatial
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i]) ** 2
    return res ** (1 / 2)


def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res


def jaccard_dist(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union


def cosine_sim(List1, List2):
    result = 1 - spatial.distance.cosine(List1, List2)
    return result

# Feel free to add more
