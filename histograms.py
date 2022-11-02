import pandas as pd
from matplotlib import pyplot as plt


def plot_histograms(csv_in='params.csv', png_out='params_hist.png'):
    df = pd.read_csv(csv_in)
    n_params = len(df.columns) - 1
    fig, axs = plt.subplots(3, 4)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs.reshape(-1):
        ax.set_visible(False)
    for ax, c in zip(axs.reshape(-1), df.columns[1:]):
        ax.set_visible(True)
        ax.hist(df[c], bins=20)
        ax.set_title(c, fontsize=8)
    fig.suptitle(f'{len(df)} experiments: Parameter spread.')

    fig.savefig(png_out)


if __name__ == "__main__":
    plot_histograms()
