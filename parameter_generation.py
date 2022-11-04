"""Parameter generation script"""
from random import seed, randrange
import numpy as np

from rand_param import Product
from histograms import plot_histograms

N_EXPERIMENTS = 20000
seed(123)

params = {
    'swim_speed': np.arange(0.5, 5.01, 0.5),
    'piling_duration': np.arange(1, 13),
    'max_SEL': np.arange(200, 225.1, 5),
    'add_duration': np.arange(0, 30.01, 5),
    'slow_start_duration': np.arange(0, 60.01, 10),
    'slow_start_strike_rate': np.arange(1, 30.01, 6),
    'slow_start_hammer_energy': np.arange(10, 100.01, 10),
    'soft_start_duration': np.arange(0, 60.01, 10),
    'soft_start_strike_rate': np.arange(30, 60.01, 6),
    'soft_start_hammer_energy': np.arange(10, 100.01, 10),
    'full_power_strike_rate': np.arange(30, 60.01, 6)
}


def main(n_experiments=N_EXPERIMENTS, csv_out='params.csv'):
    # First and last experiment
    p = Product(params.values())
    n_max = len(p)
    print(f'{n_max=}')
    print(f'{p[0]=}')
    print(f'{p[-1]=}')
    print('')

    param_names = list(params)
    idx_slow_start = param_names.index('slow_start_duration')
    idx_soft_start = param_names.index('soft_start_duration')
    idx_piling_duration = param_names.index('piling_duration')
    # Output the experiment number and the parameters
    with open(csv_out, 'w') as f:
        f.write('n,' + ','.join(params.keys()) + '\n')
        rows_written = 0
        while rows_written < N_EXPERIMENTS:
            n = randrange(n_max)
            p_n = p[n]
            soft_slow = p_n[idx_soft_start] + p_n[idx_slow_start]
            total = 60 * p_n[idx_piling_duration]
            # We want to ignore parameter sets where the slow and soft are
            # greater than the total duration
            if soft_slow > total:
                continue
            f.write(f'{n},' + ','.join(str(ex) for ex in p_n) + '\n')
            rows_written += 1


if __name__ == "__main__":
    main(N_EXPERIMENTS, 'params.csv')
    plot_histograms('params.csv', 'params_hist.png')
