import pandas as pd
from event_datetime import Datetime, Date, Time

def get_repo_dfs(dfs: dict[str, pd.DataFrame], repo_name: str) -> dict[str, pd.DataFrame]:
    return_dict: dict[str, pd.DataFrame] = {}

    for key, df in dfs.items():
        new_df: pd.DataFrame = df[(df['repo_name'] == repo_name)]
        return_dict[key] = new_df


    return return_dict
