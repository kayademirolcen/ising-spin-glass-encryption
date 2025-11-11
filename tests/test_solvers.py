from isingcrypto.solvers.classical import simulated_annealing

def test_sa_runs():
    import numpy as np
    def cost(s):
        return float((s**2).sum())
    s, e = simulated_annealing(cost, 8, steps=10)
    assert len(s) == 8
