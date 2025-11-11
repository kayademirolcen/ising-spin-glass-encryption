import numpy as np
from .models import Ising

def encode_message_to_ising(msg: str):
    n = max(8, len(msg) * 4)
    model = Ising.random(n)
    key = {"n": n}
    return model, key
