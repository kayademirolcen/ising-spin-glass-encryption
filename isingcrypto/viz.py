import matplotlib.pyplot as plt

def plot_energy_trace(vals):
    plt.figure()
    plt.plot(vals)
    plt.xlabel("step")
    plt.ylabel("energy")
    plt.title("Energy trace")
    plt.tight_layout()
