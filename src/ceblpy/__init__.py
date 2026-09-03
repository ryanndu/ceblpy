from importlib.metadata import version

from ceblpy.loaders import (
    load_cebl_officials,
    load_cebl_pbp,
    load_cebl_player_boxscore,
    load_cebl_schedule,
    load_cebl_team_boxscore,
)

__version__ = version("ceblpy")

__all__ = [
    "__version__",
    "load_cebl_officials",
    "load_cebl_pbp",
    "load_cebl_player_boxscore",
    "load_cebl_schedule",
    "load_cebl_team_boxscore",
]
