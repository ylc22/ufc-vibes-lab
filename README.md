# 🥊 UFC Vibes Lab

> **A completely serious data project about an extremely unserious question:**  
> _Which UFC fighters are technicians, human backpacks, damage merchants, or pure chaos?_

`UFC Vibes Lab` is an end-to-end analytics project that pulls publicly available career statistics from **UFCStats**, engineers interpretable fighter-style features, clusters fighters into style archetypes, and computes a handful of intentionally ridiculous-but-reproducible metrics.

The goal is not to predict fight outcomes. It is to demonstrate a clean analytics workflow with web ingestion, feature engineering, unsupervised learning, testing, CI, and an interactive dashboard.

## ✨ What it does

| Metric | What it means |
|---|---|
| **Chaos Index** 🌪️ | How much striking action tends to happen around a fighter |
| **Just Bleed Score** 🩸 | High output + high absorption = appointment television |
| **Human Backpack Score** 🎒 | Takedowns + submissions + takedown accuracy |
| **Nope Button** 🛑 | Defensive ability across striking and takedowns |
| **Technical Bully Score** 🧠 | Offensive efficiency without rewarding volume alone |
| **Octagon Tax Rate** 💸 | Damage absorbed for every unit of offense landed |

Data-driven archetypes include:

- 🧠 **Technical Sniper**
- 🌪️ **Certified Chaos Merchant**
- 🎒 **Human Backpack**
- 🛡️ **Defensive Goblin**
- 🔨 **Pressure Technician**
- 🤷 **Beautiful Statistical Mystery**

The labels are assigned from cluster-level feature profiles, not fighter identities.

## 🧪 Questions this project asks

- Who creates the most total striking chaos per minute?
- Which fighters absorb suspicious amounts of damage while still producing offense?
- Who has the strongest wrestling/grappling statistical profile?
- Who is unusually hard to hit _and_ hard to take down?
- Do recognizable fighting styles emerge naturally from career statistics?
- Which fighter pays the highest **Octagon Tax Rate**?

## 🏗️ Project structure

```text
ufc-vibes-lab/
├── app.py
├── src/
│   ├── scrape.py
│   ├── features.py
│   ├── archetypes.py
│   └── pipeline.py
├── tests/
│   ├── test_features.py
│   └── test_archetypes.py
├── .github/workflows/ci.yml
├── requirements.txt
├── LICENSE
└── README.md
```

## 🚀 Quickstart

```bash
git clone https://github.com/ylc22/ufc-vibes-lab.git
cd ufc-vibes-lab

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.pipeline --limit 150
streamlit run app.py
```

The pipeline writes:

```text
data/fighters_raw.csv
data/fighters_features.csv
data/fighters_clustered.csv
```

The scraper is intentionally polite: it uses a descriptive user agent, request timeouts, and a delay between fighter-detail requests.

## 📊 Engineered metrics

### Chaos Index 🌪️
```text
Chaos = SLpM + SApM
```
If both you and your opponent are landing constantly, congratulations: you are the weather.

### Just Bleed Score 🩸
```text
Just Bleed = 0.65 × SLpM + 0.35 × SApM
```

### Human Backpack Score 🎒
```text
Backpack = TD Avg + 1.5 × Sub Avg + 2 × TD Accuracy
```

### Nope Button 🛑
```text
Nope = 0.5 × Striking Defense + 0.5 × Takedown Defense
```

### Octagon Tax Rate 💸
```text
Tax = SApM / max(SLpM, 0.25)
```

## 🤖 Style archetypes

The project standardizes career features and applies **K-Means clustering** across:

- significant strikes landed per minute
- significant strikes absorbed per minute
- striking accuracy
- striking defense
- takedowns per 15 minutes
- takedown accuracy
- takedown defense
- submissions per 15 minutes

Cluster names come from aggregate cluster profiles. The same algorithm may produce different archetypes depending on the dataset size.

## 🖥️ Dashboard

The Streamlit app includes:

- searchable fighter table
- metric leaderboards
- archetype filters
- interactive scatter plots
- fighter profile cards
- hoverable records and nicknames

Recommended plots:

- `Chaos Index` vs `Nope Button`
- `Human Backpack Score` vs `Just Bleed Score`
- `SLpM` vs `SApM`, colored by archetype

## ✅ Engineering choices

This repo is intentionally more than a notebook:

- reusable Python modules
- typed feature functions
- resilient HTML parsing
- deterministic clustering
- unit tests
- GitHub Actions CI
- cached local CSV outputs
- dashboard separated from ingestion logic
- no hard-coded fighter rankings

## ⚠️ Limitations

Career statistics are useful summaries, not complete measures of fighter quality.

- UFCStats aggregates career-level statistics across changing opponents and eras.
- Fighter statistics are not adjusted for opponent strength.
- Style and performance change over time.
- Some fighters have very small UFC samples.
- K-Means assumes Euclidean cluster structure.
- The funny metrics are intentionally heuristic.
- This project is **not** a betting model.

## 🧠 Why build this?

Because “I built another Titanic classifier” has never made anyone want to open a GitHub repo.

This project shows:

**data ingestion → cleaning → feature engineering → unsupervised ML → interpretation → testing → dashboard**

...while answering questions that sound like they were invented during a pay-per-view watch party.

## 📚 Data source

Career statistics are retrieved from **UFCStats.com** at runtime.

This repository does not redistribute a large scraped UFCStats dataset. Please use the scraper responsibly and respect the source site's terms and availability.

## 🛣️ Roadmap

- [ ] rolling fighter statistics by fight date
- [ ] weight-class normalized metrics
- [ ] opponent-strength adjustment
- [ ] PCA / UMAP visualization
- [ ] “style matchup weirdness” score
- [ ] southpaw tax analysis
- [ ] age / reach / height interaction analysis
- [ ] fight-network graph
- [ ] automatic nickname hall of fame

## 📜 License

MIT.

### Final scientific conclusion

Some fighters optimize distance management.

Some optimize top control.

Some optimize damage efficiency.

And some appear to optimize **making Dana White stand up from his chair**.
