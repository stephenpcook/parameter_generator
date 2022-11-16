import math

import pandas as pd
from matplotlib import pyplot as plt

N_ROWS = 3


def plot_histograms(csv_in='params.csv', png_out='params_hist.png',
                    hist_args=None, params=None):
    if hist_args is None:
        hist_args = {}
    if params is None:
        params = {}
    df = pd.read_csv(csv_in)
    n_params = len(df.columns) - 1
    n_columns = math.ceil(n_params/3)
    fig, axs = plt.subplots(N_ROWS, n_columns)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs.reshape(-1):
        ax.set_visible(False)
    for ax, c in zip(axs.reshape(-1), df.columns[1:]):
        bins = params.get(c, None)
        if (bins is not None):
            bins = list(bins)
            if (len(bins) > 1):
                bin_width = bins[1] - bins[0]
                bins.append(bins[-1] + bin_width)
        else:
            bins = 20
        ax.set_visible(True)
        ax.hist(df[c], bins=bins, **hist_args)
        ax.set_title(c, fontsize=8)
    fig.suptitle(f'{len(df)} experiments: Parameter spread.')

    fig.savefig(png_out)


if __name__ == "__main__":
    plot_histograms()
