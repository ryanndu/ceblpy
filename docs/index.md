# ceblpy <img src="https://github.com/ryanndu/ceblpy/raw/main/assets/images/cebl-logo.jpg" align="right" width="100" height="100"/>

The goal of this package is to help people access clean and tidy data from
the Canadian Elite Basketball League. It provides a set of loaders that return
schedules, box scores, play-by-play, and officials as pandas DataFrames, ready
to analyze.

## Installation

```bash
pip install ceblpy
```

## Usage

```python exec="true" source="above"
import ceblpy

schedule = ceblpy.load_cebl_schedule(2025)

print(
    schedule[
        [
            "start_time_utc",
            "home_team_name",
            "home_team_score",
            "away_team_name",
            "away_team_score",
        ]
    ]
    .head()
    .to_markdown(index=False)
)
```

Every loader takes a season, a list of seasons, or nothing at all for every
season available.

```python
ceblpy.load_cebl_player_boxscore(2025)
ceblpy.load_cebl_pbp([2024, 2025])
ceblpy.load_cebl_team_boxscore()
```

Data is sourced from [cebl-data](https://github.com/ryanndu/cebl-data), which
updates daily during the season.