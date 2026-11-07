from collections import Counter
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    c = Counter(samples)
    n = len(samples)
    return [(key, value/n) for key, value in c.items()]