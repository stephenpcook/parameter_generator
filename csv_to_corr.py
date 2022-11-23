from typing import Optional
from pathlib import Path
import pandas as pd

CSV_IN = Path(__file__).parent / "../params.csv"
HTML_OUT = Path(__file__).parent / "../params_corr.html"


def csv_to_corr_html(csv_in: Path, html_out: Path, ignore_cols: Optional[list[int]] = None):
    df = pd.read_csv(csv_in, index_col=0)
    columns = list(df.columns)
    if ignore_cols is not None:
        for col in ignore_cols:
            columns.remove(col)
    corr = df[columns].corr()
    for ii in range(len(corr)):
        corr.iloc[ii, ii] = pd.NA
    corr_styled = corr.style.background_gradient(cmap='coolwarm', axis=None)
    corr_styled.to_html(html_out)


if __name__ == "__main__":
    csv_to_corr_html(CSV_IN, HTML_OUT)
