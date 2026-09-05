# Data dictionary

Every column in every dataset.

## `schedule`

```python exec="true"
import json
from pathlib import Path

import ceblpy

frame = ceblpy.load_cebl_schedule()
descriptions = json.loads(Path("docs/columns.json").read_text())["schedule"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `team-boxscore`

```python exec="true"
import json
from pathlib import Path

import ceblpy

frame = ceblpy.load_cebl_team_boxscore()
descriptions = json.loads(Path("docs/columns.json").read_text())["team-boxscore"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `player-boxscore`

```python exec="true"
import json
from pathlib import Path

import ceblpy

frame = ceblpy.load_cebl_player_boxscore()
descriptions = json.loads(Path("docs/columns.json").read_text())["player-boxscore"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `pbp`

```python exec="true"
import json
from pathlib import Path

import ceblpy

frame = ceblpy.load_cebl_pbp()
descriptions = json.loads(Path("docs/columns.json").read_text())["pbp"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `officials`

```python exec="true"
import json
from pathlib import Path

import ceblpy

frame = ceblpy.load_cebl_officials()
descriptions = json.loads(Path("docs/columns.json").read_text())["officials"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```