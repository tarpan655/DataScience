"""Simple data loading and preprocessing utilities."""
import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(path)


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: drop duplicates and reset index."""
    df = df.drop_duplicates().reset_index(drop=True)
    return df


if __name__ == '__main__':
    print('data_processing module')
