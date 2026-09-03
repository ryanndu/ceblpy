from datetime import UTC, datetime

import pytest

from ceblpy.loaders import _validate_seasons


def test_none_returns_every_season():
    assert _validate_seasons(None) == list(range(2019, datetime.now(UTC).year + 1))


def test_int_becomes_a_list():
    assert _validate_seasons(2024) == [2024]


def test_list_passes_through():
    assert _validate_seasons([2023, 2024]) == [2023, 2024]


def test_non_int_season_raises():
    with pytest.raises(TypeError):
        _validate_seasons("2024")

    with pytest.raises(TypeError):
        _validate_seasons([2023, "2024"])


def test_season_out_of_range_raises():
    with pytest.raises(ValueError):
        _validate_seasons(2018)

    with pytest.raises(ValueError):
        _validate_seasons(datetime.now(UTC).year + 1)
