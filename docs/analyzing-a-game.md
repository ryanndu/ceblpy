# Analyzing a game

Let's look at one game: the 2025 CEBL final, where the Niagara River Lions beat
the Calgary Surge 79–73 to win the championship.

## Find the game

Every dataset is keyed on `fiba_game_id`, so the schedule is where you start.

```python exec="true" source="above"
import ceblpy

schedule = ceblpy.load_cebl_schedule(2025)
final = schedule[schedule["fiba_game_id"] == "2702972"]

print(
    final[[
        "start_time_utc",
        "venue_name",
        "home_team_name",
        "home_team_score",
        "away_team_name",
        "away_team_score",
    ]].to_markdown(index=False)
)
```

## Team totals

The team box score has one row per team per game.

```python exec="true" source="above"
import ceblpy

boxscore = ceblpy.load_cebl_team_boxscore(2025)
final = boxscore[boxscore["fiba_game_id"] == "2702972"]

print(
    final[[
        "team_name",
        "points",
        "field_goals_made",
        "field_goals_attempted",
        "total_rebounds",
        "bench_points",
        "points_in_paint",
    ]].to_markdown(index=False)
)
```

The two teams combined for 54 made field goals on 147 attempts. Calgary scored more 
in the paint, 30–20, while Niagara had the edge on the glass and from the bench.

## Individual lines

The player box score has one row per player per game, including players who
didn't get off the bench. Filtering on `minutes > 0` drops them, which is
useful when you're computing per-player rates and don't want zero-minute rows
in the denominator.

```python exec="true" source="above"
import ceblpy

players = ceblpy.load_cebl_player_boxscore(2025)
final = players[
    (players["fiba_game_id"] == "2702972") & (players["minutes"] > 0)
]

print(
    final.sort_values("points", ascending=False)
    .head(6)[[
        "first_name",
        "family_name",
        "minutes",
        "points",
        "total_rebounds",
        "assists",
    ]]
    .to_markdown(index=False)
)
```

## Where the shots came from

Play-by-play has one row per event. Shots carry court coordinates in `x` and
`y`, so you can work with location as well as outcome.

```python exec="true" source="above"
import ceblpy

pbp = ceblpy.load_cebl_pbp(2025)
shots = pbp[
    (pbp["fiba_game_id"] == "2702972") & 
    (pbp["action_type"].isin(["2pt", "3pt"]))
]

print(
    shots[[
        "player_name",
        "action_type",
        "success",
        "x",
        "y",
    ]]
    .head(6)
    .to_markdown(index=False)
)
```

## Plotting the shots

Lets create a plot of every shot in the game for the home team, Niagra.
Shots show up at both ends because they switch sides at the half. So the 
first half is one side and the second is the other.

```python exec="true" html="true" source="above"
from io import StringIO

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from mplbasketball import Court

import ceblpy

pbp = ceblpy.load_cebl_pbp(2025)

shots = pbp[
    (pbp["fiba_game_id"] == "2702972") &
    (pbp["action_type"].isin(["2pt", "3pt"])) &
    (pbp["is_home"] == True)
].copy()

# x and y run 0-100 across the full court; scale to FIBA metres (28m x 15m)
shots["x_m"] = (shots["x"] / 100) * 28
shots["y_m"] = (shots["y"] / 100) * 15

# Drawn in a placeholder colour, swapped for currentColor at the end so the
# court and labels follow the page's light or dark theme.
INHERIT = "#ff00ff"

court = Court(court_type="fiba", origin="bottom-left", units="m")
fig, ax = court.draw(showaxis=False, line_color=INHERIT, line_alpha=0.45)

shot_styles = {
    True: ("Made", {"color": "#e8452c"}),
    False: ("Missed", {"facecolors": "none", "edgecolors": "#4c9be8"}),
}

for made, (label, style) in shot_styles.items():
    subset = shots[shots["success"].eq(made)]
    ax.scatter(subset["x_m"], subset["y_m"], s=55, alpha=0.9, label=label, **style)

ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), frameon=False, labelcolor=INHERIT)
ax.set_title("Niagara River Lions shots — 2025 CEBL final", pad=15, color=INHERIT)

buffer = StringIO()
plt.savefig(buffer, format="svg", bbox_inches="tight", transparent=True)
print(buffer.getvalue().replace(INHERIT, "currentColor"))
```

## What else

`load_cebl_officials` gives you the crew for each game, and every loader takes
a list of seasons or nothing at all if you want the full history. See the
[API reference](reference.md) for the details.