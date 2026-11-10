import math

def multinomial_logpmf(counts, theta):
    N = sum(counts)
    log_N = sum([math.log(n) for n in range(1,N+1)])
    log_fact = 0.
    log_theta = 0.
    for ni,thetai in zip(counts,theta):
        log_fact += sum([math.log(n) for n in range(1,ni+1)])
        if ni > 0:
            log_theta += ni * math.log(thetai) if thetai > 0 else -math.inf
    return log_N - log_fact + log_theta