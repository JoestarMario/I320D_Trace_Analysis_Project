import pandas as pd
from datetime import datetime, time, date
import matplotlib.pyplot as plt

def get_repo_dfs(dfs: dict[str, pd.DataFrame], repo_name: str) -> dict[str, pd.DataFrame]:
    return_dict: dict[str, pd.DataFrame] = {}

    for key, df in dfs.items():
        new_df: pd.DataFrame = df[(df['repo_name'] == repo_name)]
        new_df['event_datetime'] = pd.to_datetime(new_df['event_datetime'], utc=True)
        return_dict[key] = new_df


    return return_dict

def plot_pr_success_by_hour(pr_df: pd.DataFrame) -> None:
    entries_data: dict[time, list[int]] = {}

    for entry in pr_df.itertuples():
        event_hour = entry.event_datetime.time().replace(minute=0, second=0, microsecond=0)

        if event_hour not in entries_data:
            entries_data[event_hour] = [0, 0]
        if entry.pr_merge_status == "merged":
            entries_data[event_hour][0] += 1
        else:
            entries_data[event_hour][1] += 1

    x_axis: list[str] = []
    y_axis: list[float] = []

    for key in sorted(entries_data.keys(), key=lambda x: x.hour):
        x_axis.append(key.strftime("%I %p"))
        y_axis.append(entries_data[key][0] / sum(entries_data[key]))
        

    plt.bar(x_axis, y_axis)
    plt.xticks(rotation=60)
    plt.xlabel("Hour of day")
    plt.ylabel("PR succesful merge rate")
    plt.yticks(ticks=[0.0, 0.5, 1.0], labels=["0%", "50%", "100%"])
    plt.show()
