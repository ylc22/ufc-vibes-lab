"""Feature engineering for UFC fighter career statistics."""

from __future__ import annotations

import numpy as np
import pandas as pd

CORE_COLUMNS = [
    "slpm", "sapm", "str_acc", "str_def",
    "td_avg", "td_acc", "td_def", "sub_avg",
]

def safe_divide(a: pd.Series, b: pd.Series, floor: float = 0.25) -> pd.Series:
    return a / b.clip(lower=floor)

def add_fun_metrics(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["chaos_index"] = out["slpm"] + out["sapm"]
    out["just_bleed_score"] = 0.65 * out["slpm"] + 0.35 * out["sapm"]
    out["human_backpack_score"] = out["td_avg"] + 1.5 * out["sub_avg"] + 2.0 * out["td_acc"]
    out["nope_button"] = 0.5 * out["str_def"] + 0.5 * out["td_def"]
    out["technical_bully_score"] = out["slpm"] * out["str_acc"] + 0.5 * out["td_avg"] * out["td_acc"]
    out["octagon_tax_rate"] = safe_divide(out["sapm"], out["slpm"])
    out["activity_score"] = np.log1p(
        out["wins"].fillna(0) + out["losses"].fillna(0) + out["draws"].fillna(0)
    )
    return out
