import pandas as pd
from datetime import datetime

def get_repo_dfs(dfs: dict[str, pd.DataFrame], repo_name: str) -> dict[str, pd.DataFrame]:
    return_dict: dict[str, pd.DataFrame] = {}

    for key, df in dfs.items():
        new_df: pd.DataFrame = df[(df['repo_name'] == repo_name)]
        new_df['event_datetime'] = pd.to_datetime(new_df['event_datetime'], utc=True)
        return_dict[key] = new_df


    return return_dict
