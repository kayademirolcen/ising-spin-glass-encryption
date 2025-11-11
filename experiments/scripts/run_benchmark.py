import json, time, pathlib
from isingcrypto.models import Ising
from isingcrypto.solvers.classical import simulated_annealing
from isingcrypto.metrics import tts

if __name__ == "__main__":
    n = 32
    model = Ising.random(n)
    start = time.time()
    s, e = simulated_annealing(lambda x: model.energy(x), n, steps=2000)
    dt = time.time() - start
    m = {"n": n, "energy": float(e), "seconds": dt, "tts": tts(dt, 0.5)}
    out = pathlib.Path("experiments/runs/sa_demo.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(m, indent=2))
    print(out)
