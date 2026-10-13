import matplotlib.pyplot as plt

def plot_hist(counts,title="Plot"):

    labels = [str(k) for k in counts]
    values = [int(v) for v in counts.values()]
    shots = sum(values)

    _, ax = plt.subplots(figsize=(5, 4))
    bars = ax.bar(labels, values, color="#4C72B0", width=0.6)
    ax.bar_label(bars, labels=[f"{v}  ({v/shots:.0%})" for v in values], padding=3, fontsize=9)

    ax.set_xlabel("Bitstring")
    ax.set_ylabel(f"Counts  (shots = {shots})")
    ax.set_title(title)
    ax.set_ylim(0, max(values) * 1.2)
    ax.grid(axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation="vertical")
    plt.tight_layout()
    plt.show()

