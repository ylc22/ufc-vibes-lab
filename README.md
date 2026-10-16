# 🥊 UFC Vibes Lab

<p align="center">
  <img src="assets/octagon-chaos.svg" alt="Animated UFC data octagon" width="900">
</p>

> **A deeply serious analytics project about extremely unserious fighter archetypes.**

Because sometimes “significant strikes absorbed per minute” is a statistic.

And sometimes it is a **lifestyle**.

---

## 🧠 What this project actually does

- 📥 Pulls public career stats from **UFCStats**
- 🧹 Cleans and validates fighter data
- 🧮 Engineers interpretable style metrics
- 🤖 Clusters fighters with **K-Means**
- 🏷️ Gives clusters absurd-but-readable names
- 📊 Serves everything in a **Streamlit dashboard**
- ✅ Runs tests in **GitHub Actions**
- 🚫 Does **not** tell you what to bet on
- 🥴 Does occasionally tell you who statistically appears to enjoy chaos

The pipeline is basically:

**scrape → clean → feature engineer → cluster → judge vibes → dashboard**

---

## 😂 The important scientific metrics

- 🌪️ **Chaos Index** — How much striking activity happens whenever this person enters the cage. High score = the octagon becomes a weather event.
- 🩸 **Just Bleed Score** — Rewards output, but also gives partial credit for getting hit a lot. Defense is apparently optional DLC.
- 🎒 **Human Backpack Score** — Takedowns + submissions + takedown accuracy. High score = your opponent now has a 170 lb carry-on.
- 🛑 **Nope Button** — Combines striking defense and takedown defense. High score = “absolutely not, thank you.”
- 🧠 **Technical Bully Score** — Efficient offense without blindly rewarding volume. Being mean, but spreadsheet-approved.
- 💸 **Octagon Tax Rate** — Damage absorbed relative to offense landed. Some fighters pay sales tax. Some pay **face tax**.

---

## 🧬 Fighter archetypes

- 🧠 **Technical Sniper**
- 🌪️ **Certified Chaos Merchant**
- 🎒 **Human Backpack**
- 🛡️ **Defensive Goblin**
- 🔨 **Pressure Technician**
- 🤼 **Chain-Wrestling Enthusiast**
- 🤷 **Beautiful Statistical Mystery**

These names come from **cluster-level feature profiles**.

So no, I did not manually look at a fighter and say:

> “yeah, this guy has Defensive Goblin energy.”

The math did that.

Probably.

---

## 🧪 Questions this repo can answer

- Who creates the most total striking chaos per minute?
- Who has a worrying relationship with absorbing punches?
- Who statistically treats opponents like backpacks?
- Who is hard to hit **and** hard to take down?
- Which fighting styles emerge naturally from career stats?
- Who pays the highest **Octagon Tax Rate**?
- Who is technically efficient but spiritually allergic to peace?

---

## 🚀 Quickstart

1. Clone: `git clone https://github.com/ylc22/ufc-vibes-lab.git`
2. Enter the repo: `cd ufc-vibes-lab`
3. Create env: `python -m venv .venv`
4. Activate it:
   - macOS / Linux: `source .venv/bin/activate`
   - Windows PowerShell: `.\\.venv\\Scripts\\Activate.ps1`
5. Install: `pip install -r requirements.txt`
6. Build data: `python -m src.pipeline --limit 150`
7. Launch: `streamlit run app.py`

Then open the dashboard and begin making statistically responsible accusations.

---

## 🏗️ Repo layout

- `app.py` — dashboard
- `src/scrape.py` — polite UFCStats ingestion
- `src/features.py` — funny-but-interpretable metrics
- `src/archetypes.py` — clustering + labels
- `src/pipeline.py` — end-to-end orchestration
- `tests/` — checks so the goblins stay deterministic
- `assets/octagon-chaos.svg` — animated cartoon chaos
- `.github/workflows/ci.yml` — robot referee
- `CONTRIBUTING.md` — how to enter the cage without breaking things

---

## 📊 Metric formulas, because apparently we are professionals

- 🌪️ **Chaos Index** = `SLpM + SApM`  
  If both fighters are landing constantly, congratulations: the cage has become a natural disaster.

- 🩸 **Just Bleed Score** = `0.65 × SLpM + 0.35 × SApM`  
  High offense is good. High absorption is not good. Combining both is excellent television.

- 🎒 **Human Backpack Score** = `TD Avg + 1.5 × Sub Avg + 2 × TD Accuracy`  
  The unofficial “please get off me” index.

- 🛑 **Nope Button** = `0.5 × Striking Defense + 0.5 × Takedown Defense`  
  Measures the statistical frequency of “no ❤️”.

- 💸 **Octagon Tax Rate** = `SApM / max(SLpM, 0.25)`  
  How much punishment you pay for the privilege of doing offense.

---

## 🤖 What the ML is doing

- Standardizes career-level fighter features
- Uses **K-Means clustering**
- Keeps the process deterministic with a fixed random seed
- Builds cluster-level summaries
- Assigns readable archetype names from the cluster profile
- Avoids hard-coding fighter identities into the logic

Features include:

- significant strikes landed per minute
- significant strikes absorbed per minute
- striking accuracy
- striking defense
- takedowns per 15 minutes
- takedown accuracy
- takedown defense
- submissions per 15 minutes

It is unsupervised.

Which is a sophisticated way of saying:

> “I gave the algorithm a bunch of fighters and let it develop opinions.”

---

## 🖥️ Dashboard features

- 🔎 searchable fighter table
- 🏆 metric leaderboards
- 🎭 archetype filters
- 📈 interactive scatter plots
- 🧬 fighter profile cards
- 👀 hoverable nicknames and records
- 🔬 fighter-by-fighter stat inspection

Recommended plots:

- `Chaos Index` vs `Nope Button`
- `Human Backpack Score` vs `Just Bleed Score`
- `SLpM` vs `SApM`, colored by archetype

The third one is especially useful for finding fighters who live in the **upper-right quadrant of consequences**.

---

## ✅ Why this is more than a joke repo

Under the memes, it still has:

- modular Python
- reusable feature functions
- web ingestion
- data validation
- deterministic clustering
- unit tests
- CI
- reproducible outputs
- interactive visualization
- explicit limitations
- no hard-coded “best fighter” rankings

So yes, the project contains the phrase **Defensive Goblin**.

It also has a functioning ML/data pipeline.

Both can be true.

---

## ⚠️ Limitations

- Career stats compress years of fights into averages
- Opponent strength is not adjusted for
- Fighters evolve over time
- Small sample sizes can be weird
- K-Means is not a sacred law of combat sports
- Funny metrics are heuristic by design
- This is **not a betting model**
- The existence of a “Chaos Index” does not mean chaos is causal

Please do not mortgage your house because someone scored highly on **Human Backpack Score**.

---

## 🧠 Why I built this

Because:

- another Titanic classifier would have made me sad
- sports data is fun
- clustering is easier to explain when the result is “Defensive Goblin”
- dashboards are better when the variables sound mildly unhinged
- recruiters are more likely to remember **Octagon Tax Rate** than `project_final_v7.ipynb`

The real technical story is:

**data ingestion → cleaning → feature engineering → unsupervised ML → interpretation → testing → dashboard**

The fake technical story is:

**fighter goes bonk → Python takes notes**

---

## 🛣️ Roadmap

- [ ] weight-class normalized chaos
- [ ] rolling stats by fight date
- [ ] opponent-strength adjustment
- [ ] PCA / UMAP fight-style map
- [ ] “style matchup weirdness” score
- [ ] southpaw tax analysis
- [ ] age / reach / height interactions
- [ ] fight-network graph
- [ ] nickname hall of fame
- [ ] “who fights like your manager?” classifier
- [ ] “this matchup has HR implications” score
- [ ] absolutely unnecessary radar charts

---

## 📚 Data source

Career statistics are retrieved from **UFCStats.com** at runtime.

The scraper is intentionally polite:

- descriptive user agent
- request timeout
- small delay between detail requests
- no access-control bypassing
- no giant scraped dataset committed to the repo

---

## 📜 License

MIT.

Use responsibly.

Do not use this repo to settle family arguments about who would win in a cage.

---

## 🧾 Final scientific conclusion

- Some fighters optimize distance management.
- Some optimize top control.
- Some optimize damage efficiency.
- Some optimize making analysts say “interesting.”
- Some optimize making commentators yell.
- And some appear to optimize **making Dana White stand up from his chair**.

**Peer review pending.**
