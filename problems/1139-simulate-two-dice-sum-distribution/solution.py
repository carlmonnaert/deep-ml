def simulate_dice_sum(num_rolls, seed=0):
    import numpy as np
    rng = np.random.RandomState(seed)
    d1 = rng.randint(1,7, size=num_rolls)
    d2 = rng.randint(1,7, size=num_rolls)
    s = d1+d2
    p = np.array([np.sum(s==i)/num_rolls for i in range(2,13)])
    return p, np.array([(6 - abs(i-7))/36 for i in range(2,13)])