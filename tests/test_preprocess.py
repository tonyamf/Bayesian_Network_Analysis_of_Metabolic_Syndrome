from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from bn_preprocess import RULES, discretise, discretise_series

FIX = Path(__file__).parent / "fixtures"
ROOT = Path(__file__).parent.parent
COLUMNS = ["DBP", "SBP", "FastingBloodSugar", "Triglycerides",
           "HDLcholestrol", "LDLcholestrol", "IDFMetsynd", "ATPMetssynd"]


def test_matches_committed_dataD_rows():
    raw = pd.read_csv(FIX / "sample_raw.csv")
    expected = pd.read_csv(FIX / "sample_discrete.csv")
    got = discretise(raw)
    pd.testing.assert_frame_equal(
        got.reset_index(drop=True).astype(float),
        expected.reset_index(drop=True).astype(float),
    )


def test_full_dataset_matches_dataD_csv():
    raw = pd.read_csv(ROOT / "data.csv")
    expected = pd.read_csv(ROOT / "dataD.csv")
    got = discretise(raw)
    assert len(got) == len(expected) == 9971
    assert np.array_equal(got.to_numpy(float), expected.to_numpy(float))


@pytest.mark.parametrize("value,level", [(79.9, 0), (80, 1), (89.9, 1), (90, 2), (120, 2), (120.1, 3)])
def test_dbp_boundaries(value, level):
    r = RULES["DBP"]
    assert discretise_series(pd.Series([value]), r["ge"], r["gt"]).iloc[0] == level


@pytest.mark.parametrize("value,level", [(39.9, 0), (40, 1), (60, 1), (60.1, 2)])
def test_hdl_boundaries_are_inclusive_at_both_ends(value, level):
    r = RULES["HDLcholestrol"]
    assert discretise_series(pd.Series([value]), r["ge"], r["gt"]).iloc[0] == level


def test_missing_rows_are_dropped_and_labels_untouched():
    raw = pd.read_csv(FIX / "sample_raw.csv").head(3)
    raw.loc[1, "SBP"] = np.nan
    got = discretise(raw)
    assert len(got) == 2
    assert set(got["IDFMetsynd"]) <= {0.0, 1.0}


def test_level_ranges():
    got = discretise(pd.read_csv(FIX / "sample_raw.csv"))
    for col, rule in RULES.items():
        assert got[col].between(0, len(rule["ge"]) + len(rule["gt"])).all()


def test_raw_data_schema():
    raw = pd.read_csv(ROOT / "data.csv")
    assert list(raw.columns) == COLUMNS
    assert raw.isna().sum().sum() == 0


@pytest.mark.xfail(reason="Real data problem (see review.md): data.csv has a diastolic "
                          "pressure of 0, which is a recording error, not a measurement.",
                   strict=True)
def test_diastolic_pressure_is_physiologically_plausible():
    raw = pd.read_csv(ROOT / "data.csv")
    assert (raw["DBP"] >= 20).all()
