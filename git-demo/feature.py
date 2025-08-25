import pandas as pd

def create_features(data):
    """
    Create new features from the input DataFrame.
    
    Parameters:
    data (pd.DataFrame): Input DataFrame containing raw data.
    
    Returns:
    pd.DataFrame: DataFrame with new features added.
    """
    # Example feature creation
    data['feature_sum'] = data.sum(axis=1)
    data['feature_mean'] = data.mean(axis=1)
    
    return data