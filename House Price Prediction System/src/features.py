"""Feature engineering helpers."""

import pandas as pd


def add_total_rooms(df: pd.DataFrame) -> pd.DataFrame:
    """Example feature: total rooms if columns exist."""
    cols = ['bedrooms', 'bathrooms', 'living_rooms']
    present = [c for c in cols if c in df.columns]
    if present:
        df['total_rooms'] = df[present].sum(axis=1)
    return df
