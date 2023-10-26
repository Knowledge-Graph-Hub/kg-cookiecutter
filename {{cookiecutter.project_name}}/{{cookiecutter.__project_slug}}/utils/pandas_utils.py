"""Pandas utilities."""
from pathlib import Path

import pandas as pd


def drop_duplicates(file_path: Path):
    """
    Read TSV, drop duplicates and export to same file.

    :param df: Dataframe
    :param file_path: file path.
    """
    df = pd.read_csv(file_path, sep="\t", low_memory=False)
    df = df.drop_duplicates()
    df.to_csv(file_path, sep="\t", index=False)
