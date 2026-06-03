import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.asarray(x)
    
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x.tolist())
    max_count = max(counts.values())
    mode = sorted(k for k, v in counts.items() if v == max_count)
    mode = mode[0] 

    return mean, median, mode