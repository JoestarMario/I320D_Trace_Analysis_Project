"""Module creating and providing functions for analysis in notebook"""

import pandas as pd

def get_repo_dfs(dfs: dict[str, pd.DataFrame], repo_name: str) -> dict[str, pd.DataFrame]:
    """
    Get dataframes with repo_name value matching the given repo name

    Parameters
    ----------
    dfs : dict[str, DataFrame]
        DataFrames to filter, with keys representing the title of the df.
    repo_name : str
        Repository name to filter by. 
        Should be ordered as commits, then issues, the pull request dfs.

    Returns
    -------
    return_dict
        Dictionary of dataframes filtered by repo_name.
    """
    return_dict: dict[str, pd.DataFrame] = {}

    for key, df in dfs.items():
        return_dict[key] = df[(df['repo_name'] == repo_name)]
    return return_dict
