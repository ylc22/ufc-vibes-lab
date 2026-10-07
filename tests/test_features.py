import pandas as pd
from src.features import add_fun_metrics

def test_fun_metrics_are_computed():
    df = pd.DataFrame([{
        "slpm": 5.0, "sapm": 3.0, "str_acc": 0.5, "str_def": 0.6,
        "td_avg": 2.0, "td_acc": 0.4, "td_def": 0.8, "sub_avg": 1.0,
        "wins": 10, "losses": 2, "draws": 0,
    }])
    out = add_fun_metrics(df)
    assert out.loc[0, "chaos_index"] == 8.0
    assert out.loc[0, "human_backpack_score"] > 0
    assert out.loc[0, "nope_button"] == 0.7
    assert out.loc[0, "octagon_tax_rate"] == 0.6
