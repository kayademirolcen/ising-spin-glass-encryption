import numpy as np

def simulated_annealing(cost_fn, n, steps=1000, temp0=5.0, seed=0):
    rng = np.random.default_rng(seed)
    s = rng.choice([-1, 1], size=n)
    e = cost_fn(s)
    for t in range(1, steps + 1):
        i = rng.integers(0, n)
        s_new = s.copy()
        s_new[i] *= -1
        e_new = cost_fn(s_new)
        de = e_new - e
        T = temp0 / t
        if de <= 0 or rng.random() < np.exp(-de / max(T, 1e-9)):
            s, e = s_new, e_new
    return s, e
