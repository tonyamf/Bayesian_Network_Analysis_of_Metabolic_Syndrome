"""Clinical-threshold discretisation used in preprocess.ipynb (cells 6-11).

The notebook did this with sequential in-place ``df.loc[...] = k`` assignments.
Here the same rules are written once as data, so they can be tested. Each
variable has "ge" edges (value >= edge moves up one level) and "gt" edges
(value > edge moves up one level), which reproduces the notebook's mixed
inclusive/exclusive boundaries, e.g. HDL 40..60 inclusive is level 1.
"""
import pandas as pd

RULES = {
    "DBP": {"ge": [80, 90], "gt": [120]},
    "SBP": {"ge": [120, 130, 140], "gt": [180]},
    "FastingBloodSugar": {"ge": [100, 126], "gt": []},
    "Triglycerides": {"ge": [150, 200, 500], "gt": []},
    "HDLcholestrol": {"ge": [40], "gt": [60]},
    "LDLcholestrol": {"ge": [100, 130, 160, 190], "gt": []},
}


def discretise_series(values: pd.Series, ge, gt) -> pd.Series:
    level = pd.Series(0, index=values.index)
    for edge in ge:
        level += (values >= edge).astype(int)
    for edge in gt:
        level += (values > edge).astype(int)
    return level


def discretise(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with the six measurements replaced by level codes.

    IDFMetsynd and ATPMetssynd are already 0/1 and are left unchanged.
    Rows with missing values are dropped first, as in the notebook.
    """
    out = df.dropna().copy()
    for column, rule in RULES.items():
        out[column] = discretise_series(out[column], rule["ge"], rule["gt"])
    return out
