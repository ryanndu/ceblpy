# ceblpy <img src="https://github.com/ryanndu/ceblpy/raw/main/assets/images/cebl-logo.jpg" align="right" width="100" height="100"/>

---

## Overview

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/ceblpy?period=total&units=NONE&left_color=BLACK&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/ceblpy)

**[ceblpy](https://github.com/ryanndu/ceblpy)** loads Canadian Elite Basketball League (CEBL) data as pandas DataFrames.

Five datasets are available: game schedules, team box scores, player box scores, play-by-play, and game officials. Coaches are included as columns on the team box score.

Full documentation, including a worked example and a data dictionary for every column, is at **[ryanndu.github.io/ceblpy](https://ryanndu.github.io/ceblpy/)**.

---

## Installation

```bash
pip install ceblpy
```

---

## Usage

Every loader takes a season, a list of seasons, or nothing at all for every season available.

```python
from ceblpy import load_cebl_schedule

# Load the 2024 CEBL season schedule
schedule = load_cebl_schedule(2024)

# Preview the data
print(schedule.head())
```

The five loaders are:

| Function | Returns |
| --- | --- |
| `load_cebl_schedule()` | One row per game |
| `load_cebl_team_boxscore()` | One row per team per game |
| `load_cebl_player_boxscore()` | One row per player per game |
| `load_cebl_pbp()` | One row per play-by-play event |
| `load_cebl_officials()` | One row per official per game |

Data is sourced from **[cebl-data](https://github.com/ryanndu/cebl-data)**, which updates daily during the season.