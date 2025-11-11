from dataclasses import dataclass
import numpy as np
import networkx as nx

@dataclass
class Ising:
    J: np.ndarray
    h: np.ndarray
    def energy(self, s: np.ndarray) -> float:
        return float(s @ self.J @ s + self.h @ s)
    @staticmethod
    def random(n: int, p: float = 0.2, scale: float = 1.0):
        g = nx.gnp_random_graph(n, p, seed=0)
        J = np.zeros((n, n))
        for i, j in g.edges():
            val = np.random.uniform(-scale, scale)
            J[i, j] = val
            J[j, i] = val
        h = np.random.uniform(-scale, scale, size=n)
        return Ising(J=J, h=h)
