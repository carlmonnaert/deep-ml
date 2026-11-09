import numpy as np

def simulate_clt(num_samples: int, sample_size: int, distribution: str = 'uniform') -> float:
    """
    Compute the mean of sample means to demonstrate the sampling distribution.

    Args:
        num_samples: Number of independent samples to draw
        sample_size: Size of each sample
        distribution: 'uniform' (0,1) or 'exponential' (scale=1)

    Returns:
        Mean of the sample means (float)
    """
    if distribution == 'uniform':
        x = np.random.uniform(0, 1, size=(num_samples,sample_size))
    elif distribution == 'exponential':
        x = np.random.exponential(1, size=(num_samples,sample_size))
    else:
        raise ValueError(f'Distribution not supported: {distribution}')
    means = np.mean(x, axis=1)
    return np.mean(means)
