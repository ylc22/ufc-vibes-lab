import pandas as pd
from src.archetypes import cluster_fighters
from src.features import CORE_COLUMNS

def test_cluster_fighters_adds_labels():
    rows = []
    for i in range(12):
        rows.append({
            "fighter": f"Fighter {i}",
            "slpm": 2 + (i % 4),
            "sapm": 1.5 + (i % 3),
            "str_acc": 0.35 + 0.02 * i,
            "str_def": 0.45 + 0.01 * (i % 5),
            "td_avg": 0.4 * (i % 5),
            "td_acc": 0.25 + 0.03 * (i % 4),
            "td_def": 0.5 + 0.02 * (i % 5),
            "sub_avg": 0.2 * (i % 4),
        })
    df = pd.DataFrame(rows)
    out = cluster_fighters(df, n_clusters=3)
    assert len(out) == len(df)
    assert out["archetype"].notna().all()
    assert set(CORE_COLUMNS).issubset(out.columns)
