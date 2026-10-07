"""End-to-end data pipeline."""

from __future__ import annotations
import argparse
from pathlib import Path
from .archetypes import cluster_fighters
from .features import add_fun_metrics
from .scrape import scrape

def main() -> None:
    parser = argparse.ArgumentParser(description="Build UFC fighter vibes dataset")
    parser.add_argument("--limit", type=int, default=150)
    parser.add_argument("--clusters", type=int, default=6)
    parser.add_argument("--delay", type=float, default=0.35)
    args = parser.parse_args()

    out_dir = Path("data")
    out_dir.mkdir(exist_ok=True)

    raw = scrape(limit=args.limit, delay=args.delay)
    raw.to_csv(out_dir / "fighters_raw.csv", index=False)

    features = add_fun_metrics(raw)
    features.to_csv(out_dir / "fighters_features.csv", index=False)

    clustered = cluster_fighters(features, n_clusters=args.clusters)
    clustered.to_csv(out_dir / "fighters_clustered.csv", index=False)

    print(f"Saved {len(clustered)} clustered fighters to {out_dir/'fighters_clustered.csv'}")

if __name__ == "__main__":
    main()
