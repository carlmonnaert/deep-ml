import numpy as np

def simulate_clt(distribution: str, n: int, runs: int = 10000, seed: int = 42) -> dict:
    """
    Simulate the Central Limit Theorem.

    Args:
        distribution (str): The distribution to sample from ('uniform', 'exponential', 'bernoulli').
        n (int): Sample size.
        runs (int): Number of repeated experiments.
        seed (int): Random seed for reproducibility.

    Returns:
        dict: {'mean': float, 'std': float} of the standardized sample means.
    """
    np.random.seed(seed)
    str_to_fun = {
        'uniform': lambda s: (np.random.uniform(0,1,size=s),0.5, np.sqrt(1/12)),
        'exponential': lambda s:(np.random.exponential(1.0, size=s),1.0, 1.0),
        'bernoulli': lambda s:((np.random.rand(*s) < 0.3), 0.3, np.sqrt(0.21))
    }
    x,mu,sigma = str_to_fun[distribution]((runs,n))
    z = (np.mean(x, axis=1)-mu)/(sigma/np.sqrt(n))
    return {
        'mean': np.mean(z),
        'std': np.std(z)
        }