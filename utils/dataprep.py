import pandas as pd
from typing import List

def load_and_preprocess_data(file_name: str, target_columns: List[str]) -> pd.DataFrame:
    """Read dataset by specifying additional na values to recognize and columns to remove rows with na cells
    
    Parameters:
    file_name (str): Path to file to read from. Path is relative from module
    target_columns (list of str): Remove rows if these columns have nan cells

    Returns:
    DataFrame: Cleaned dataframe
    """
    df = pd.read_csv(file_name, na_values='na')
    df.dropna(subset=target_columns, inplace=True)
    return df