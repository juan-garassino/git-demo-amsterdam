import numpy as np

def calculate_wip(data):
    """
    Calculate the Weighted Importance Performance (WIP) score for a given dataset.
    
    Parameters:
    data (list of tuples): A list where each tuple contains (importance, performance).
    
    Returns:
    float: The WIP score.
    """
    if not data:
        return 0.0
    
    importance = np.array([item[0] for item in data])
    performance = np.array([item[1] for item in data])
    
    # Normalize importance and performance
    norm_importance = importance / np.sum(importance)
    norm_performance = performance / np.sum(performance)
    
    # Calculate WIP
    wip_score = np.sum(norm_importance * norm_performance)
    
    return wip_score