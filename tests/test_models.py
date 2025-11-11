import numpy as np
from isingcrypto.models import Ising

def test_energy_shape():
    n = 8
    m = Ising.random(n)
    s = np.ones(n)
    e = m.energy(s)
    assert isinstance(e, float)
