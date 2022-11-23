import argparse
from typing import Optional
import sys
from pathlib import Path
import pandas as pd

CSV_DEFAULT_IN = Path(__file__).parent / "../params.csv"
HTML_DEFAULT_OUT = Path(__file__).parent / "../params_corr.html"


def csv_to_corr_html(csv_in: Path, html_out: Path, ignore_col: Optional[list[int]] = None):
    df = pd.read_csv(csv_in)
    columns = list(df.columns)
    if ignore_col is not None:
        for col in ignore_col:
            try:
                columns.remove(col)
            except ValueError as e:
                raise ValueError('Value {:} not found in CSV columns.'.format(
                    col)).with_traceback(e.__traceback__)
    corr = df[columns].corr()
    for ii in range(len(corr)):
        corr.iloc[ii, ii] = pd.NA
    corr_styled = corr.style.background_gradient(cmap='coolwarm', axis=None)
    corr_styled.to_html(html_out)


def cli_args():
    parser = argparse.ArgumentParser(
        prog='csv_to_corr_html',
        description="Produce html correlation matrix from a CSV file."
    )
    parser.add_argument('csv_in', type=argparse.FileType('r'))

    parser.add_argument(
        'html_out', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
        help="Path to write html file to - default to stdout.")

    parser.add_argument(
        '-i', '--ignore', action='append',
        dest='ignore_col', metavar="COLUMN_NAME",
        help='CSV column to ignore (repeat to ignore multiple columns).')

    return parser.parse_args()


if __name__ == "__main__":
    args = cli_args()
    csv_to_corr_html(**vars(args))
