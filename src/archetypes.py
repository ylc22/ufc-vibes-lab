"""Unsupervised fighter-style clustering and interpretable archetype labels."""

from __future__ import annotations
from typing import Dict
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from .features import CORE_COLUMNS

def _cluster_name(profile: pd.Series, overall: pd.Series) -> str:
    above = profile - overall
    if above["td_avg"] > 0.45 and above["sub_avg"] > 0.20:
        return "🎒 Human Backpack"
    if above["slpm"] > 0.50 and above["sapm"] > 0.40:
        return "🌪️ Certified Chaos Merchant"
    if above["str_def"] > 0.40 and above["td_def"] > 0.35:
        return "🛡️ Defensive Goblin"
    if above["str_acc"] > 0.35 and above["slpm"] > 0.20:
        return "🧠 Technical Sniper"
    if above["td_avg"] > 0.35:
        return "🤼 Chain-Wrestling Enthusiast"
    if above["slpm"] > 0.30:
        return "🔨 Pressure Technician"
    return "🤷 Beautiful Statistical Mystery"

def cluster_fighters(df: pd.DataFrame, n_clusters: int = 6) -> pd.DataFrame:
    clean = df.dropna(subset=CORE_COLUMNS).copy()
    if len(clean) < n_clusters:
        raise ValueError("Need at least as many complete fighters as clusters.")

    pipe = Pipeline([
        ("scale", StandardScaler()),
        ("cluster", KMeans(n_clusters=n_clusters, random_state=42, n_init=20)),
    ])
    clean["cluster"] = pipe.fit_predict(clean[CORE_COLUMNS])

    standardized = pd.DataFrame(
        pipe.named_steps["scale"].transform(clean[CORE_COLUMNS]),
        columns=CORE_COLUMNS,
        index=clean.index,
    )
    standardized["cluster"] = clean["cluster"]

    cluster_profiles = standardized.groupby("cluster")[CORE_COLUMNS].mean()
    overall = standardized[CORE_COLUMNS].mean()

    labels: Dict[int, str] = {
        int(cluster_id): _cluster_name(profile, overall)
        for cluster_id, profile in cluster_profiles.iterrows()
    }
    clean["archetype"] = clean["cluster"].map(labels)
    return clean
