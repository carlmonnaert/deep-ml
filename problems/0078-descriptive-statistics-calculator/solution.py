import numpy as np
from scipy import stats
def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data = np.asarray(data)
    mean = np.mean(data)
    median = np.median(data)
    mode = stats.mode(data)[0]
    variance = np.var(data)
    standard_deviation = np.sqrt(variance)
    percentiles = np.percentile(data, q=[25, 50, 75])
    iqr = percentiles[2] - percentiles[0]
    return {'mean': mean,
            'median': median,
            'mode': mode,
            'variance': variance,
            'standard_deviation':standard_deviation,
            '25th_percentile': percentiles[0],
            '50th_percentile': percentiles[1],
            '75th_percentile': percentiles[2],
            'interquartile_range': iqr
            }


