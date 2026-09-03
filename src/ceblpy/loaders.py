import io
from datetime import UTC, datetime

import pandas as pd
import requests


def _load(dataset: str, seasons: int | list[int] | None) -> pd.DataFrame:
    """Loads one published dataset, filtered to the given seasons.

    Args:
        dataset: A dataset name, which is also its release tag.
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        The dataset as published, filtered to the requested seasons.

    Raises:
        TypeError: If seasons isn't an int, a list of ints, or None.
        ValueError: If a season is outside the range of available data.
        ConnectionError: If the data couldn't be downloaded.
    """
    seasons = _validate_seasons(seasons)
    asset = f"cebl_{dataset.replace('-', '_')}.parquet"
    url = f"https://github.com/ryanndu/cebl-data/releases/download/{dataset}/{asset}"

    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
    except requests.RequestException as error:
        raise ConnectionError(
            f"Could not download {dataset} data from {url}"
        ) from error

    frame = pd.read_parquet(io.BytesIO(response.content))
    return frame[frame["season"].isin(seasons)].reset_index(drop=True)


def _validate_seasons(seasons: int | list[int] | None) -> list[int]:
    """_summary_

    Args:
        seasons (int | list[int] | None): _description_

    Raises:
        TypeError: _description_
        TypeError: _description_
        ValueError: _description_

    Returns:
        list[int]: _description_
    """
    first_season = 2019
    latest = datetime.now(UTC).year
    if seasons is None:
        return list(range(first_season, latest + 1))
    if isinstance(seasons, int):
        seasons = [seasons]
    if not isinstance(seasons, list):
        raise TypeError(
            f"Expected seasons to be an int, list of ints, or None, "
            f"got {type(seasons).__name__}"
        )
    for season in seasons:
        if not isinstance(season, int):
            raise TypeError(f"Expected an integer season, got {type(season).__name__}")
        if not first_season <= season <= latest:
            raise ValueError(f"Season {season} out of range ({first_season}-{latest})")
    return seasons


def load_cebl_schedule(seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads the CEBL schedule.

    Args:
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per game.

    Examples:
        >>> load_cebl_schedule(2024)
        >>> load_cebl_schedule([2023, 2024])
        >>> load_cebl_schedule()
    """
    return _load("schedule", seasons)


def load_cebl_team_boxscore(seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads CEBL team box scores.

    Args:
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per team per game, home team first. Includes the head coach
        and assistants.

    Examples:
        >>> load_cebl_team_boxscore(2024)
        >>> load_cebl_team_boxscore([2023, 2024])
        >>> load_cebl_team_boxscore()
    """
    return _load("team-boxscore", seasons)


def load_cebl_player_boxscore(seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads CEBL player box scores.

    Args:
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per player per game, including players who didn't play.

    Examples:
        >>> load_cebl_player_boxscore(2024)
        >>> load_cebl_player_boxscore([2023, 2024])
        >>> load_cebl_player_boxscore()
    """
    return _load("player-boxscore", seasons)


def load_cebl_pbp(seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads CEBL play-by-play.

    Args:
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per event, oldest first, with shot coordinates on shooting
        events.

    Examples:
        >>> load_cebl_pbp(2024)
        >>> load_cebl_pbp([2023, 2024])
        >>> load_cebl_pbp()
    """
    return _load("pbp", seasons)


def load_cebl_officials(seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads CEBL game officials.

    Args:
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per official per game. Games with no officials recorded
        produce no rows.

    Examples:
        >>> load_cebl_officials(2024)
        >>> load_cebl_officials([2023, 2024])
        >>> load_cebl_officials()
    """
    return _load("officials", seasons)
