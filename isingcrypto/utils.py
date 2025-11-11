def set_seed(seed: int):
    import numpy as np
    import random
    import os
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
