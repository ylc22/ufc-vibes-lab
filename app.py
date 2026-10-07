from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path("data/fighters_clustered.csv")

st.set_page_config(page_title="UFC Vibes Lab", page_icon="🥊", layout="wide")
st.title("🥊 UFC Vibes Lab")
st.caption("Unsupervised fighter archetypes + deeply unserious metrics built from career statistics.")

if not DATA_PATH.exists():
    st.warning("Run `python -m src.pipeline --limit 150` first to build the dataset.")
    st.stop()

df = pd.read_csv(DATA_PATH)

metric_labels = {
    "chaos_index": "Chaos Index 🌪️",
    "just_bleed_score": "Just Bleed Score 🩸",
    "human_backpack_score": "Human Backpack Score 🎒",
    "nope_button": "Nope Button 🛑",
    "technical_bully_score": "Technical Bully Score 🧠",
    "octagon_tax_rate": "Octagon Tax Rate 💸",
}

left, right = st.columns([1, 2])
with left:
    archetypes = sorted(df["archetype"].dropna().unique())
    selected = st.multiselect("Archetypes", archetypes, default=archetypes)
    metric = st.selectbox("Leaderboard metric", list(metric_labels), format_func=metric_labels.get)
    top_n = st.slider("Top fighters", 5, 25, 10)

filtered = df[df["archetype"].isin(selected)].copy()

with right:
    st.subheader(metric_labels[metric])
    board = filtered.nlargest(top_n, metric)[["fighter", "nickname", "archetype", metric]]
    st.dataframe(board, use_container_width=True, hide_index=True)

st.divider()
x = st.selectbox("X axis", ["slpm", "td_avg", "str_acc", "nope_button", "human_backpack_score"], index=0)
y = st.selectbox("Y axis", ["sapm", "just_bleed_score", "chaos_index", "octagon_tax_rate"], index=2)

fig = px.scatter(
    filtered, x=x, y=y, color="archetype", hover_name="fighter",
    hover_data=["nickname", "wins", "losses"], title=f"{x} vs {y}"
)
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("🔬 Fighter profile")
fighter = st.selectbox("Choose a fighter", sorted(filtered["fighter"].unique()))
row = filtered.loc[filtered["fighter"] == fighter].iloc[0]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Archetype", row["archetype"])
c2.metric("Chaos Index", f"{row['chaos_index']:.2f}")
c3.metric("Backpack Score", f"{row['human_backpack_score']:.2f}")
c4.metric("Nope Button", f"{row['nope_button']:.2f}")

st.write({
    "record": f"{int(row['wins'])}-{int(row['losses'])}-{int(row['draws'])}",
    "SLpM": round(row["slpm"], 2),
    "SApM": round(row["sapm"], 2),
    "Striking accuracy": round(row["str_acc"], 3),
    "Takedowns / 15 min": round(row["td_avg"], 2),
    "Takedown defense": round(row["td_def"], 3),
    "Octagon tax rate": round(row["octagon_tax_rate"], 2),
})

st.caption("For entertainment and analytics only. Not a betting model.")
